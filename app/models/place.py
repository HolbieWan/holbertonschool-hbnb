from models.base_model import BaseModel
from datetime import datetime


class Place(BaseModel):
    """
    Place model representing a rental property.

    Attributes:
        name (str): Name of the place.
        description (str): Description of the place.
        address (str): Address of the place.
        city_id (str): ID of the city where the place is located.
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        host_id (str): ID of the host.
        num_rooms (int): Number of rooms in the place.
        num_bathrooms (int): Number of bathrooms in the place.
        price_per_night (float): Price per night for renting the place.
        max_guests (int): Maximum number of guests that can stay.
        amenities (list): List of amenities available at the place.
        data_manager (DataManager): Instance to manage data persistence.

    Methods:
        from_dict(data, data_manager): Creates a Place instance from a
        dictionary.
        to_dict(): Converts the Place instance to a dictionary.
        add_amenity(amenity_id): Adds an amenity to the place.
        remove_amenity(amenity_id): Removes an amenity from the place.
    """

    def __init__(self, name, description, address, city_id, latitude,
                 longitude, host_id, num_rooms, num_bathrooms,
                 price_per_night, max_guests, amenities=None,
                 data_manager=None):
        """
        Initializes a new Place instance.

        Args:
            name (str): Name of the place.
            description (str): Description of the place.
            address (str): Address of the place.
            city_id (str): ID of the city where the place is located.
            latitude (float): Latitude of the place.
            longitude (float): Longitude of the place.
            host_id (str): ID of the host.
            num_rooms (int): Number of rooms in the place.
            num_bathrooms (int): Number of bathrooms in the place.
            price_per_night (float): Price per night for renting the place.
            max_guests (int): Maximum number of guests that can stay.
            amenities (list, optional): List of amenities available at the
            place. Defaults to None.
            data_manager (DataManager, optional): The data manager instance
            for data persistence. Defaults to None.

        Raises:
            ValueError: If any field is missing or has invalid values.
        """
        super().__init__()

        if not all([name, description, address, city_id, latitude,
                    longitude, host_id, num_rooms, num_bathrooms,
                    price_per_night, max_guests]):
            raise ValueError("All fields are required!")
        if not -90 <= latitude <= 90:
            raise ValueError("Latitude must be between -90 and 90 degrees")
        if not -180 <= longitude <= 180:
            raise ValueError("Longitude must be between -180 and 180 degrees")
        if not 0 <= num_rooms <= 100:
            raise ValueError(
                "Number of rooms must be a positive integer" +
                "between 0 and 100")
        if not 0 <= num_bathrooms <= 100:
            raise ValueError(
                "Number of bathrooms must be a positive integer" +
                "between 0 and 100")
        if not 0 <= price_per_night <= 10000:
            raise ValueError(
                "Price per night must be a positive value" +
                " between 0 and 10000")
        if not 1 <= max_guests <= 100:
            raise ValueError(
                "Max guests must be a positive integer between 1 and 100")
        if data_manager and \
                data_manager.place_exists_with_attributes(name, address,
                                                          city_id,
                                                          host_id,
                                                          num_rooms,
                                                          num_bathrooms,
                                                          price_per_night,
                                                          max_guests):
            raise ValueError("Place already exists!")

        self._name = name
        self._description = description
        self._address = address
        self._city_id = city_id
        self._latitude = latitude
        self._longitude = longitude
        self._host_id = host_id
        self._num_rooms = num_rooms
        self._num_bathrooms = num_bathrooms
        self._price_per_night = price_per_night
        self._max_guests = max_guests
        self._amenities = amenities or []
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        """
        Creates a Place instance from a dictionary.

        Args:
            data (dict): The dictionary containing place data.
            data_manager (DataManager): The data manager instance for
            data persistence.

        Returns:
            Place: A new Place instance.
        """
        place = Place(
            name=data['place_name'],
            description=data['description'],
            address=data['address'],
            city_id=data['city_id'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            host_id=data['host_id'],
            num_rooms=data['num_rooms'],
            num_bathrooms=data['num_bathrooms'],
            price_per_night=data['price_per_night'],
            max_guests=data['max_guests'],
            amenities=data.get('amenities', []),
            data_manager=data_manager
        )
        place.id = data['place_id']
        place.created_at = datetime.fromisoformat(data['created_at'])
        place.updated_at = datetime.fromisoformat(data['updated_at'])
        return place

    @property
    def name(self):
        """str: Gets the name of the place."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the place and updates the updated_at timestamp.

        Args:
            value (str): The new name of the place.
        """
        self._name = value
        self.save()

    @property
    def description(self):
        """str: Gets the description of the place."""
        return self._description

    @description.setter
    def description(self, value):
        """
        Sets the description of the place and updates the updated_at timestamp.

        Args:
            value (str): The new description of the place.
        """
        self._description = value
        self.save()

    @property
    def address(self):
        """str: Gets the address of the place."""
        return self._address

    @address.setter
    def address(self, value):
        """
        Sets the address of the place and updates the updated_at timestamp.

        Args:
            value (str): The new address of the place.
        """
        self._address = value
        self.save()

    @property
    def city_id(self):
        """str: Gets the city ID of the place."""
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        """
        Sets the city ID of the place and updates the updated_at timestamp.

        Args:
            value (str): The new city ID.
        """
        self._city_id = value
        self.save()

    @property
    def latitude(self):
        """float: Gets the latitude of the place."""
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        """
        Sets the latitude of the place and updates the updated_at timestamp.

        Args:
            value (float): The new latitude.

        Raises:
            ValueError: If the latitude is not between -90 and 90 degrees.
        """
        if not -90 <= value <= 90:
            raise ValueError("Latitude must be between -90 and 90 degrees")
        self._latitude = value
        self.save()

    @property
    def longitude(self):
        """float: Gets the longitude of the place."""
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        """
        Sets the longitude of the place and updates the updated_at timestamp.

        Args:
            value (float): The new longitude.

        Raises:
            ValueError: If the longitude is not between -180 and 180 degrees.
        """
        if not -180 <= value <= 180:
            raise ValueError("Longitude must be between -180 and 180 degrees")
        self._longitude = value
        self.save()

    @property
    def host_id(self):
        """str: Gets the host ID of the place."""
        return self._host_id

    @host_id.setter
    def host_id(self, value):
        """
        Sets the host ID and updates the updated_at timestamp.

        Args:
            value (str): The new host ID.
        """
        self._host_id = value
        self.save()

    @property
    def num_rooms(self):
        """int: Gets the number of rooms in the place."""
        return self._num_rooms

    @num_rooms.setter
    def num_rooms(self, value):
        """
        Sets the number of rooms in the place and updates the updated_at
        timestamp.

        Args:
            value (int): The new number of rooms.

        Raises:
            ValueError: If the number of rooms is not between 0 and 100.
        """
        if value < 0 or value > 100:
            raise ValueError(
                "Number of rooms must be a positive integer between" +
                "0 and 100")
        self._num_rooms = value
        self.save()

    @property
    def num_bathrooms(self):
        """ int: Gets the number of bathrooms in the place."""
        return self._num_bathrooms

    @num_bathrooms.setter
    def num_bathrooms(self, value):
        """
        Sets the number of bathrooms in the place.

        Args:
            value (int): The number of bathrooms to set.

        Raises:
            ValueError: If the value is not a positive integer between 0
            and 100.
        """
        if value < 0 or value > 100:
            raise ValueError(
                "Number of bathrooms must be a positive integer between 0" +
                "and 100")
        self._num_bathrooms = value
        self.save()

    @property
    def price_per_night(self):
        """float: Gets the price per night for the place."""
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        """
        Sets the price per night for staying at the place.

        Args:
            value (int): The price per night to set.

        Raises:
            ValueError: If the value is not a positive integer between 0
            and 10000.
        """
        if value < 0 or value > 10000:
            raise ValueError(
                "Price per night must be a positive integer between 0" +
                "and 10000")
        self._price_per_night = value
        self.save()

    @property
    def max_guests(self):
        """int: Gets the maximum number of guests that can stay."""
        return self._max_guests

    @max_guests.setter
    def max_guests(self, value):
        """
        Sets the maximum number of guests allowed in the place.

        Args:
            value (int): The maximum number of guests to set.

        Raises:
            ValueError: If the value is not a positive integer between
            1 and 100.
        """
        if value <= 0 or value > 100:
            raise ValueError(
                "Max guests must be a positive integer between 1" +
                "and 100")
        self._max_guests = value
        self.save()

    @property
    def amenities(self):
        """list: Gets the list of amenities available at the place."""
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        """
        Sets the list of amenities available at the place.

        Args:
            value (list): The list of amenities to set.
        """
        self._amenities = value
        self.save()

    def add_amenity(self, amenity_id):
        """
        Adds an amenity to the list of amenities available at the place.

        Args:
            amenity_id (int): The identifier of the amenity to add.
        """
        if amenity_id not in self._amenities:
            self._amenities.append(amenity_id)
            self.save()

    def remove_amenity(self, amenity_id):
        """
        Removes an amenity from the list of amenities available at the place.

        Args:
            amenity_id (int): The identifier of the amenity to remove.
        """
        if amenity_id in self._amenities:
            self._amenities.remove(amenity_id)
            self.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the place object.

        Returns:
            dict: A dictionary containing all attributes of the place object.
        """
        return {
            "place_id": self.id,
            "place_name": self._name,
            "description": self._description,
            "address": self._address,
            "city_id": self._city_id,
            "latitude": self._latitude,
            "longitude": self._longitude,
            "host_id": self._host_id,
            "num_rooms": self._num_rooms,
            "num_bathrooms": self._num_bathrooms,
            "price_per_night": self._price_per_night,
            "max_guests": self._max_guests,
            "amenities": self._amenities,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
