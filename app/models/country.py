from .base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code