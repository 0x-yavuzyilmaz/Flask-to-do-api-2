from flask import Flask, jsonify

app = Flask(__name__)

# sahte veritabanı
todos = [
    {"id": 1, "task": "Build a REST API", "done": True},
    {"id": 2, "task": "Create a GET endpoint", "done": False}
]


@app.route('/api/todos')
def get_all_todos():
    return jsonify(todos)


@app.route('/')
def home():
    return "Todo API server is running"


if __name__ == '__main__':
    app.run(debug=True)
