from json import load


class Patient: 
    properties = {
        'id': int,
        'position_lat': float,
        'position_long': float,
        # 'incident_time_day': int,
        # 'incident_time_hour': float,
        'triage_priority': int,
        'centroid': int
    }

    def __init__(self, id, position_lat, position_long, centroid):
        self.triage_priority = None
        self.id = id
        self.position_lat = position_lat
        self.position_long = position_long
        # self.incident_time_hour = incident_time_hour
        self.centroid = centroid
        print("Patient created: " + str(self.id) + " at location lat: " + str(self.position_lat) + " and long: "
              + str(self.position_long) + ", centroid index: " + str(self.centroid))

        #self.incident_time_day = 0 #vad är detta?
        #self.triage_priority = 3 #3 = gul, ska sättas vid senare tillfälle
        #self.incident_time = self.incident_time_hour
        #self.incident_time = float(24) * float(get_attribute(self, 'incident_time_day')) + float(get_attribute(self, 'incident_time_hour'))
