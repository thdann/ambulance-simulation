class AmbulanceToPatientArrival():
    properties = {
        'time': float

    }

    def __init__(self, patient, ambulance):
        self.time = patient.incident_time_hour # + tiden det tog för ambulansen att ta sig dit
        print("init AmbulanceToPatientArrival. ")

    def action(self):
        print("action i " + self.__class__.__name__)
        # här ska vi sätta traige-prioritet i patient-objektet
        # och kanske uppdatera tiden typ.
        # och uppdatera ambulansens position (hämtas från patientens position)





