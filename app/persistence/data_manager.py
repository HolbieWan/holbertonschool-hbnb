import json
import os
from persistence.ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    """
    DataManager implements the IPersistenceManager interface for handling
    persistence of various entities using JSON files.

    Attributes:
        storage (dict): A dictionary storing all entities by their type.
        data_file (str): The path to the JSON file for persistence.

    Methods:
        create_directory_if_not_exists():
            Ensures the directory for the data file exists.

        load_from_json():
            Loads entities from the JSON file into the storage.

        dict_to_entity(entity_type, entity_data):
            Converts a dictionary to an entity object.

        save(entity):
            Saves an entity to the storage and updates the JSON file.

        get(entity_id, entity_type):
            Retrieves an entity by its ID and type from the storage.

        get_by_email(email):
            Retrieves a User entity by its email.

        get_country_by_code(country_code):
            Retrieves a Country entity by its code.

        place_exists_with_attributes(...):
            Checks if a Place entity exists with the specified attributes.

        review_exists_with_attributes(place_id, user_id):
            Checks if a Review entity exists with the specified attributes.

        city_exists_with_name_and_country(name, country_id):
            Checks if a City entity exists with the specified attributes.

        amenity_exists_with_name(name):
            Checks if an Amenity entity exists with the specified name.

        get_reviews_by_place_id(place_id):
            Retrieves all Review entities for a given place.

        get_reviews_by_user_id(user_id):
            Retrieves all Review entities for a given user.

        update(entity):
            Updates an existing entity in the storage and JSON file.

        delete(entity_id, entity_type):
            Deletes an entity by its ID and type from the storage
            and JSON file.

        save_to_json(file_path=None):
            Saves the current state of the storage to the JSON file.
    """

    def __init__(self, data_file):
        self.storage = {}
        self.data_file = data_file
        self.create_directory_if_not_exists()
        self.load_from_json()

    def create_directory_if_not_exists(self):
        """
        Ensures the directory for the data file exists.
        If it doesn't exist, the directory is created.
        """
        directory = os.path.dirname(self.data_file)

        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_from_json(self):
        """
        Loads entities from the JSON file into the storage.
        Handles the conversion of dictionaries to entity objects.
        """
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for entity_type, entities in data.items():
                    self.storage[entity_type] = {}
                    for entity_id, entity_data in entities.items():
                        try:
                            entity = self.dict_to_entity(
                                entity_type, entity_data)
                            self.storage[entity_type][entity_id] = entity
                        except ValueError as e:
                            print(f"Skipping invalid {entity_type}: {e}")
        except FileNotFoundError:
            self.storage = {}

    def dict_to_entity(self, entity_type, entity_data):
        """
        Converts a dictionary to an entity object.

        Args:
            entity_type (str): The type of the entity.
            entity_data (dict): The data of the entity.

        Returns:
            object: The entity object.
        """
        module = __import__('models.' + entity_type.lower(),
                            fromlist=[entity_type])
        entity_class = getattr(module, entity_type)
        return entity_class.from_dict(entity_data, self)

    def save(self, entity):
        """
        Saves an entity to the storage and updates the JSON file.

        Args:
            entity (object): The entity to save.

        Returns:
            object: The saved entity.
        """
        entity_type = type(entity).__name__

        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity
        self.save_to_json()
        return entity

    def get(self, entity_id, entity_type):
        """
        Retrieves an entity by its ID and type from the storage.

        Args:
            entity_id (str): The ID of the entity.
            entity_type (str): The type of the entity.

        Returns:
            object: The retrieved entity or None if not found.
        """
        if entity_type in self.storage \
                and entity_id in self.storage[entity_type]:
            return self.storage[entity_type][entity_id]
        return None

    def get_by_email(self, email):
        """
        Retrieves a User entity by its email.

        Args:
            email (str): The email of the user.

        Returns:
            object: The User entity or None if not found.
        """
        users = self.storage.get('User', {}).values()
        for user in users:
            if user.email == email:
                return user
        return None

    def get_country_by_code(self, country_code):
        """
        Retrieves a Country entity by its code.

        Args:
            country_code (str): The code of the country.

        Returns:
            object: The Country entity or None if not found.
        """
        countries = self.storage.get('Country', {}).values()
        for country in countries:
            if country.code == country_code:
                return country
        return None

    def place_exists_with_attributes(self, name, address, city_id, host_id,
                                     num_rooms, num_bathrooms,
                                     price_per_night, max_guests):
        """
        Checks if a Place entity exists with the specified attributes.

        Args:
            name (str): The name of the place.
            address (str): The address of the place.
            city_id (str): The city ID.
            host_id (str): The host ID.
            num_rooms (int): The number of rooms.
            num_bathrooms (int): The number of bathrooms.
            price_per_night (float): The price per night.
            max_guests (int): The maximum number of guests.

        Returns:
            bool: True if the place exists, False otherwise.
        """

        places = self.storage.get('Place', {}).values()

        for place in places:
            if (place._name == name and
                place._address == address and
                place._city_id == city_id and
                place._host_id == host_id and
                place._num_rooms == num_rooms and
                place._num_bathrooms == num_bathrooms and
                place._price_per_night == price_per_night and
                    place._max_guests == max_guests):
                return True
        return False

    def review_exists_with_attributes(self, place_id, user_id):
        """
        Checks if a Review entity exists with the specified attributes.

        Args:
            place_id (str): The place ID.
            user_id (str): The user ID.

        Returns:
            bool: True if the review exists, False otherwise.
        """
        reviews = self.storage.get('Review', {}).values()

        for review in reviews:
            if review._place_id == place_id and review._user_id == user_id:
                return True
        return False

    def city_exists_with_name_and_country(self, name, country_id):
        """
        Checks if a City entity exists with the specified attributes.

        Args:
            name (str): The name of the city.
            country_id (str): The country ID.

        Returns:
            bool: True if the city exists, False otherwise.
        """
        cities = self.storage.get('City', {}).values()

        for city in cities:
            if city._name == name and city._country_id == country_id:
                return True
        return False

    def amenity_exists_with_name(self, name):
        """
        Checks if an Amenity entity exists with the specified name.

        Args:
            name (str): The name of the amenity.

        Returns:
            bool: True if the amenity exists, False otherwise.
        """
        amenities = self.storage.get('Amenity', {}).values()

        for amenity in amenities:
            if amenity._name == name:
                return True
        return False

    def get_reviews_by_place_id(self, place_id):
        """
        Retrieves all Review entities for a given place.

        Args:
            place_id (str): The place ID.

        Returns:
            list: List of Review entities.
        """
        return [review for review in
                self.storage.get('Review', {}).values()
                if review.place_id == place_id]

    def get_reviews_by_user_id(self, user_id):
        """
        Retrieves all Review entities for a given user.

        Args:
            user_id (str): The user ID.

        Returns:
            list: List of Review entities.
        """
        return [review for review
                in self.storage.get('Review', {}).values()
                if review.user_id == user_id]

    def update(self, entity):
        """
        Updates an existing entity in the storage and JSON file.

        Args:
            entity (object): The entity with updated data.

        Returns:
            object: The updated entity or None if not found.
        """
        entity_type = type(entity).__name__
        if entity_type in self.storage \
                and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity
            self.save_to_json()
            return entity
        return None

    def delete(self, entity_id, entity_type):
        """
        Deletes an entity by its ID and type from the storage and updates
        the JSON file.

        Args:
            entity_id (str): The ID of the entity to delete.
            entity_type (str): The type of the entity to delete.

        Returns:
            bool: True if the entity was successfully deleted, False
            otherwise.
        """
        if entity_type in self.storage \
                and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            self.save_to_json()
            return True
        return False

    def save_to_json(self, file_path=None):
        """
        Saves the current state of the storage to the JSON file.

        Args:
            file_path (str, optional): The path to the JSON file.
            If not provided,
            defaults to the initialized data_file path.
        """

        if not file_path:
            file_path = self.data_file
        serializable_storage = {}
        for entity_type, entities in self.storage.items():
            entity_dict = {}
            for entity_id, entity in entities.items():
                entity_data = entity.to_dict()
                entity_dict[entity_id] = entity_data
            serializable_storage[entity_type] = entity_dict
        with open(file_path, 'w') as file:
            json.dump(serializable_storage, file, indent=4)
