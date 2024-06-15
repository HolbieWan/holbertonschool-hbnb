from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """
    Abstract base class for persistence managers.

    This class defines the interface for managing the persistence of entities,
    including saving, retrieving, updating, and deleting entities. Any concrete
    implementation of this interface should provide the specific mechanisms for
    these operations.

    Methods:
        save(entity):
            Save an entity to the persistence layer.

        get(entity_id, entity_type):
            Retrieve an entity from the persistence layer by its ID and type.

        update(entity):
            Update an existing entity in the persistence layer.

        delete(entity_id, entity_type):
            Delete an entity from the persistence layer by its ID and type.
    """
    @abstractmethod
    def save(self, entity):
        """
        Save an entity to the persistence layer.

        Args:
            entity (object): The entity to be saved.

        Raises:
            NotImplementedError: If the method is not implemented by a
            subclass.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve an entity from the persistence layer by its ID and type.

        Args:
            entity_id (str): The unique identifier of the entity.
            entity_type (str): The type of the entity.

        Returns:
            object: The retrieved entity.

        Raises:
            NotImplementedError: If the method is not implemented by a
            subclass.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update an existing entity in the persistence layer.

        Args:
            entity (object): The entity with updated data.

        Raises:
            NotImplementedError: If the method is not implemented by a
            subclass.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity from the persistence layer by its ID and type.

        Args:
            entity_id (str): The unique identifier of the entity to be
            deleted.
            entity_type (str): The type of the entity to be deleted.

        Raises:
            NotImplementedError: If the method is not implemented by a
            subclass.
        """
        pass
