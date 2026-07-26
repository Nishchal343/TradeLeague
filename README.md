# TradeLeague

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?logo=docker)
![Render](https://img.shields.io/badge/Deployment-Render-46E3B7)

TradeLeague is a **Django-based virtual trading platform** where users compete in simulated stock trading matches using virtual currency. Players can create or join private trading rooms, analyze market assets, make investment decisions, and track their performance through dashboards, rankings, and match statistics.

---

## Features

- User Registration & Login
- Session-based Authentication
- Dashboard with Profit, League, Win Streak & Statistics
- Leaderboard for Top Traders
- Create and Join Private Trading Rooms
- Trading Arena with Simulated Assets
- Investment & Portfolio Tracking
- Match Result Analysis
- Market Overview
- Responsive Pixel-Themed UI
- REST API using Django REST Framework
- Real-time Room Communication using Django Channels
- Docker Support
- Render Deployment

---

## Tech Stack

| Category | Technology |
|-----------|------------|
| Backend | Django, Django REST Framework |
| Frontend | HTML, CSS, JavaScript, Django Templates |
| Database | SQLite |
| Real-time | Django Channels (WebSockets) |
| Authentication | Django Session Authentication |
| Deployment | Render |
| Containerization | Docker |

---

## Architecture

```text
Browser
    │
    ▼
Django Views
    │
    ▼
Business Logic
    │
    ▼
SQLite Database
```

---

## Project Structure

```text
TradeLeague/
│
├── fintech_backend/      # Django project configuration
├── game/                 # Core application
├── nginx/                # Production configuration
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── manage.py
└── requirements.txt
```

---

## Local Setup

```bash
git clone <repository-url>

cd TradeLeague

python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py seed_assets

python manage.py runserver
```

Application runs at:

```
http://127.0.0.1:8000
```

---

## Docker

Build and run using Docker:

```bash
docker compose up --build
```

---

## Deployment

The project is deployed on **Render** using Docker.

Required environment variables include:

```
SECRET_KEY
DEBUG=False
CSRF_TRUSTED_ORIGINS
CORS_ALLOWED_ORIGINS
```

---

## Screenshots

Add screenshots here:

- Home Page
- Login
- Dashboard
- Trading Lobby
- Trading Arena
- Match Results

---

## Future Improvements

- Password Reset
- Email Verification
- Live Market Data Integration
- User Profile Management
- Enhanced Analytics Dashboard
- Notifications

---

## License

MIT License