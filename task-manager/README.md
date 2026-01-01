# Task Manager Application

A simple full-stack task management application demonstrating the integration of IDE, GitHub, and Docker.

## Project Structure

```
task-manager/
├── frontend/              # Front-end files
│   ├── index.html        # Main HTML page
│   ├── style.css         # Styling
│   └── app.js            # JavaScript logic
├── backend/              # Back-end files
│   ├── app.py           # Flask API server
│   ├── database.py      # Database operations
│   └── requirements.txt # Python dependencies
├── Dockerfile.backend    # Docker configuration for backend
├── Dockerfile.frontend   # Docker configuration for frontend
├── docker-compose.yml   # Multi-container orchestration
├── nginx.conf           # Nginx web server configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Technologies Used

- **Front-end**: HTML, CSS, JavaScript
- **Back-end**: Python Flask
- **Database**: SQLite
- **Containerization**: Docker & Docker Compose
- **Web Server**: Nginx


## Running with Docker

1. Make sure Docker and Docker Compose are installed
2. Navigate to the project directory
3. Run: `docker-compose up --build`
4. Access the application at `http://localhost:8080`

## Running Locally (Without Docker)

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
Open `frontend/index.html` in your browser, or use a simple HTTP server:
```bash
cd frontend
python -m http.server 8080
```

## API Endpoints

- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/<id>/toggle` - Toggle task completion
- `DELETE /api/tasks/<id>` - Delete a task

## Features

- ✅ Add new tasks
- ✅ Mark tasks as complete
- ✅ Delete tasks
- ✅ Persistent storage with SQLite
- ✅ RESTful API design
- ✅ Containerized deployment


## Common Troubleshooting Issues - WIP

### Port Issue Resolution

When you first clone this repo into your own local environment, make sure that you modify two important files to change the ports from which you local task manager will run: 

- `docker-compose.yml` - change both `frontend` and `backend` ports (first four digits) to something other than 8000 (e.g. 8002, 6756, etc)
- `app.js` - change the API_URL to match the backend port you set