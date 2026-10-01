# Telangana Advertisement & Display Monitoring System (T-DDMS) • GPS CAM

An enterprise-grade, production-ready Android application and backend architecture for physically inspecting, geo-tagging, and monitoring advertisement TVs and digital display installations across the 33 districts of Telangana.

---

## 📱 Application Overview & Key Features

The application bridges field inspectors (vendors) and state municipal administrators:

1. **Strict Role-Based Access Control (RBAC):**
   - **Type 1: District-Specific Vendor:** Assigned one or more specific districts by the Admin. Authorization is enforced server-side via Firestore Security Rules. Vendors can neither submit nor query installations outside their assigned districts.
   - **Type 2: All-District Vendor:** Authorized to operate statewide across all 33 Telangana districts.
   - **State Administrator:** Complete dashboard to review vendor registrations, toggle operational scopes, manage Telangana districts and display categories, audit inspection submissions, and export CSV compliance logs.

2. **GPS Camera Geo-Tagging & Watermark Overlay:**
   - Automatically acquires authentic device GPS coordinates using Google Play Services Fused Location.
   - **Anti-Spoofing:** Actively detects mocked locations (`isMockLocation`) and rejects falsified inspections.
   - High-contrast GPS watermark banner stamped onto photos displaying:
     - Organization Emblem & Branding
     - Angle Identifier (`[FRONT VIEW]`, `[BACK VIEW]`, `[SIDE VIEW]`)
     - Vendor Name & District
     - Category (e.g. `CCTV Screens at ANNA Canteens`) & Landmark
     - Coordinates (`Lat 17.385044° N, Long 78.486671° E`) & Accuracy (`± 3.5m`)
     - Timestamp in Indian Standard Time (IST)
   - Preserves original raw photos on device while generating watermarked photos for audit submissions.

### 3. Pluggable Storage Architecture (Zero-Billing Default)
- **Local Storage Provider (`LocalStorageProvider`):** Default configuration. Stores high-resolution watermarked photos in isolated app-private storage (`files/inspections/{submissionId}/{IMAGE_TYPE}.jpg`) and syncs metadata to Cloud Firestore with status `LOCAL_STORED`. Enables complete offline functionality and zero-cost operation without requiring Google Cloud Billing setup.
- **Firebase Cloud Storage Provider (`FirebaseStorageProvider`):** Pluggable drop-in implementation ready for enterprise cloud deployments when Google Cloud Billing (Blaze plan) is provisioned.

4. **Modern UI/UX Philosophy:**
   - Preserves the emerald green visual identity (`#0D7E40`), clean white cards, rounded geometry, and large accessible buttons matching the government portal design language.
   - Responsive layouts avoiding keyboard overlap (`imePadding`), clipping, or distortion.

---

## 🏛️ Centralized Telangana District Directory

The application seeds and supports all **33 official districts** of Telangana:
`Adilabad`, `Bhadradri Kothagudem`, `Hanumakonda`, `Hyderabad`, `Jagtial`, `Jangaon`, `Jayashankar Bhupalpally`, `Jogulamba Gadwal`, `Kamareddy`, `Karimnagar`, `Khammam`, `Komaram Bheem Asifabad`, `Mahabubabad`, `Mahabubnagar`, `Mancherial`, `Medak`, `Medchal-Malkajgiri`, `Mulugu`, `Nagarkurnool`, `Nalgonda`, `Narayanpet`, `Nirmal`, `Nizamabad`, `Peddapalli`, `Rajanna Sircilla`, `Ranga Reddy`, `Sangareddy`, `Siddipet`, `Suryapet`, `Vikarabad`, `Wanaparthy`, `Warangal`, `Yadadri Bhuvanagiri`.

---

## 🔄 End-to-End Workflows

### 1. Vendor Onboarding & Approval Workflow
```
[ Vendor Registration Form ]
            │
            ▼
[ Status: PENDING_APPROVAL ]  (Access to protected functionality blocked)
            │
            ▼
[ Admin Reviews in Admin Portal ]
            ├── Reject -> Account Marked REJECTED
            └── Approve -> Admin selects Vendor Type:
                            ├── ALL_DISTRICTS
                            └── DISTRICT_SPECIFIC (Assigns specific districts)
                                    │
                                    ▼
                        [ Status: APPROVED ] -> Vendor Logs In
```

### 2. Field Inspection & Capture Workflow
```
[ Vendor Logs In ] -> [ Vendor Dashboard ]
            │
            ▼
[ Tap: "NEW INSPECTION / GEO TAGGING" ]
            │
            ├── 1. Select District (Filtered strictly to authorized districts)
            ├── 2. Select Category (e.g. CCTV Screens at ANNA Canteens)
            ├── 3. Enter Landmark Description (e.g. Near ANNA Canteen, Main Road)
            ├── 4. Acquire Real-Time Device GPS Lock
            │
            ├── 5. Capture FRONT Photo ───┐
            ├── 6. Capture BACK Photo  ───┼──> WatermarkRenderer stamps GPS banner
            └── 7. Capture SIDE Photo  ───┘
            │
            ▼
[ Review Stamped Photographs & Coordinates ]
            │
            ▼
[ Confirm & Submit Inspection ]
            ├── Active Provider: LocalStorageProvider -> Status: LOCAL_STORED (Zero Billing)
            └── Active Provider: FirebaseStorageProvider -> Status: PENDING_REVIEW (Blaze plan)
```

---

## 🛠️ Project Structure & Architecture

```
GPS CAM/
├── app/
│   ├── src/main/
│   │   ├── AndroidManifest.xml
│   │   ├── java/com/telangana/advertisement/monitoring/
│   │   │   ├── MonitoringApp.kt           # Application class & DI bootstrapper
│   │   │   ├── MainActivity.kt            # Edge-to-edge Compose host activity
│   │   │   ├── config/
│   │   │   │   └── Branding.kt            # Centralized logos, colors & constants
│   │   │   ├── data/
│   │   │   │   ├── model/Models.kt        # User, Vendor, Submission, Audit models
│   │   │   │   ├── model/TelanganaDistricts.kt # 33 TS Districts seed data
│   │   │   │   ├── local/AppDatabase.kt   # Room Database & DAOs
│   │   │   │   ├── remote/FirebaseSource.kt # Firebase Auth & Firestore client
│   │   │   │   └── repository/            # Repositories enforcing RBAC & caching
│   │   │   ├── domain/
│   │   │   │   ├── LocationHelper.kt      # Fused Location & mock detection
│   │   │   │   ├── ImageProcessor.kt      # EXIF rotation & JPEG compression
│   │   │   │   ├── WatermarkRenderer.kt   # GPS Camera overlay renderer
│   │   │   │   └── storage/               # Pluggable Storage Provider abstraction
│   │   │   ├── worker/UploadWorker.kt     # WorkManager background sync
│   │   │   ├── di/AppContainer.kt         # Dependency injection container
│   │   │   └── ui/
│   │   │       ├── theme/                 # Material 3 Green Theme
│   │   │       ├── common/Components.kt   # Reusable UI cards, buttons, badges
│   │   │       ├── auth/                  # Login & Registration screens
│   │   │       ├── vendor/                # Vendor Dashboard, Capture & Review
│   │   │       ├── admin/                 # Admin Dashboard, Approvals & Review
│   │   │       └── navigation/AppNavHost.kt # Jetpack Compose Navigation
│   │   └── res/                           # Colors, strings, drawables, XML
│   └── build.gradle.kts                   # App module Gradle configuration
├── firestore.rules                        # Server-side authorization rules
├── storage.rules                          # Cloud Storage directory isolation rules
├── firestore.indexes.json                 # Firestore compound query indexes
├── scripts/seed_telangana_districts.js    # Firebase Admin seeding script
├── gradle/libs.versions.toml              # Version catalog
├── SETUP.md                               # Firebase & environment setup guide
└── README.md                              # Project documentation
```

---

## 🧪 Testing

The repository includes unit tests verifying crucial business logic:
- `DistrictAuthorizationTest.kt`: Tests district-specific vs all-districts access rules, pending account restrictions, and admin bypass.
- `SubmissionValidationTest.kt`: Tests mandatory 3-photo validation, fake/mock GPS rejection, cloud storage URL persistence, and coordinate validity.

Run unit tests via Gradle:
```bash
./gradlew testDebugUnitTest
```

---

## 🚀 Building & Production Release

### Prerequisites
- JDK 17 (Java SE Runtime 17+)
- Android SDK with Platform 35 (`compileSdk = 35`, `minSdk = 24`)

### Build Production Signed Release APK
```bash
./gradlew assembleRelease
```
* **Output Path:** `app/build/outputs/apk/release/app-release.apk`
* **Package Name:** `com.telangana.advertisement.monitoring`
* **Version:** `1.0.0` (`versionCode = 1`)
* **Signature Scheme:** APK Signature Scheme v2 (Signed with 2048-bit RSA key)
* **Cloud Storage Bucket:** `telangana-ad-monitoring.firebasestorage.app`

### Install on Device via ADB
```bash
adb install -r app/build/outputs/apk/release/app-release.apk
```

### Build Debug APK
```bash
./gradlew assembleDebug
```
* **Output Path:** `app/build/outputs/apk/debug/app-debug.apk`
* **Package Name:** `com.telangana.advertisement.monitoring.debug`

### Authentication & Role Provisioning
Administrator and Employee accounts are securely provisioned via Firebase Authentication and Cloud Firestore according to strict least-privilege security rules. No credentials or passwords exist in source code or repositories.

See [SETUP.md](SETUP.md) for production Firebase deployment, security rules deployment, and service account key setup.
