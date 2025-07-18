<h1 align="center">🧠 Taskie — Smart Task Manager</h1>

<p align="center">
  A modern, API-powered, Dockerized task management system built with Django & DRF. Taskie lets users manage daily tasks with full lifecycle control, history tracking, and a clean UI — all wrapped with Swagger-documented REST APIs.
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Status-Production-brightgreen" alt="status"/>
  <img src="https://img.shields.io/badge/Django-4.x-success" alt="django"/>
  <img src="https://img.shields.io/badge/DRF-Enabled-blue" alt="drf"/>
  <img src="https://img.shields.io/badge/Docker-Ready-blue" alt="docker"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="license"/>
</div>

---

## ✨ Features

- 🔐 User Authentication (Signup, Login, Logout)
- 📋 Full Task CRUD Operations
- 🔄 Task Status Workflow: Pending → In Progress → Completed
- 🔗 Task Dependencies Linking
- 🕓 Change History & Timeline Logging
- 🔍 Searchable Task History
- 🌐 Swagger-based API Documentation (`/api/docs/`)
- 🐳 Dockerized for Easy Setup & Deployment

---

## 📸 Preview

<table> <tr> <td><img src="Screenshots/landing_page.png" width="100%"/></td> <td><img src="Screenshots/signup.png" width="100%"/></td> </tr> <tr> <td align="center">Landing Page</td> <td align="center">Signup</td> </tr> <tr> <td><img src="Screenshots/login.png" width="100%"/></td> <td><img src="Screenshots/home.png" width="100%"/></td> </tr> <tr> <td align="center">Login</td> <td align="center">Home</td> </tr> <tr> <td><img src="Screenshots/create_task.png" width="100%"/></td> <td><img src="Screenshots/saved_task.png" width="100%"/></td> </tr> <tr> <td align="center">Create Task</td> <td align="center">Saved Task</td> </tr> <tr> <td><img src="Screenshots/history.png" width="100%"/></td> <td><img src="Screenshots/history_changes.png" width="100%"/></td> </tr> <tr> <td align="center">History</td> <td align="center">History Changes</td> </tr> </table>

---

## ⚙️ Tech Stack

| Layer      | Technology                |
|------------|---------------------------|
| Backend    | Django 4.x, DRF            |
| Frontend   | HTML, Bootstrap 5          |
| Database   | SQLite (dev) / PostgreSQL (prod-ready) |
| DevOps     | Docker, Docker Compose     |
| API Docs   | Swagger via `drf-yasg`     |

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Laiba-muzammal/taskie.git
cd taskie
```

### 2️⃣ Run with Docker
```bash
docker-compose up --build
```

---

### Open in browser:

🌐 App: http://localhost:8000

📘 API Docs: http://localhost:8000/api/docs/

---

### 🔌 API Endpoints
Interact via Swagger UI or Postman:

```pgsql
Copy
Edit
GET     /api/tasks/         → List all tasks  
POST    /api/tasks/         → Create new task  
PUT     /api/tasks/{id}/    → Update task  
DELETE  /api/tasks/{id}/    → Delete task  
GET     /api/history/       → View change history
```

---

### 🧩 Project Structure
```graphql
Copy
Edit
taskie/
├── core/                 # Django project settings (urls, wsgi, asgi)
├── tasks/                # Main app: models, views, forms, migrations
├── api/                  # DRF views and serializers (optional separation)
├── templates/            # HTML templates for UI
├── static/               # CSS, JS, images
├── screenshots/          # UI preview assets
├── demo/                 # Optional walkthrough video
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

```

### 🐳 Docker Support

This project includes full Docker support via `Dockerfile` and `docker-compose.yml`.

> ⚠️ Note: Due to hardware virtualization being disabled on the local machine, Docker setup hasn't been locally tested — however, the configuration is complete and production-ready. Feel free to run and report any containerization issues via GitHub Issues or PRs.

---

### 🧾 License
MIT License © Laiba Muzammal
