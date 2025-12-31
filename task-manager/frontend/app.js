// API endpoint - change this based on your environment
const API_URL = 'http://localhost:5000/api';

// Load tasks when page loads
document.addEventListener('DOMContentLoaded', () => {
    loadTasks();
});

// Load all tasks from the backend
async function loadTasks() {
    try {
        const response = await fetch(`${API_URL}/tasks`);
        const tasks = await response.json();
        
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = '';
        
        if (tasks.length === 0) {
            taskList.innerHTML = '<div class="empty-state">No tasks yet. Add one above!</div>';
            return;
        }
        
        tasks.forEach(task => {
            const taskElement = createTaskElement(task);
            taskList.appendChild(taskElement);
        });
    } catch (error) {
        console.error('Error loading tasks:', error);
        alert('Failed to load tasks. Make sure the backend is running!');
    }
}

// Create a task element
function createTaskElement(task) {
    const li = document.createElement('li');
    li.className = `task-item ${task.completed ? 'completed' : ''}`;
    
    li.innerHTML = `
        <span class="task-text">${task.title}</span>
        <div class="task-actions">
            <button class="complete-btn" onclick="toggleTask(${task.id})">
                ${task.completed ? 'Undo' : 'Complete'}
            </button>
            <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
        </div>
    `;
    
    return li;
}

// Add a new task
async function addTask() {
    const input = document.getElementById('taskInput');
    const title = input.value.trim();
    
    if (!title) {
        alert('Please enter a task!');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title: title })
        });
        
        if (response.ok) {
            input.value = '';
            loadTasks();
        } else {
            alert('Failed to add task');
        }
    } catch (error) {
        console.error('Error adding task:', error);
        alert('Failed to add task. Make sure the backend is running!');
    }
}

// Toggle task completion status
async function toggleTask(id) {
    try {
        const response = await fetch(`${API_URL}/tasks/${id}/toggle`, {
            method: 'PUT'
        });
        
        if (response.ok) {
            loadTasks();
        } else {
            alert('Failed to update task');
        }
    } catch (error) {
        console.error('Error toggling task:', error);
        alert('Failed to update task');
    }
}

// Delete a task
async function deleteTask(id) {
    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/tasks/${id}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            loadTasks();
        } else {
            alert('Failed to delete task');
        }
    } catch (error) {
        console.error('Error deleting task:', error);
        alert('Failed to delete task');
    }
}

// Allow pressing Enter to add task
document.getElementById('taskInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addTask();
    }
});
