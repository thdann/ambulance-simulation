from tkinter import EventType
from events.ambulance_to_healthcenter_arrival import AmbulanceToHealthCenterArrival


class AmbulanceToHealthCenterDeparture():
    properties = {
         'id': int,
         'time': float
     }


    def __init__(self, event_time, patient):
        self.time = event_time + 00.10
        self.patient = patient
        print("init AmbulanceToHealthCenterDeparture.")
        # Hämtar koordinater till health center
     #   self.time = None #Nån uträknad tid

       

    def action(self):
        print(self.__class__.__name__ + ":s actionmetod och patient: " + str(self.patient.id))
        return AmbulanceToHealthCenterArrival(self.time, self.patient)
        #next_event = AmbulanceToHealthCenterArrival()
        #next_event.action(patient)