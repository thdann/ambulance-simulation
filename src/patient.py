from json import load


class Patient: 
    properties = {
        'id': int, 
        'location_id': int, 
        'incident_time_day': int,
        'incident_time_hour': float,
        'triage_priority': int
    }

    def __init__(self, id, location, incident_time_hour):
        self.id = id
        self.location_id= location
        self.incident_time_hour = incident_time_hour
        print("Patient created: " + str(self.id) + " at location: " + str(self.location_id) + " at time: " + str(self.incident_time_hour))

        #self.incident_time_day = 0 #vad är detta?
        #self.triage_priority = 3 #3 = gul, ska sättas vid senare tillfälle
        #self.incident_time = self.incident_time_hour
        #self.incident_time = float(24) * float(get_attribute(self, 'incident_time_day')) + float(get_attribute(self, 'incident_time_hour'))
