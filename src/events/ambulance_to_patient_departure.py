from events.ambulance_to_patient_arrival import AmbulanceToPatientArrival


class AmbulanceToPatientDeparture:
    properties = {
        'id': int,
        'time': float
    }

    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        # Räkna ut körtid:
        driving_time = 0.10
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        return AmbulanceToPatientArrival(self.time + driving_time, self.patient)