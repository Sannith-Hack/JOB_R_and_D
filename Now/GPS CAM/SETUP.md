# T-DDMS GPS CAM: Complete Firebase & Production Setup Guide

This guide details the step-by-step instructions for deploying and configuring the **Telangana Advertisement TV & Display Monitoring System (T-DDMS)** on Firebase, configuring Android build environments, deploying security rules, and maintaining strict secret isolation.

---

## 1. Architectural Security & Secret Separation

### Public Client Configuration (Safe in APK)
The following files and parameters are part of the standard Android client integration and are designed to identify the project endpoint:
- `app/google-services.json` (Contains `project_id`, `project_number`, `mobilesdk_app_id`, public client API key)
- `BuildConfig.ENV_NAME` ("development", "staging", "production")
- Application IDs and public storage bucket names

> **Crucial Rule:** Firebase Android client keys do NOT grant administrative access. Authorization and data security are strictly enforced by **Firestore Security Rules** (`firestore.rules`).

### Private Server Secrets (MUST NEVER BE BUNDLED IN APK)
- Firebase Admin Service Account Private Keys (`serviceAccountKey.json`)
- Firebase Admin SDK Tokens & Database Secrets
- Cloud Functions deployment secrets & environment keys

---

## 2. Production Storage Architecture (Firebase Cloud Storage Enabled)

### Active Backend: `FirebaseStorageProvider` (Google Cloud Storage)
Firebase Cloud Storage is fully enabled and active on the production bucket (`telangana-ad-monitoring.firebasestorage.app`):
- **Active Provider:** `FirebaseStorageProvider` wired into `AppContainer.kt`.
- **Upload Structure:** Watermarked high-resolution inspection photos are uploaded directly to:
  `vendors/{vendorId}/inspections/{submissionId}/{IMAGE_TYPE}.jpg`
- **Security & Authorization:** Server-side isolation enforced via [storage.rules](storage.rules). Only authenticated vendors can upload to their designated directory (max 10MB per image), and only state administrators can audit all vendor photos.
- **Offline Resiliency:** If a vendor captures inspections without internet connectivity, photos are safely persisted in Room local storage with status `UPLOAD_FAILED` (`syncPending = true`). Once connectivity returns, `WorkManager` (`UploadWorker`) automatically uploads photos to Firebase Cloud Storage and syncs metadata to Cloud Firestore.
- **Fallback / Local Provider:** `LocalStorageProvider` is retained in the architecture for local simulation or air-gapped field testing if needed.

---

## 3. Setting Up the Firebase Project

### Step 3.1: Create Firebase Project
1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click **Add Project** and name it (e.g. `telangana-ad-monitoring`).
3. (Optional) Enable Google Analytics for crash reports and monitoring.

### Step 3.2: Enable Authentication
1. Navigate to **Build > Authentication** in the Firebase console.
2. Click **Get Started**.
3. Under the **Sign-in method** tab, enable **Email/Password**.
4. Disable public self-registration if desired, or allow it since new registrations default to `PENDING_APPROVAL` status.

### Step 3.3: Create Cloud Firestore Database
1. Navigate to **Build > Firestore Database**.
2. Click **Create Database**.
3. Select region (e.g. `asia-south1` Mumbai).
4. Start in **Production mode** (Security rules deployed in Step 5).

---

## 4. Registering the Android Application

1. In the Project Overview, click the **Android** icon to add an Android app.
2. Enter the Package Name:
   - **Production:** `com.telangana.advertisement.monitoring`
   - **Development:** `com.telangana.advertisement.monitoring.debug`
3. Enter your SHA-1 fingerprint:
   ```bash
   # On Windows PowerShell:
   keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android
   ```
4. Download `google-services.json` and place it in `app/google-services.json`.

---

## 5. Deploying Firestore Security Rules & Indexes

Using the Firebase CLI:
```bash
npm install -g firebase-tools
firebase login
firebase use --add telangana-ad-monitoring --alias default
```

### Deploy Rules & Indexes
Run from the project root:
```bash
firebase deploy --only firestore:rules,firestore:indexes
```

The repository includes:
- [firestore.rules](firestore.rules): Enforces server-side district authorization, role-based access, and prevents vendor access to unauthorized districts.
- [firestore.indexes.json](firestore.indexes.json): Optimized indexes for compound queries on districts, timestamps, and approval statuses.

---

## 6. Seeding Telangana Districts & Categories

A Node.js administrative script is provided to seed the 33 official districts of Telangana and initial display categories:

1. Generate a Service Account Private Key:
   - In Firebase Console > **Project settings** > **Service accounts**.
   - Click **Generate new private key**.
   - Save the JSON file securely outside the Git repository (e.g. `C:\secrets\serviceAccountKey.json`).
2. Run the seeding script:
   ```bash
   cd scripts
   npm install firebase-admin
   $env:GOOGLE_APPLICATION_CREDENTIALS="C:\secrets\serviceAccountKey.json"
   node seed_telangana_districts.js
   ```

---

## 7. Environment Configurations (Dev, Staging, Prod)

| Environment | Application ID | Build Command | Purpose |
|---|---|---|---|
| **Development** | `com.telangana.advertisement.monitoring.debug` | `./gradlew assembleDebug` | Local development, debug buttons enabled |
| **Staging** | `com.telangana.advertisement.monitoring.staging` | `./gradlew assembleStaging` | QA testing, staging backend, UAT |
| **Production** | `com.telangana.advertisement.monitoring` | `./gradlew assembleRelease` | Field deployment, ProGuard enabled, debug prefill stripped |

---

## 8. Initial Administrative Account
 
To provision an Administrator:
1. In Firebase Console > Authentication, create a user with an administrative email (e.g., `admin@poojarigroup.com`) and a strong, complex password.
2. In Firestore > `users` collection, create a document where the Document ID equals the user's Auth UID:
   ```json
   {
     "id": "<AUTH_UID>",
     "email": "admin@poojarigroup.com",
     "username": "admin",
     "fullName": "Poojari Administrative Director",
     "phone": "+91 94400 12345",
     "role": "ADMIN",
     "status": "APPROVED",
     "employeeType": "ALL_DISTRICTS",
     "authorizedDistricts": [],
     "authorizedCanteens": [],
     "organization": "Anna Canteens",
     "createdAt": 1700000000000,
     "updatedAt": 1700000000000
   }
   ```
3. Admins log in via the single unified login screen. Roles and authorizations are strictly verified against Cloud Firestore security rules.
