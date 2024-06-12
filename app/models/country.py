import uuid
from datetime import datetime

class Country:
    def __init__(self, name, code):
        if not name:
            raise ValueError("Name is required!")
        if not code:
            raise ValueError("Code is required!")
        self.id = str(uuid.uuid4())
        self._name = name
        self._code = code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.updated_at = datetime.now()

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "country_id": self.id,
            "country_name": self.name,
            "country_code": self.code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def save(self):
        self.updated_at = datetime.now()