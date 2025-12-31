from flask import Flask, jsonify, request
from flask_cors import CORS
import database

# Create Flask app
app = Flask(__name__)

# Enable CORS so frontend can communicate with backend
CORS(app)

# Initialize database when app starts
database.init_db()

@app.route('/')
def home():
    """Home endpoint to check if API is running"""
    return jsonify({
        'message': 'Task Manager API is running!',
        'version': '1.0',
        'endpoints': {
            'GET /api/tasks': 'Get all tasks',
            'POST /api/tasks': 'Create a new task',
            'PUT /api/tasks/<id>/toggle': 'Toggle task completion',
            'DELETE /api/tasks/<id>': 'Delete a task'
        }
    })

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    tasks = database.get_all_tasks()
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    
    title = data['title'].strip()
    if not title:
        return jsonify({'error': 'Title cannot be empty'}), 400
    
    task_id = database.create_task(title)
    return jsonify({'id': task_id, 'message': 'Task created successfully'}), 201

@app.route('/api/tasks/<int:task_id>/toggle', methods=['PUT'])
def toggle_task(task_id):
    """Toggle task completion status"""
    database.toggle_task(task_id)
    return jsonify({'message': 'Task updated successfully'})

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    database.delete_task(task_id)
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
