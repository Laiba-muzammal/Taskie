# Taskie

<h1 align="center">🧠 Taskie - Smart Task Manager</h1>

<p align="center">
  A beautiful, Dockerized Django-based task management system with full task lifecycle, history tracking, Swagger API support, and user authentication.
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Status-Production-green" alt="status"/>
# 🧠 Taskie – Smart Task Manager

A clean, full-featured task management system built with Django and Docker. Taskie helps users manage their daily tasks with full CRUD support, task history tracking, and a beautiful UI – now with Swagger-based API documentation!

---

## ✨ Key Features

- 🔐 User Authentication (Signup/Login)
- 📋 Task CRUD (Create, Read, Update, Delete)
- ⛓ Task Dependencies
- 🔄 Statuses: Pending | In Progress | Completed
- 🕓 Task History Log (Created / Updated / Deleted)
- 🌐 Swagger UI (API Docs via `drf-yasg`)
- 🐳 Dockerized Environment

---

## 🖼️ UI Preview

> Add your screenshots in a `screenshots/` folder and use the format below.

<table>
  <tr>
    <td><img src="screenshots/dashboard.png" width="100%"></td>
    <td><img src="screenshots/history.png" width="100%"></td>
  </tr>
  <tr>
    <td align="center">Dashboard View</td>
    <td align="center">Task History</td>
  </tr>
</table>

---

## 🛠 Tech Stack

- **Backend**: Django 4.x, Django REST Framework
- **Database**: SQLite (default) — can switch to PostgreSQL
- **Frontend**: HTML, Bootstrap 5
- **Docs**: Swagger (via drf-yasg)
- **Containerization**: Docker + Docker Compose

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Laiba-muzammal/taskie.git
cd taskie
2. Run with Docker
bash
Copy
Edit
docker-compose up --build
Visit:

🌐 App: http://localhost:8000

📘 Docs: http://localhost:8000/api/docs/

🔌 API Access
Explore RESTful endpoints like:

GET /api/tasks/

POST /api/tasks/

PUT /api/tasks/{id}/

DELETE /api/tasks/{id}/

Go to /api/docs/ for full interactive Swagger UI.

📁 Project Layout
graphql
Copy
Edit
taskie/
│
├── tasks/              # Core app with models/views
├── api/                # DRF views and serializers
├── templates/          # HTML pages
├── static/             # CSS / assets
├── Dockerfile
├── docker-compose.yml
└── README.md
📸 Assets
Add dashboard.png, history.png in screenshots/ folder

(Optional) Add a demo walkthrough video in /demo/ and embed it:

html
Copy
Edit
<!-- Inside README.md if GitHub supports video in your case -->
<video controls width="100%">
  <source src="demo/taskie_demo.mp4" type="video/mp4">
</video>

📄 License
MIT License © Laiba Muzammal

Built with 💙 for learning, growth, and resume building. 
