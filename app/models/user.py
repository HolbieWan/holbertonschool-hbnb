from email_validator import validate_email, EmailNotValidError
from models.base_model import BaseModel
from datetime import datetime

class User(BaseModel):
    def __init__(self, email, first_name, last_name, data_manager):
        super().__init__()
        if not email:
            raise ValueError("Email is required!")
        if not self.is_valid_email_format(email):
            raise ValueError("Invalid email format!")
        if data_manager.get_by_email(email):
            raise ValueError("Email already exists!")
        if not first_name:
            raise ValueError("First name is required!")
        if not last_name:
            raise ValueError("Last name is required!")
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

    @staticmethod
    def is_valid_email_format(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False

    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        self.updated_at = datetime.now()
        self.save()

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
        self.updated_at = datetime.now()
        self.save()

    @email.setter
    def email(self, value):
        if not self.is_valid_email_format(value):
            raise ValueError("Invalid email format!")
        self._email = value
        self.updated_at = datetime.now()
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
