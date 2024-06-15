from email_validator import validate_email, EmailNotValidError
from models.base_model import BaseModel
from datetime import datetime


class User(BaseModel):
    """
        User model that represents a user with an email, first name,
        and last name.

        Attributes:
            email (str): User's email address.
            first_name (str): User's first name.
            last_name (str): User's last name.
            data_manager (DataManager): Instance to manage data
            persistence.

        Methods:
            from_dict(data, data_manager): Creates a User instance
            from a dictionary.
            is_valid_email_format(email): Validates the email format.
            to_dict(): Converts the User instance to a dictionary.
    """

    def __init__(self, email, first_name, last_name, data_manager):
        """
        Initializes a new User instance.

        Args:
            email (str): The user's email address.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            data_manager (DataManager): The data manager instance for
            data persistence.

        Raises:
            ValueError: If email is invalid, email already exists, or
            if first name or last name is missing.
        """
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
        """
        Creates a User instance from a dictionary.

        Args:
            data (dict): The dictionary containing user data.
            data_manager (DataManager): The data manager instance
            for data persistence.

        Returns:
            User: A new User instance.
        """
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
        """
        Validates the email format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False

    @property
    def email(self):
        """str: Gets the user's email address."""
        return self._email

    @property
    def first_name(self):
        """str: Gets the user's first name."""
        return self._first_name

    @property
    def last_name(self):
        """str: Gets the user's last name."""
        return self._last_name

    @first_name.setter
    def first_name(self, value):
        """
        Sets the user's first name and updates the updated_at timestamp.

        Args:
            value (str): The new first name.
        """
        self._first_name = value
        self.updated_at = datetime.now()
        self.save()

    @last_name.setter
    def last_name(self, value):
        """
        Sets the user's last name and updates the updated_at timestamp.

        Args:
            value (str): The new last name.
        """
        self._last_name = value
        self.updated_at = datetime.now()
        self.save()

    @email.setter
    def email(self, value):
        """
        Sets the user's email address and updates the updated_at timestamp.

        Args:
            value (str): The new email address.

        Raises:
            ValueError: If the email format is invalid.
        """
        if not self.is_valid_email_format(value):
            raise ValueError("Invalid email format!")
        self._email = value
        self.updated_at = datetime.now()
        self.save()

    def to_dict(self):
        """
        Converts the User instance to a dictionary.

        Returns:
            dict: The dictionary representation of the User instance.
        """
        return {
            "user_id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
