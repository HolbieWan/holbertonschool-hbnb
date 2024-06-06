from .base_model import BaseModel


class City(BaseModel):
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_country_id(self):
        return self.country_id

    def set_country_id(self, country_id):
        self.country_id = country_id
