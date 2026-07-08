import jsonschema
import logging
from rest.models.todo import TodoModel
from datetime import datetime

#todo request schema
todo_request_schema = {
    "type": "object",
    "properties": {
        "task_name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 250
        }
    },
    "required": ["task_name"]
}

def validate_todo_request(request: dict) -> bool:
    try:
        # Validate against jsonschema
        jsonschema.validate(request, todo_request_schema)
        return True
        # Return true if validation is successful
    except Exception as e:
        logging.error(f"Error validating todo request: {e}")
        return False

def to_todo_model(request: dict) -> TodoModel:
    # Convert the request to a todo model
    return TodoModel(
        task_name=request["task_name"],
        created_at=datetime.now(),
        updated_at=datetime.now(),
        deleted_at=None,
    )
