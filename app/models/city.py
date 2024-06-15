from models.base_model import BaseModel
from datetime import datetime


class City(BaseModel):
    """
    A class representing a city.

    Attributes:
        id (str): The unique identifier for the city.
        _name (str): The name of the city.
        _country_id (str): The identifier of the country to which the city
        belongs.
        data_manager: Additional data manager or context if needed.

    Methods:
        __init__(name, country_id, data_manager):
            Initializes a City object with the given name, country ID,
            and data manager.

        from_dict(data, data_manager):
            Creates a City object from a dictionary representation of its
            data.

        name:
            Property that gets the name of the city.

        name.setter:
            Setter method for updating the name of the city.

        country_id:
            Property that gets the identifier of the country to which the
            city belongs.

        country_id.setter:
            Setter method for updating the country ID of the city.

        to_dict():
            Returns a dictionary representation of the city object.

    Raises:
        ValueError: If the city name is empty, the city name is not unique
        within the same country, or the country ID is not provided.
    """

    def __init__(self, name, country_id, data_manager):
        """
        Initializes a City object with the given name, country ID, and data
        manager.

        Args:
            name (str): The name of the city.
            country_id (str): The identifier of the country to which the city
            belongs.
            data_manager: Additional data manager or context if needed.

        Raises:
            ValueError: If the city name is empty, the city name is not unique
            within the same country, or the country ID is not provided.
        """
        super().__init__()

        if not name:
            raise ValueError("City name is required!")
        if data_manager.city_exists_with_name_and_country(name, country_id):
            raise ValueError(
                "City name must be unique within the same country")
        if not country_id:
            raise ValueError("Country ID is required!")
        self._name = name
        self._country_id = country_id
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        """
        Creates a City object from a dictionary representation of its data.

        Args:
            data (dict): A dictionary containing the city data.
            data_manager: Additional data manager or context if needed.

        Returns:
            City: A City object created from the provided dictionary data.
        """
        city = City(
            name=data['city_name'],
            country_id=data['country_id'],
            data_manager=data_manager
        )
        city.id = data['city_id']
        city.created_at = datetime.fromisoformat(data['created_at'])
        city.updated_at = datetime.fromisoformat(data['updated_at'])
        return city

    @property
    def name(self):
        """
        Property that gets the name of the city.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter method for updating the name of the city.

        Args:
            value (str): The new name of the city.
        """
        self._name = value
        self.save()

    @property
    def country_id(self):
        """
        Property that gets the identifier of the country to
        which the city belongs.
        """
        return self._country_id

    @country_id.setter
    def country_id(self, value):
        """
        Setter method for updating the country ID of the city.

        Args:
            value (str): The new country ID of the city.
        """
        self._country_id = value
        self.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the city object.

        Returns:
            dict: A dictionary containing all attributes of the city
            object.
        """
        return {
            "city_id": self.id,
            "city_name": self._name,
            "country_id": self._country_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
