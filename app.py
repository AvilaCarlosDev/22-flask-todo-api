"""
Flask Todo API - Lista de Tareas Interactiva con Python y Flask
API RESTful para gestionar una lista de tareas (todos)
"""
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory todo list
todos = [
    {"done": False, "label": "Sample Todo 1"},
    {"done": True, "label": "Sample Todo 2"},
]

@app.route('/')
def index():
    return jsonify({"message": "Todo API is running!", "endpoints": {
        "GET /todos": "Get all todos",
        "POST /todos": "Add a new todo",
        "DELETE /todos/<int:position>": "Delete a todo by position"
    }})

@app.route('/todos', methods=['GET'])
def get_todos():
    """Return the list of all todos"""
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    """Add a new todo to the list"""
    body = request.get_json()
    if not body or 'label' not in body:
        return jsonify({"error": "Missing 'label' field"}), 400
    
    new_todo = {
        "done": body.get("done", False),
        "label": body["label"]
    }
    todos.append(new_todo)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    """Delete a todo by its position in the list"""
    if position < 0 or position >= len(todos):
        return jsonify({"error": f"Position {position} is out of range"}), 400
    
    todos.pop(position)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['PUT'])
def update_todo(position):
    """Update a todo at the given position"""
    if position < 0 or position >= len(todos):
        return jsonify({"error": f"Position {position} is out of range"}), 400
    
    body = request.get_json()
    if 'done' in body:
        todos[position]['done'] = body['done']
    if 'label' in body:
        todos[position]['label'] = body['label']
    
    return jsonify(todos[position]), 200

if __name__ == '__main__':
    app.run(debug=True, port=3000)
