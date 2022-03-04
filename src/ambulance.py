class Ambulance:
    properties = {
        'id': int, 
        'is_available': bool,
        'position_lat': float,
        'position_long': float
    }

    def __init__(self, id, is_available, lat, long):
        self.position_lat = lat #starting position
        self.position_long = long #starting position
        self.id=id
        self.is_available = is_available
        print("Ambulance created: " + str(self.id))

    def update_position(self, lat, long):
        self.position_lat = lat
        self.position_long = long



