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

<table>
  <tr>
    <td><img src="screenshots/dashboard.png" width="100%"/></td>
    <td><img src="screenshots/history.png" width="100%"/></td>
  </tr>
  <tr>
    <td align="center">Task Dashboard</td>
    <td align="center">Change History View</td>
  </tr>
</table>

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
2️⃣ Run with Docker
bash
Copy
Edit
docker-compose up --build
Open in browser:

🌐 App: http://localhost:8000

📘 API Docs: http://localhost:8000/api/docs/

🔌 API Endpoints
Interact via Swagger UI or Postman:

pgsql
Copy
Edit
GET     /api/tasks/         → List all tasks  
POST    /api/tasks/         → Create new task  
PUT     /api/tasks/{id}/    → Update task  
DELETE  /api/tasks/{id}/    → Delete task  
GET     /api/history/       → View change history  
🧩 Project Structure
graphql
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

🎥 Optional Demo Video
Place your walkthrough video in /demo/ folder and embed below:

html
Copy
Edit
<video controls width="100%">
  <source src="demo/taskie_demo.mp4" type="video/mp4">
</video>
🧾 License
MIT License © Laiba Muzammal

