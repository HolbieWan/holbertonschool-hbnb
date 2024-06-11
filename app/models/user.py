from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()
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
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
