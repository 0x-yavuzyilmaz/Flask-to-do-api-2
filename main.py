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


@app.route('/')
def home():
    return "Todo API server is running"


if __name__ == '__main__':
    app.run(debug=True)
