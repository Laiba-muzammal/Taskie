# Taskie

````markdown
<h1 align="center">🧠 Taskie - Smart Task Manager</h1>

<p align="center">
  A beautiful, Dockerized Django-based task management system with full task lifecycle, history tracking, Swagger API support, and user authentication.
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Status-Production-green" alt="status"/>
  <img src="https://img.shields.io/badge/Django-4.x-green" alt="django"/>
  <img src="https://img.shields.io/badge/Docker-Enabled-blue" alt="docker"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="license"/>
</div>

---

## 📸 Screenshots

> (Insert screenshots of your UI and Swagger if available)

---

## ⚙️ Features

- 👤 **Authentication** (Sign up / Login / Logout)
- 📋 **Task CRUD** (Create / Edit / Delete)
- 🔁 **Dependencies** (Link tasks together)
- 🔄 **Task Statuses** (Pending / In Progress / Completed)
- 🕓 **Task History Log** (View what was updated/deleted/created)
- 🔍 **Search Task History**
- 🌐 **Swagger UI** – auto-documented API
- 🐳 **Fully Dockerized Setup**

---

## 🧰 Tech Stack

| Tech | Purpose |
|------|---------|
| **Django** | Core backend logic |
| **Django REST Framework** | API creation |
| **SQLite** | Dev DB (can switch to PostgreSQL easily) |
| **Swagger (drf-yasg)** | Auto-generated API docs |
| **Docker + Docker Compose** | Environment setup |

---

## 🐳 Run Locally with Docker

### 📦 Requirements
- Docker & Docker Compose installed

### 🧪 Quick Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/taskie.git
cd taskie

# Build and run containers
docker-compose up --build
````

🔗 Visit:

* App: [http://localhost:8000](http://localhost:8000)
* Swagger Docs: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---

## 📂 Project Structure

```bash
├── tasks/               # App containing models, views, etc.
├── templates/           # HTML templates
├── static/              # CSS / JS / Assets
├── api/                 # DRF views + serializers
├── Dockerfile           # Docker image build config
├── docker-compose.yml   # Container orchestration
├── requirements.txt     # Python dependencies
└── README.md            # You're here!
```

---

## 💡 API Preview (via Swagger)

You can explore API endpoints for:

* GET, POST, PUT, DELETE tasks
* View history
* Create users

➡️ Just visit `/api/docs/`

---

## 🛠️ Still Improving...

* [ ] Admin Panel polish
* [ ] Email reminders for due tasks
* [ ] Role-based access control (maybe 👀)

---

## 🤝 Contributing

Found a bug or want to suggest a feature?
PRs are welcome. Fork the repo, make changes, and submit!

---

## 🧾 License

MIT License © [Laiba Muzammal](https://github.com/Laiba-muzammal)

---

> Built for personal productivity, resume strength & growth 🚀

