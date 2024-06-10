import uuid

class Country:
    def __init__(self, name, code):
        self.id = str(uuid.uuid4())
        self.name = name
        self.code = code

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
        }