from models.base_model import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    """
        A class representing an amenity.

        Attributes:
            id (str): The unique identifier for the amenity.
            _name (str): The name of the amenity.
            data_manager: Additional data manager or context if needed.
            created_at (datetime): The date and time when the amenity was
            created.
            updated_at (datetime): The date and time when the amenity was
            last updated.

        Methods:
            __init__(name, data_manager):
                Initializes an Amenity object with the given name and data
                manager.

        from_dict(data, data_manager):
            Creates an Amenity object from a dictionary representation of
            its data.

        name:
            Property that gets the name of the amenity.

        name.setter:
            Setter method for updating the name of the amenity.

        to_dict():
            Returns a dictionary representation of the amenity object.

        Raises:
            ValueError: If the amenity name is empty or the amenity with
            the same name already exists.
    """

    def __init__(self, name, data_manager):
        """
        Initializes an Amenity object with the given name and data manager.

        Args:
            name (str): The name of the amenity.
            data_manager: Additional data manager or context if needed.

        Raises:
            ValueError: If the amenity name is empty or the amenity with
            the same name already exists.
        """
        super().__init__()

        if not name:
            raise ValueError("Amenity name is required!")
        if data_manager.amenity_exists_with_name(name):
            raise ValueError("This amenity already exists!")
        self._name = name
        self.data_manager = data_manager

    @staticmethod
    def from_dict(data, data_manager):
        """
        Creates an Amenity object from a dictionary representation of its
        data.

        Args:
            data (dict): A dictionary containing the amenity data.
            data_manager: Additional data manager or context if needed.

        Returns:
            Amenity: An Amenity object created from the provided dictionary
            data.
        """
        amenity = Amenity(
            name=data['amenity_name'],
            data_manager=data_manager
        )
        amenity.id = data['amenity_id']
        amenity.created_at = datetime.fromisoformat(data['created_at'])
        amenity.updated_at = datetime.fromisoformat(data['updated_at'])
        return amenity

    @property
    def name(self):
        """ Property that gets the name of the amenity."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Setter method for updating the name of the amenity.

        Args:
            value (str): The new name of the amenity.
        """
        self._name = value
        self.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the amenity object.

        Returns:
            dict: A dictionary containing all attributes of the amenity
            object.
        """
        return {
            "amenity_id": self.id,
            "amenity_name": self._name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
