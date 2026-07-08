import os
from pymongo import MongoClient
from rest.models.todo import TodoModel
import logging

class TodoRepository:
    def __init__(self):
        # Initialize the mongo client
        try:
            self.mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
            self.db = MongoClient(self.mongo_uri)['test_db']
        except Exception as e:
            logging.error(f"Error initializing todo repository: {e}")
            raise e
            
    def get_all_todos(self):
        # Get all todos
        try:
            # Find all todos that are not deleted
            docs = self.db.todo.find({"deleted_at": None})
            todos = []
            for doc in docs:
                todo = TodoModel(
                    id=doc.get("_id"),
                    task_name=doc.get("task_name"),
                    created_at=doc.get("created_at"),
                    updated_at=doc.get("updated_at"),
                    deleted_at=doc.get("deleted_at")
                )
                todos.append(todo)
            return todos
        except Exception as e:
            logging.error(f"Error getting all todos: {e}")
            return None

    def create_todo(self, todo: TodoModel):
        # Insert the todo into the database
        try:
            # Convert to dict format
            doc = todo.to_mongo()
            # If _id key exists and is None, delete it to let Mongo autogenerate a unique ObjectId
            if '_id' in doc and doc['_id'] is None:
                del doc['_id']
            self.db.todo.insert_one(doc)
            # Return true if the todo is created successfully
            return True
        except Exception as e:
            logging.error(f"Error inserting todo: {e}")
            return False