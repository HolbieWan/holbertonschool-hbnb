from models.base_model import BaseModel
from datetime import datetime

class Review(BaseModel):
    def __init__(self, place_id, user_id, rating, text, data_manager=None):
        super().__init__()
        if not all([place_id, user_id, rating, text]):
            raise ValueError("All fields are required!")
        rating = int(rating)
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        if data_manager and data_manager.review_exists_with_attributes(place_id, user_id):
            raise ValueError("Review already exists for this user and place")
        self._place_id = place_id
        self._user_id = user_id
        self._rating = rating
        self._text = text
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        try:
            rating = int(data['rating'])
        except (ValueError, TypeError):
            raise ValueError("Rating must be an integer between 1 and 5")
        
        review = Review(
            place_id=data['place_id'],
            user_id=data['user_id'],
            rating=rating,
            text=data['text'],
            data_manager=data_manager
        )
        review.id = data['review_id']
        review.created_at = datetime.fromisoformat(data['created_at'])
        review.updated_at = datetime.fromisoformat(data['updated_at'])
        return review

    @property
    def place_id(self):
        return self._place_id

    @property
    def user_id(self):
        return self._user_id

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        value = int(value)
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Text cannot be empty")
        self._text = value

    def to_dict(self):
        return {
            "review_id": self.id,
            "place_id": self._place_id,
            "user_id": self._user_id,
            "rating": self._rating,
            "text": self._text,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
