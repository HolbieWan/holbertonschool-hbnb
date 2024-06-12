from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        if not name:
            raise ValueError("Name is required!")
        self._name = name


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, value):
        self._name = value
        self.save()


    def to_dict(self):
        return {
            "amenity_id": self.id,
            "amenity_name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
