import pycountry
from datetime import datetime
from models.base_model import BaseModel


class Country(BaseModel):
    """
    A class representing a country.

    Attributes:
        id (str): The unique identifier for the country.
        _name (str): The name of the country.
        _code (str): The ISO 3166-1 alpha-2 code of the country.
        created_at (datetime): The date and time when the country
        record was created.
        updated_at (datetime): The date and time when the country
        record was last updated.

    Methods:
        __init__(name, code=None):
            Initializes a Country object with the given name and
            optionally the code.

        get_country_code(country_name):
            Retrieves the ISO 3166-1 alpha-2 code for the given country
            name using pycountry.

        from_dict(data, data_manager):
            Creates a Country object from a dictionary representation of
            its data.

        name:
            Property that gets the name of the country.

        name.setter:
            Setter method for updating the name of the country.

        code:
            Property that gets the ISO 3166-1 alpha-2 code of the country.

        code.setter:
            Setter method for updating the ISO 3166-1 alpha-2 code of the
            country.

        to_dict():
            Returns a dictionary representation of the country object.

    Raises:
        ValueError: If the provided name is empty or an invalid country name
        is used in get_country_code().
    """

    def __init__(self, name, code=None):
        """
        Initializes a Country object with the given name and optionally the
        code.

        Args:
            name (str): The name of the country.
            code (str, optional): The ISO 3166-1 alpha-2 code of the country.
            Defaults to None.

        Raises:
            ValueError: If the provided name is empty or an invalid country
            name is used in get_country_code().
        """
        super().__init__()

        if not name:
            raise ValueError("Name is required!")
        self._name = name
        self._code = code if code else self.get_country_code(name)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def get_country_code(self, country_name):
        """
        Retrieves the ISO 3166-1 alpha-2 code for the given country name using
        pycountry.

        Args:
            country_name (str): The name of the country.

        Returns:
            str: The ISO 3166-1 alpha-2 code of the country.

        Raises:
            ValueError: If an invalid country name is provided.
        """
        country = pycountry.countries.get(name=country_name)

        if country:
            return country.alpha_2
        raise ValueError("Invalid country name!")

    @staticmethod
    def from_dict(data, data_manager):
        """
        Creates a Country object from a dictionary representation of its
        data.

        Args:
            data (dict): A dictionary containing the country data.
            data_manager: Additional data manager or context if needed.

        Returns:
            Country: A Country object created from the provided dictionary
            data.
        """
        country = Country(
            name=data['name'],
            code=data.get('code', None)
        )
        country.id = data['country_id']
        country.created_at = datetime.fromisoformat(data['created_at'])
        country.updated_at = datetime.fromisoformat(data['updated_at'])
        return country

    @property
    def name(self):
        """
        Property that gets the name of the country.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter method for updating the name of the country.

        Args:
            value (str): The new name of the country.

        Raises:
            ValueError: If the provided name is empty.
        """
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
        self.updated_at = datetime.now()

    @property
    def code(self):
        """ Property that gets the ISO 3166-1 alpha-2 code of the country."""
        return self._code

    @code.setter
    def code(self, value):
        """
        Setter method for updating the ISO 3166-1 alpha-2 code of the
        country.

        Args:
            value (str): The new ISO 3166-1 alpha-2 code of the country.

        Raises:
            ValueError: If the provided code is empty.
        """
        if not value:
            raise ValueError("Code cannot be empty")
        self._code = value
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the country object.

        Returns:
            dict: A dictionary containing all attributes of the country
            object.
        """
        return {
            "country_id": self.id,
            "name": self._name,
            "code": self._code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
