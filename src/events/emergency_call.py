from src.events.ambulance_to_patient_departure import AmbulanceToPatientDeparture
from src.patient import Patient


class EmergencyCall():
    # properties = {
    #     'id': int,
    #     'patient': Patient,
    #     'time': float
    # }

    def __init__(self):
        print("init(EmergencyCall())")
        # self.id = new_id
        # self.patient = patient
        # self.time = patient.incident_time_hour
        # print("EmergencyCall created " + str(self.id) + "with patient: " + str(self.patient))

    def action(self):
        print("EmergencyCall.action()")
        # if ambulance.is_available:
        next_event = AmbulanceToPatientDeparture()
        next_event.action()

    # trigga ambulance to patient departure. Vad behöver vi då?
    # Är ambulance ledig? - skicka den.
    # patienten (dess loaction iaf) hela objektet?
