from .base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
