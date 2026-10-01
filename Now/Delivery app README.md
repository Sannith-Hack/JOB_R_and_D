# 🍔 ZestBite Food Delivery Ecosystem

A modular, scalable, and migratable food-ordering platform engineered for high performance. Comprises a stateless Express.js backend with strict Repository and Dependency Injection patterns, a Next.js store management dashboard, and a native Java Android application localized for the Indian market.

---

## 📖 Complete Technical Documentation

All architecture diagrams, API references, database schemas, runbooks, and test matrices are maintained in the central documentation hub:

👉 **[Explore Full Project Documentation (`docs/README.md`)](docs/README.md)**

### Key Documentation Sections
- **[System Architecture](docs/architecture/system-architecture.md)**: End-to-end topology, component breakdown, and service contracts.
- **[REST API Reference](docs/api/README.md)**: Consumer (`/api/v1/app/*`) and admin (`/api/v1/admin/*`) endpoints.
- **[Mobile Application (Android)](docs/mobile/README.md)**: MVVM architecture, 5-tab navigation, CartManager, and UI design system.
- **[Database Architecture](docs/database/schema.md)**: TiDB Cloud distributed SQL schema, indexes, and connection pooling.
- **[Local Development Setup](docs/operations/local-development.md)**: Onboarding instructions for backend, web panel, and mobile.
- **[Master Test Matrix](docs/testing/test-matrix.md)**: Comprehensive multi-layered QA test inventory.
- **[Release Engineering](docs/git/commit-convention.md)**: Conventional Commits and milestone release guidelines.

---

## 🏛 Architecture Overview

```
                      +-----------------------------+
                      |   Mobile App (Android/Java)  |
                      |   MVVM + Retrofit + Glide   |
                      +--------------+--------------+
                                     |
                                     |  HTTP (Bearer JWT)
                                     v
                      +-----------------------------+
                      |      Load Balancer Proxy    |
                      +--------------+--------------+
                                     |
                                     v
                      +-----------------------------+
                      |   Unified Express Backend   |
                      |      Modular Routes         |
                      |  /api/v1/app  /api/v1/admin |
                      +--------------+--------------+
                                     |
          +--------------------------+--------------------------+
          | (Repository Pattern)     | (Storage Abstraction)    | (Payment Stub)
          v                          v                          v
+-------------------+      +-------------------+      +-------------------+
|   IDatabaseRepo   |      |  IStorageService  |      |  IPaymentService  |
+---------+---------+      +---------+---------+      +---------+---------+
          |                          |                          |
    +-----+-----+              +-----+-----+                    |
    |           |              |           |                    v
    v           v              v           v          +-------------------+
+-------+ +-----------+  +-----------+ +---------+    |   Mock Razorpay   |
| TiDB  | | Firestore |  |Cloudinary | |Firebase |    |  Gateway Provider |
| Cloud | |  (Ph 2)   |  |  (Ph 1)   | | Storage |    +-------------------+
+-------+ +-----------+  +-----------+ | (Ph 2)  |
                                       +---------+
```

---

## ⚡ Quick Start

### 1. Unified Backend
```bash
cd backend
npm install
npm test      # Executes full integration test suite
npm start     # Starts HTTP API at http://localhost:5000
```

### 2. Next.js Admin Dashboard
```bash
cd admin-dashboard
npm install
npm run dev   # Starts Next.js dashboard at http://localhost:3000
```
- Open `http://localhost:3000/login`
- Click **"Auto-Fill Admin Credentials"** (`admin@burgerking.com` / `Admin@123`) to enter.

### 3. Android Mobile Application
```powershell
cd mobile-app
.\gradlew.bat assembleDebug
```
- Generated APK: `mobile-app/app/build/outputs/apk/debug/app-debug.apk`

---

## 🔄 Phase 1 to Phase 2 Migration Switch

To migrate from **MySQL + Cloudinary** (Phase 1) to **Firebase Firestore + Firebase Storage** (Phase 2), **NO backend controllers or routes need to be modified**. Update driver switches in `backend/.env`:

```env
# Phase 2 (Zero code changes required):
DATABASE_DRIVER=firestore
STORAGE_DRIVER=firebase
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_CLIENT_EMAIL=firebase-adminsdk@your-project-id.iam.gserviceaccount.com
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
FIREBASE_STORAGE_BUCKET=your-project-id.appspot.com
```

The Dependency Injection container ([`src/services/container.js`](file:///D:/User/Desktop/delivery%20application/backend/src/services/container.js)) automatically swaps the concrete implementations.
