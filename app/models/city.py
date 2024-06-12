from models.base_model import BaseModel


class City(BaseModel):
    def __init__(self, name, country_id):
        super().__init__()
        if not name:
            raise ValueError("Name is required!")
        if not country_id:
            raise ValueError("Country code is required!")
        self._name = name
        self._country_id = country_id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.save()

    @property
    def country_id(self):
        return self._country_id

    @country_id.setter
    def country_id(self, value):
        self._country_id = value
        self.save()

    def to_dict(self):
        return {
            "city_id": self.id,
            "city_name": self.name,
            "country_code": self.country_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
