import sqlite3
import os

# Database file path
DB_PATH = os.path.join(os.path.dirname(__file__), 'tasks.db')

def init_db():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def get_connection():
    """Get a database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

def get_all_tasks():
    """Get all tasks from the database"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
    tasks = cursor.fetchall()
    conn.close()
    
    # Convert to list of dictionaries
    return [dict(task) for task in tasks]

def create_task(title):
    """Create a new task"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (title, False))
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return task_id

def toggle_task(task_id):
    """Toggle the completion status of a task"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = NOT completed WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    """Delete a task"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
