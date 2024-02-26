class TemporaryStorage:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        self.data[key] = value

    def read(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def filter(self, filter_func):
        return {key: value for key, value in self.data.items() if filter_func(value)}
