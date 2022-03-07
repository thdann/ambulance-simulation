from events.ambulance_to_hospital_arrival import AmbulanceToHospitalArrival


class AmbulanceToHospitalDeparture:
    properties = {
         'id': int,
         'time': float
     }
     
    def __init__(self, event_time, patient):
        # Hämtar koordinater till helsingborgs sjukhus:
        # self.hospital_lat = hospital.latitude
        # self.hospital_long = hospital.longitude
        #
        # self.time = None #Nån uträknad tid
        self.time = event_time + 00.10
        self.patient = patient
        print("init AmbulanceToHospitalDeparture.")

    def action(self):
        print(self.__class__.__name__ + ":s actionmetod och patient: " + str(self.patient.id))
        return AmbulanceToHospitalArrival(self.time, self.patient)
        #next_event = AmbulanceToHospitalArrival()
        #next_event.action(patient)