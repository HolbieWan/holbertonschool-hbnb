from email_validator import validate_email, EmailNotValidError
from models.base_model import BaseModel
from datetime import datetime

class User(BaseModel):
    def __init__(self, email, first_name, last_name, data_manager):
        super().__init__()
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        user = User(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            data_manager=data_manager
        )
        user.id = data['user_id']
        user.created_at = datetime.fromisoformat(data['created_at'])
        user.updated_at = datetime.fromisoformat(data['updated_at'])
        return user

    @property
    def email(self):
        return self._email

    @staticmethod
    def is_valid_email_format(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False

    @email.setter
    def email(self, value):
        self._email = value
        self.save()

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        self.save()

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
        self.save()

    def to_dict(self):
        return {
            "user_id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
