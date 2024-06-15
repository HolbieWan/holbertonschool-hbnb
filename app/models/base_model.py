import uuid
from datetime import datetime


class BaseModel:
    """
    A base class representing a model with common attributes and methods.

    Attributes:
        id (str): The unique identifier for the model instance.
        created_at (datetime): The date and time when the model instance
        was created.
        updated_at (datetime): The date and time when the model instance
        was last updated.

    Methods:
        __init__():
            Initializes a BaseModel instance with a unique identifier,
            creation, and update timestamps.

        to_dict():
            Returns a dictionary representation of the BaseModel instance.

        save():
            Updates the 'updated_at' timestamp to the current date and time.
    """

    def __init__(self):
        """
        Initializes a BaseModel instance with a unique identifier, creation,
        and update timestamps.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary containing the 'id', 'created_at', and
            'updated_at' attributes.
        """
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    def save(self):
        """
        Updates the 'updated_at' timestamp to the current date and time.
        """
        self.updated_at = datetime.now()
