from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []
counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    global counter
    data = request.json
    task = {
        'id': counter,
        'title': data['title'],
        'completed': False
    }
    tasks.append(task)
    counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(debug=True)