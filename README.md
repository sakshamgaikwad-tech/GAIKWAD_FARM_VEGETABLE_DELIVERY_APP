<div align="center">

#  GAIKWAD FARM

### Hyperlocal Vegetable Delivery & Franchise Platform

[![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)](https://flutter.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Razorpay](https://img.shields.io/badge/Razorpay-02042B?style=for-the-badge&logo=razorpay&logoColor=white)](https://razorpay.com)

*Empowering local vegetable vendors through scalable digital commerce.*

</div>

---

##  Overview

**GAIKWAD FARM** is a modern hyperlocal vegetable delivery platform designed to transform traditional vegetable shops into scalable digital businesses. Inspired by platforms like Swiggy, Blinkit, and Zomato, it focuses specifically on fresh produce delivery — enabling online ordering, live tracking, secure payments, and future franchise expansion.

---

##  Features

###   Customer
- User authentication & profile management
- Browse fresh vegetables, fruits & groceries
- Smart product search
- Cart management & order placement
- Online payments via Razorpay (UPI, Cards, Wallets, Net Banking)
- Live order tracking with Google Maps
- Delivery notifications
- Address management
- Mobile-responsive UI

###  Admin
- Product & inventory management
- Order monitoring & delivery assignment
- Customer management
- Sales analytics & revenue tracking

###  Delivery Partner
- Dedicated delivery login
- Order acceptance & live navigation
- Delivery status updates with OTP verification
- Earnings dashboard

###  Franchise System *(Coming Soon)*
- Franchise registration & area management
- Revenue sharing & multi-store operations
- Franchise analytics dashboard

###  AI Features *(Coming Soon)*
- Smart demand prediction & inventory forecasting
- Dynamic pricing system
- AI freshness detection
- Personalized product recommendations
- AI-powered customer support chatbot

---

##  Architecture

```
Flutter Mobile App
       ↓
  FastAPI Backend
       ↓
PostgreSQL Database
       ↓
Admin Dashboard Panel
       ↓
Delivery Management System
       ↓
Franchise Management
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Mobile Frontend | Flutter / Dart | Cross-platform mobile app |
| Backend | FastAPI (Python) | REST API development |
| Database | PostgreSQL | Relational data storage |
| Authentication | JWT | Secure login & protected routes |
| Payments | Razorpay | UPI, Cards, Wallets, Net Banking |
| Notifications / OTP | Firebase | Push notifications & OTP login |
| Maps & Tracking | Google Maps API | Live delivery tracking |
| Hosting | Render | Backend deployment |
| Version Control | Git & GitHub | Source control |
| API Testing | Postman | API development & testing |
| UI/UX Design | Figma | Prototyping & design |

---

##  Project Structure

```
GAIKWAD_FARM/
│
├── backend_fastapi/
│   ├── app/
│   │   ├── models/         # Database models
│   │   ├── routes/         # API route handlers
│   │   ├── services/       # Business logic
│   │   └── utils/          # Helper functions
│   ├── main.py
│   └── requirements.txt
│
├── frontend_flutter/
│   ├── lib/
│   │   ├── screens/        # App screens
│   │   ├── widgets/        # Reusable UI components
│   │   ├── services/       # API service layer
│   │   └── main.dart
│
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.9+
- Flutter SDK 3.x
- PostgreSQL
- Git

---

### Backend Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/GAIKWAD_FARM.git
cd GAIKWAD_FARM/backend_fastapi

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install fastapi uvicorn pydantic psycopg2-binary python-jose passlib

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your DB credentials, JWT secret, Razorpay keys, etc.

# 5. Start the development server
uvicorn main:app --reload
```

> API documentation available at: `http://127.0.0.1:8000/docs`

---

### Flutter Setup

```bash
# 1. Navigate to the frontend folder
cd ../frontend_flutter

# 2. Install Flutter dependencies
flutter pub get

# 3. Run the app
flutter run
```

---

## 🔌 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/products` | Fetch all products |
| `POST` | `/products` | Add a new product |
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | User login (returns JWT) |
| `GET` | `/orders` | Fetch user orders |
| `POST` | `/orders` | Place a new order |

---

##  Database Schema

### Users
| Column | Type | Description |
|---|---|---|
| `id` | UUID | Primary key |
| `name` | VARCHAR | Full name |
| `email` | VARCHAR | Unique email |
| `password` | VARCHAR | Hashed password |
| `phone` | VARCHAR | Contact number |

### Products
| Column | Type | Description |
|---|---|---|
| `id` | UUID | Primary key |
| `name` | VARCHAR | Product name |
| `price` | DECIMAL | Price per unit |
| `stock` | INTEGER | Available quantity |
| `image` | TEXT | Image URL |

### Orders
| Column | Type | Description |
|---|---|---|
| `id` | UUID | Primary key |
| `user_id` | UUID | Foreign key → Users |
| `total_amount` | DECIMAL | Order total |
| `order_status` | VARCHAR | pending / confirmed / delivered |

---

##  Security

- **JWT Authentication** — stateless, token-based login
- **Secure Password Hashing** — bcrypt via passlib
- **Protected API Routes** — all sensitive endpoints require a valid token

**Planned:**
- OTP-based login via Firebase
- Google OAuth 2.0

---

## 💳 Payments

Powered by **Razorpay** with support for:

| Method | Status |
|---|---|
| UPI | ✅ Supported |
| Debit / Credit Cards | ✅ Supported |
| Wallets | ✅ Supported |
| Net Banking | ✅ Supported |

---

## 🚀 Deployment

| Service | Platform | Status |
|---|---|---|
| Backend API | Render | ✅ Live |
| Database | PostgreSQL (Render) | ✅ Live |
| Mobile App | Google Play Store | 🔜 Upcoming |
| Version Control | GitHub | ✅ Active |

---

## 📈 Development Roadmap

```
Phase 1 — Foundation
  ✅ Backend APIs
  ✅ Flutter Customer App
  ✅ Product Management

Phase 2 — Core Commerce
  ✅ Authentication (JWT)
  ✅ Cart & Orders
  ✅ Razorpay Payment Integration

Phase 3 — Logistics & Operations
   Live Delivery Tracking
   Push Notifications
   Admin Dashboard

Phase 4 — Scale
  🔜 Franchise Management System
  🔜 AI-Powered Features
  🔜 Advanced Analytics Dashboard
```

---

## 🎯 Vision

GAIKWAD FARM aims to empower local vegetable vendors by providing a scalable digital commerce platform. The long-term goal is to modernize local vegetable businesses through technology — enabling online ordering, hyperlocal delivery, smart inventory management, and franchise-based expansion across regions.

---

##  Developer

**Saksham Gaikwad**

Focused on Full Stack Development, AI/ML Integration, and Startup Scalable Architecture.

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)

---

##  License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

*Built with  to modernize local vegetable commerce.*

</div>
