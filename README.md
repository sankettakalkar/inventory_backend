# Inventory Management Backend (FastAPI)

## Overview
This repository contains the **backend service** for the Inventory Management Application built for the Social Booster Media demo task.

The backend provides:
- REST APIs for full CRUD operations on inventory items
- Reporting APIs for dashboard visualizations
- Third-party API integration for currency conversion
- Health check endpoints
- PostgreSQL database integration

---

## Tech Stack

- **Python 3.9+**
- **FastAPI**
- SQLAlchemy ORM
- Pydantic
- PostgreSQL
- Uvicorn

---

## Live Backend URL

https://inventorybackend-production-0b9e.up.railway.app

---

## API Documentation

Swagger UI:
```
/docs
```

---

## Local Setup Instructions

### Prerequisites
- Python 3.9+
- PostgreSQL
- Virtual environment (recommended)

### Setup

```bash
git clone <backend-repo-url>
cd inventory-backend
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<db_name>
```

---

## Run Backend Locally

```bash
uvicorn app.main:app --reload
```

Backend runs at:
```
http://127.0.0.1:8000
```

---

## Database

- PostgreSQL is used as the primary database
- Tables are created automatically via SQLAlchemy models
- Managed PostgreSQL is used in production (Railway)

---

## API Endpoints

### Inventory CRUD
- `POST   /api/items`
- `GET    /api/items`
- `GET    /api/items/{id}`
- `PUT    /api/items/{id}`
- `DELETE /api/items/{id}`

### Reports
- `GET /api/reports/summary`

### Third-Party API Integration
- `GET /api/external/convert?currency=USD|EUR`

### Health Checks
- `GET /health`

---

## Deployment (Railway)

- Backend is deployed on **Railway**
- PostgreSQL plugin is used
- Start command:
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## Notes
- `.env` files are excluded from version control
- CORS is configured for local and deployed frontend domains
- Backend is production-ready

---

## Author
**Sanket Takalkar**
