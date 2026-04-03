from flask import Flask
from todo import TodoList

app = Flask(__name__)
todo_list = TodoList()

@app.route("/")
def home() -> str:
    return "Todo app is running"

@app.route("/todos")
def todos() -> str:
    return str(todo_list.show_todos())

app.run()