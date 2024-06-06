from .base_model import BaseModel


class Review(BaseModel):
    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review: {self.comment}"

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_place_id(self):
        return self.place_id

    def set_place_id(self, place_id):
        self.place_id = place_id

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating

    def get_comment(self):
        return self.comment

    def set_comment(self, comment):
        self.comment = comment
