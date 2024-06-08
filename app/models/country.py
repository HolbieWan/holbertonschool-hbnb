class Country:
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_code(self):
        return self.code
    
    def set_code(self, code):
        self.code = code