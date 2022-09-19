class Boat:
    
    def __init__(self, name):
        self.name = name
        self.size = None
        self.crew = list()

    def add_sailor(self, sailor):
        self.crew.append(sailor)

    def serialize(self):
        data = {
            'name': self.name,
            'size': self.size,
            'crew': list()
        }
        for sailor in self.crew:
            data['crew'].append(sailor.serialize())
        return data

    @classmethod
    def deserialize(cls, data):
        boat = cls(data['name'])
        boat.size = data['size']
        for data_sailor in data['crew']:
            boat.add_sailor(Sailor.deserialize(data_sailor))
        return boat


class Sailor:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def serialize(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
        }

    @classmethod
    def deserialize(cls, data):
        return cls(data['first_name'], data['last_name'])