from events.ambulance_to_hospital_arrival import AmbulanceToHospitalArrival


class AmbulanceToHospitalDeparture:
    properties = {
         'id': int,
         'time': float
     }
     
    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        # Transporteringstid (hämtas från Johans data):
        transport_time = 0.50 # Tar en halvtimme säger vi
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        return AmbulanceToHospitalArrival(self.time + transport_time, self.patient)
