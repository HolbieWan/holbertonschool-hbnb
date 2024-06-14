import pycountry
from datetime import datetime
from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, code=None):
        super().__init__()
        if not name:
            raise ValueError("Name is required!")
        self._name = name
        self._code = code if code else self.get_country_code(name)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_country_code(self, country_name):
        try:
            country = pycountry.countries.get(name=country_name)
            if country:
                return country.alpha_2
        except LookupError:
            raise ValueError("Invalid country name!")
        return None

    @staticmethod
    def from_dict(data, data_manager):
        country = Country(
            name=data['name'],
            code=data.get('code', None)
        )
        country.id = data['country_id']
        country.created_at = datetime.fromisoformat(data['created_at'])
        country.updated_at = datetime.fromisoformat(data['updated_at'])
        return country

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @code.setter
    def code(self, value):
        if not value:
            raise ValueError("Code cannot be empty")
        self._code = value

    def to_dict(self):
        return {
            "country_id": self.id,
            "name": self._name,
            "code": self._code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
