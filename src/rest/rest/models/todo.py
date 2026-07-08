import mongoengine
from datetime import datetime

#todo model
class TodoModel(mongoengine.Document):
    task_name = mongoengine.StringField(required=True)
    created_at = mongoengine.DateTimeField(default=datetime.now)
    updated_at = mongoengine.DateTimeField(default=datetime.now)
    deleted_at = mongoengine.DateTimeField(default=None)