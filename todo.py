import sqlite3

class TodoList:
    def __init__(self):
        self.conn = sqlite3.connect("todos.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, task TEXT)")
        
    def add_todo(self, todo: str) -> None:
        self.cursor.execute("INSERT INTO todos (task) VALUES (?)", (todo,))
        self.conn.commit()

    def mark_todo_as_done(self, task_id: int) -> None:
        self.cursor.execute("SELECT id FROM todos WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()
        if row is None:
            print("Task not found")
        else:
            self.cursor.execute("DELETE FROM todos WHERE id = ?", (task_id,))
            self.conn.commit()

    def show_todos(self) -> list:
        self.cursor.execute("SELECT * FROM todos")
        rows = self.cursor.fetchall()
        return rows