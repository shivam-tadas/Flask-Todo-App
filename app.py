from flask import Flask, request, jsonify, Response
from todo import TodoList

app = Flask(__name__)
todo_list = TodoList()

@app.route("/")
def home() -> Response:
    return jsonify({"message": "Todos app is running"})

@app.route("/todos")
def todos() -> Response:
    rows = todo_list.show_todos()
    todos = [{"id": row[0], "task": row[1]} for row in rows]
    return jsonify(todos)

@app.route("/add")
def add() -> Response:
    task = request.args.get("task")
    if task is None:
        return jsonify({"error": "task parameter is required"})
    todo_list.add_todo(task)
    return jsonify({"message": "Task added"})

@app.route("/delete")
def delete() -> Response:
    id_str = request.args.get("id")
    if id_str is None:
        return jsonify({"error": "task parameter is required"})
    try:
        task_id = int(id_str)
    except ValueError:
        return jsonify({"error": "id must be a number"})
    if todo_list.mark_todo_as_done(task_id):
        return jsonify({"message": "Task deleted"})
    return jsonify({"message": "Task not found"})

app.run()