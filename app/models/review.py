from .base_model import BaseModel

class Review(BaseModel):

    def __init__(self, place_id, user_id,rating, text):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.text = text

    def to_dict(self):
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "rating": self.rating,
            "text": self.text,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }