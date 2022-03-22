from tkinter import EventType
from events.ambulance_to_healthcenter_arrival import AmbulanceToHealthCenterArrival


class AmbulanceToHealthCenterDeparture:
    properties = {
         'id': int,
         'time': float
     }


    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient


    def action(self):
        transport_time = 0.20 # Tar 12 minuter
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        return AmbulanceToHealthCenterArrival(self.time + transport_time, self.patient)
