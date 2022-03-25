class Ambulance:
    properties = {
        'id': int, 
        'is_available': bool
    }

    def __init__(self, id, is_available):
        self.id=id
        self.is_available = is_available
        print("Ambulance created: " + str(self.id))




