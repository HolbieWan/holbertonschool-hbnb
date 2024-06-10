from app.models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "state_id": self.country_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }