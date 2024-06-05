import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now() 
        self.updated_at = datetime.now()

    def save(self):# a tester avec created_at ou saved_at
        self.created_at = datetime.now()
        # Logic to save the object to the persistence layer

    def update(self):
        self.updated_at = datetime.now()