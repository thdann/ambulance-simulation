from src.events.ambulance_to_healthcenter_departure import AmbulanceToHealthCenterDeparture
from src.events.ambulance_to_hospital_departure import AmbulanceToHospitalDeparture


class AmbulanceToPatientArrival():
    properties = {
        'time': float

    }

    def __init__(self):
        # self.time = patient.incident_time_hour # + tiden det tog för ambulansen att ta sig dit
        print("init AmbulanceToPatientArrival. ")

    def action(self):
        print("action i " + self.__class__.__name__)
        # patient.triage_priority = 1
        # if patient.triage_priority < 3:
        next_event = AmbulanceToHospitalDeparture()
        next_event.action()

# else:
#     next_event = AmbulanceToHealthCenterDeparture
#     next_event.action(patient)

# här ska vi sätta traige-prioritet i patient-objektet
# och kanske uppdatera tiden typ.
# och uppdatera ambulansens position (hämtas från patientens position)
