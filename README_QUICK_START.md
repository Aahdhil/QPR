# QPR Application - Quick Start Guide

## Prerequisites
- Python 3.8+
- pip

---

## Installation (First Time Only)

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup database
python manage.py migrate

# 4. Create initial users
python create_users.py

# 5. Start server
python manage.py runserver
```

---

## Login Credentials

| Role | Code | Password |
|------|------|----------|
| Admin | 654 | password123 |
| HOD | 905 | password123 |

---

## Quick Access URLs

- **Login:** http://localhost:8000/login/
- **Register:** http://localhost:8000/register/
- **Admin Dashboard:** http://localhost:8000/admin-dashboard/
- **User Dashboard:** http://localhost:8000/dashboard/
- **HOD Dashboard:** http://localhost:8000/hod/dashboard/

---

## Running the Server (After First Time)

```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
python manage.py runserver
```

Visit: http://localhost:8000/login/

---

## Features

✅ **Admin** - Create/manage users, approve requests, edit HOD details
✅ **HOD** - View department employee status
✅ **Users** - Register, fill QPR forms, submit reports
✅ **Profile Editing** - Request approval to edit submitted profiles
✅ **QPR Management** - Draft, save, submit quarterly progress reports

---

## Important Notes

- **Database:** `db.sqlite3` (local only, not shared in code)
- **Passwords:** Change immediately in production
- **Static Files:** CSS/JS in `static/` folder
- **Templates:** HTML pages in `templates/` folder

---

## Troubleshooting

```bash
# Check for errors
python manage.py check

# Recreate database
rm db.sqlite3
python manage.py migrate
python create_users.py
```

---

**Questions?** Check project documentation or AUDIT_REPORT.md for detailed info.
