from email_validator import validate_email, EmailNotValidError
from models.base_model import BaseModel
from persistence.data_manager import DataManager

class User(BaseModel):
    data_manager = DataManager()
    
    def __init__(self, email, first_name, last_name):
        super().__init__()

        if not email:
            raise ValueError("Email is required!")
        if not first_name:
            raise ValueError("First name is required!")
        if not last_name:
            raise ValueError("Last name is required!")
        if not self.is_valid_email_format(email):
            raise ValueError("Invalid email format!")
        if self.__class__.data_manager.get_by_email(email):
            raise ValueError("Email already exists!")
        self._email = email
        self._first_name = first_name
        self._last_name = last_name

    @property
    def email(self):
        return self._email

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

    @staticmethod
    def is_valid_email_format(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False
