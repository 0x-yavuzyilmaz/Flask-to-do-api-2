from flask import Flask, jsonify, abort, request

app = Flask(__name__)

# sahte veritabanı
todos = [
    {"id": 1, "task": "Build a REST API", "done": True},
    {"id": 2, "task": "Create a GET endpoint", "done": False}
]


@app.route('/api/todos')
def get_all_todos():
    return jsonify(todos)


@app.route('/api/todos/<int:todo_id>')
def get_single_todo(todo_id):
    found_todo = [todo for todo in todos if todo["id"] == todo_id]
    if len(found_todo) == 0:
        abort(404)
    return jsonify(found_todo[0])


@app.route('/api/todos', methods=['POST'])
def create_todo():
    if not request.json or not 'task' in request.json:
        abort(400)
    new_id = todos[-1]['id'] + 1 if todos else 1

    new_todo = {"id": new_id, "task": request.json['task'], 'done': False}
    todos.append(new_todo)
    return jsonify(new_todo), 201


@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    found_todo = [todo for todo in todos if todo["id"] == todo_id]
    if len(found_todo) == 0:
        abort(404)
    if not request.json:
        abort(400, description="Invalid data: a JSON body is required.")
    if 'task' not in request.json:
        abort(400, description="Invalid data: 'task' and 'done' fields are required.")
    if not 'done' in request.json:
        abort(400, description="Invalid data: 'done' field must be a boolean (true/false).")

    todo_to_update = found_todo[0]
    todo_to_update['task'] = request.json['task']
    todo_to_update['done'] = request.json['done']

    return jsonify(todo_to_update), 200

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    found_todo = [todo for todo in todos if todo["id"] == todo_id]
    if len(found_todo) == 0:
        abort(404)
    todos.remove(found_todo[0])
    return jsonify({'result': True, 'message': 'Todo deleted successfully'}), 200


@app.route('/')
def home():
    return "Todo API server is running"


if __name__ == '__main__':
    app.run(debug=True)
