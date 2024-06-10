from .base_model import BaseModel
from datetime import datetime

class Review(BaseModel):
    def __init__(self, place_id, user_id, rating, text):
        super().__init__()
        self._place_id = place_id
        self._user_id = user_id
        self._rating = rating
        self._text = text

    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
        self.updated_at = datetime.now()

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
        self.updated_at = datetime.now()

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
        self.updated_at = datetime.now()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.updated_at = datetime.now()

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
