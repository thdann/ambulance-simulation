# from src import patient, ambulance
from events.ambulance_to_patient_arrival import AmbulanceToPatientArrival


class AmbulanceToPatientDeparture:
    properties = {
         'id': int,
         'time': float
     }

    def __init__(self, event_time, patient):
        self.time = event_time + 00.05
        self.patient = patient
        # self.patient_position_lat = patient.position_lat
        # self.patient_position_long = patient.position_long
        # ambulance.is_available = False
        #print("init AmbulanceToPatientDeparture. Patient and ambulance positions have been set.")

    def action(self):
        #print(self.__class__.__name__ + ":s actionmetod och patient: " + str(self.patient.id))
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id)+ " time: " + str(self.time))
        return AmbulanceToPatientArrival(self.time, self.patient)
        
        #next_event = AmbulanceToPatientArrival()
        #next_event.action(patient)

