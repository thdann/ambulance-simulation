from random import randint
from tkinter import EventType
from events.ambulance_to_healthcenter_departure import AmbulanceToHealthCenterDeparture
from events.ambulance_to_hospital_departure import AmbulanceToHospitalDeparture

from src.global_variables import add_to_time


class AmbulanceToPatientArrival():
    properties = {
         'id': int,
         'time': float
     }

    def __init__(self, event_time, patient):
        self.time = event_time + 0.15 # hur lång tid ambulansen tog att köra till patienten, ska räknas ut
        # self.time = event_time + 00.15 # hur lång tid ambulansen tog att köra till patienten, ska räknas ut
        self.time = add_to_time(event_time, 0.15)
        self.patient = patient
        #print("init AmbulanceToPatientArrival. ")

    def action(self):
        #print("action i " + self.__class__.__name__ + "patient " + str(self.patient.id))
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))

        self.patient.triage_priority = randint(1,4)
        print("PATIENT TRIAGE PRIO: " + str(self.patient.triage_priority)) ## 1&2 to hospital, 3&4 to healtcenter
        
        if self.patient.triage_priority < 3:
            next_event = AmbulanceToHospitalDeparture(self.time, self.patient)
        else: 
            next_event = AmbulanceToHealthCenterDeparture(self.time, self.patient)
        
        return next_event
        #next_event.action(patient)

# else:
#     next_event = AmbulanceToHealthCenterDeparture
#     next_event.action(patient)

# här ska vi sätta traige-prioritet i patient-objektet
# och kanske uppdatera tiden typ.
# och uppdatera ambulansens position (hämtas från patientens position)
