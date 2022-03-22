from random import randint
from events.ambulance_to_healthcenter_departure import AmbulanceToHealthCenterDeparture
from events.ambulance_to_hospital_departure import AmbulanceToHospitalDeparture


class AmbulanceToPatientArrival():
    properties = {
        'id': int,
        'time': float
    }

    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        # Vårdtid (ska räknas ut eller tas ett genomsnitt):
        treatment_time = 0.30  # 18 minuter
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))

        self.patient.triage_priority = randint(1, 4)
        print("PATIENT TRIAGE PRIO: " + str(self.patient.triage_priority))  ## 1&2 to hospital, 3&4 to healtcenter

        if self.patient.triage_priority < 3:
            next_event = AmbulanceToHospitalDeparture(self.time + treatment_time, self.patient)
        else:
            next_event = AmbulanceToHealthCenterDeparture(self.time + treatment_time, self.patient)

        return next_event