import uuid
from datetime import datetime

class Country:
    def __init__(self, name, code, data_manager):
        if not name:
            raise ValueError("Name is required!")
        if not code:
            raise ValueError("Code is required!")
        self.id = str(uuid.uuid4())
        self._name = name
        self._code = code
        self._data_manager = data_manager
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def from_dict(data, data_manager):
        country = Country(
            name=data['country_name'],
            code=data['country_code'],
            data_manager=data_manager
        )
        country.id = data['country_id']
        country.created_at = datetime.fromisoformat(data['created_at'])
        country.updated_at = datetime.fromisoformat(data['updated_at'])
        return country

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
            "country_name": self._name,
            "country_code": self._code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def save(self):
        self.updated_at = datetime.now()
