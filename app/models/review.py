from models.base_model import BaseModel
from datetime import datetime


class Review(BaseModel):
    """
        Review model that represents a review for a place by a user.

        Attributes:
            place_id (str): The ID of the place being reviewed.
            user_id (str): The ID of the user who wrote the review.
            rating (int): The rating given by the user (between 1 and 5).
            text (str): The text of the review.
            data_manager (DataManager): Instance to manage data persistence.

        Methods:
            from_dict(data, data_manager): Creates a Review instance from a
            dictionary.
            to_dict(): Converts the Review instance to a dictionary.
    """

    def __init__(self, place_id, user_id, rating, text, data_manager=None):
        """
        Initializes a new Review instance.

        Args:
            place_id (str): The ID of the place being reviewed.
            user_id (str): The ID of the user who wrote the review.
            rating (int): The rating given by the user (between 1 and 5).
            text (str): The text of the review.
            data_manager (DataManager, optional): The data manager instance
            for data persistence.

        Raises:
            ValueError: If any field is missing, if the rating is not between
            1 and 5, or if a review already exists for this user and place.
        """
        super().__init__()

        if not all([place_id, user_id, rating, text]):
            raise ValueError("All fields are required!")
        rating = int(rating)
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        if data_manager and \
                data_manager.review_exists_with_attributes(place_id, user_id):
            raise ValueError("Review already exists for this user and place")
        self._place_id = place_id
        self._user_id = user_id
        self._rating = rating
        self._text = text
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        """
        Creates a Review instance from a dictionary.

        Args:
            data (dict): The dictionary containing review data.
            data_manager (DataManager): The data manager instance for data
            persistence.

        Returns:
            Review: A new Review instance.

        Raises:
            ValueError: If the rating is not an integer between 1 and 5.
        """
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
        """ Gets the ID of the place being reviewed."""
        return self._place_id

    @property
    def user_id(self):
        """ Gets the ID of the user who wrote the review."""
        return self._user_id

    @property
    def rating(self):
        """ Gets the rating given by the user."""
        return self._rating

    @rating.setter
    def rating(self, value):
        """
        Sets the rating and updates the updated_at timestamp.

        Args:
            value (int): The new rating.

        Raises:
            ValueError: If the rating is not between 1 and 5.
        """
        value = int(value)
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value
        self.updated_at = datetime.now()
        self.save()

    @property
    def text(self):
        """ Gets the text of the review."""
        return self._text

    @text.setter
    def text(self, value):
        """
        Sets the text of the review and updates the updated_at timestamp.

        Args:
            value (str): The new text of the review.

        Raises:
            ValueError: If the text is empty.
        """
        if not value:
            raise ValueError("Text cannot be empty")
        self._text = value
        self.updated_at = datetime.now()
        self.save()

    def to_dict(self):
        """
        Converts the Review instance to a dictionary.

        Returns:
            dict: The dictionary representation of the Review instance.
        """
        return {
            "review_id": self.id,
            "place_id": self._place_id,
            "user_id": self._user_id,
            "rating": self._rating,
            "text": self._text,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
