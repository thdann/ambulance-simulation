from events.ambulance_to_patient_departure import AmbulanceToPatientDeparture
import global_variables

class EmergencyCall():
    properties = {
         'id': int,
         'time': float
     }

    def __init__(self, patient):
        print("init(EmergencyCall())")
        self.patient = patient
        self.time = patient.incident_time_hour
        # self.id = new_id
        # self.time = patient.incident_time_hour
        # print("EmergencyCall created " + str(self.id) + "with patient: " + str(self.patient))

    def action(self):
        print("EmergencyCall.action() och patient nr: " + str(self.patient.id))

        if global_variables.ambulance.is_available:
            global_variables.ambulance.is_available=False
            return AmbulanceToPatientDeparture(self.time, self.patient)
            #next_event = AmbulanceToPatientDeparture()
            #next_event.action(self.patient)

        
        

    # trigga ambulance to patient departure. Vad behöver vi då?
    # Är ambulance ledig? - skicka den.
