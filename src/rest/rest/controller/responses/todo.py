from __future__ import annotations
from rest.models.todo import TodoModel

def to_todo_response(todos: list[TodoModel]) -> list[dict]:
    # Convert the todos to response
    return [{"id": str(todo.id), "task_name": todo.task_name} for todo in todos]