from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__(*args, **kwargs)
        self.name = name

