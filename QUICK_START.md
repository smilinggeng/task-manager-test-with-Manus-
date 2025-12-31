# Quick Start Guide

This guide will help you get started with the Task Manager application and understand the workflow.

## Prerequisites

Before you begin, make sure you have the following installed on your computer:

1. **VSCode**: Download from [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. **Git**: Download from [https://git-scm.com/](https://git-scm.com/)
3. **Docker Desktop**: Download from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
4. **Python 3.11+** (optional, only needed for local development without Docker)

## Step 1: Extract and Open the Project

1. Extract the `task-manager.zip` file to a location on your computer
2. Open VSCode
3. Click **File → Open Folder** and select the `task-manager` folder

## Step 2: Explore the Code in VSCode

Take some time to explore the project structure in VSCode:

### Front-End Files (`frontend/` directory)
- **`index.html`**: The main HTML structure of the web page
- **`style.css`**: All the styling that makes the page look good
- **`app.js`**: JavaScript code that handles user interactions and API calls

### Back-End Files (`backend/` directory)
- **`app.py`**: The Flask server that provides the REST API
- **`database.py`**: Functions to interact with the SQLite database
- **`requirements.txt`**: List of Python packages needed

### Docker Files (root directory)
- **`Dockerfile.backend`**: Instructions to build the backend container
- **`Dockerfile.frontend`**: Instructions to build the frontend container
- **`docker-compose.yml`**: Orchestrates both containers together
- **`nginx.conf`**: Configuration for the Nginx web server

## Step 3: Run the Application with Docker

This is the easiest way to run the complete application:

1. Open a terminal in VSCode (**Terminal → New Terminal**)
2. Make sure Docker Desktop is running
3. Run the following command:

```bash
docker-compose up --build
```

4. Wait for the containers to build and start (this may take a few minutes the first time)
5. Open your browser and go to: **http://localhost:8080**

You should see the Task Manager application! Try adding, completing, and deleting tasks.

## Step 4: Initialize Git and Push to GitHub

Now let's put your project under version control:

### Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit of task manager application"
```

### Create a GitHub Repository

1. Go to [https://github.com](https://github.com) and sign in
2. Click the **+** icon in the top right and select **New repository**
3. Name it `task-manager`
4. **Do NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **Create repository**

### Push to GitHub

GitHub will show you commands to run. They'll look like this:

```bash
git remote add origin https://github.com/YOUR-USERNAME/task-manager.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your actual GitHub username.

## Step 5: Make Changes and See the Workflow

Now let's make a change to see the complete workflow:

### 1. Make a Code Change

Open `frontend/index.html` in VSCode and change the title:

```html
<h1>📝 My Awesome Task Manager</h1>
```

### 2. Test Locally

If Docker is still running, you can just refresh your browser. Docker Compose is configured to reflect changes immediately for the backend. For frontend changes, you may need to restart:

```bash
# Press Ctrl+C to stop
docker-compose up
```

### 3. Commit and Push

```bash
git add .
git commit -m "Updated application title"
git push
```

Now your changes are saved on GitHub!

## Understanding the Workflow

Here's what you've just learned:

1. **IDE (VSCode)**: You write and edit your code here. VSCode provides syntax highlighting, code completion, and integrated terminal.

2. **GitHub**: Every time you commit and push, you create a snapshot of your project. You can always go back to previous versions if something breaks.

3. **Docker**: Your application runs in containers, which means it will work the same way on any computer that has Docker installed. No more "it works on my machine" problems!

## Running Without Docker (Optional)

If you want to run the application without Docker:

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

The backend will run on http://localhost:5000

### Frontend

```bash
cd frontend
python -m http.server 8080
```

The frontend will run on http://localhost:8080

## Troubleshooting

### Docker containers won't start
- Make sure Docker Desktop is running
- Try `docker-compose down` then `docker-compose up --build`

### Can't connect to the backend
- Check that the backend container is running: `docker ps`
- Check the backend logs: `docker-compose logs backend`

### Port already in use
- Another application might be using port 8080 or 5000
- Change the port in `docker-compose.yml` (e.g., `"8081:80"` instead of `"8080:80"`)

## Next Steps

Now that you understand the basics, you can:

1. **Add new features** to the application (e.g., task priorities, due dates)
2. **Improve the styling** with better CSS
3. **Learn about branches** in Git for feature development
4. **Deploy** your application to a cloud service like AWS, Azure, or Heroku

Happy coding!
