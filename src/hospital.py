class Hospital:
    properties = {
        'id': int, 
        'latitude': float,
        'longitude': float
    }

    def __init__(self, id, latitude, longitude):
        self.id=id
        self.latitude = latitude
        self.longitude = longitude
        print("Hospital created: ID: " + str(self.id))
