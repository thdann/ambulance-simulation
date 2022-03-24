from json import load


class Patient: 
    properties = {
        'id': int,
        'triage_priority': int,
        'centroid': int
    }

    def __init__(self, id, centroid):
        self.triage_priority = None
        self.id = id
        self.centroid = centroid
        print("Patient created: " + str(self.id) + ", centroid index: " + str(self.centroid))

        #self.incident_time_day = 0 #vad är detta?
        #self.triage_priority = 3 #3 = gul, ska sättas vid senare tillfälle
        #self.incident_time = self.incident_time_hour
        #self.incident_time = float(24) * float(get_attribute(self, 'incident_time_day')) + float(get_attribute(self, 'incident_time_hour'))
