from tkinter import EventType
import global_variables

class AmbulanceToHealthCenterArrival():
        properties = {
                'id': int,
                'time': float
                }

        def __init__(self, event_time, patient):
                self.time = event_time + 00.05
                self.patient = patient
                print("init AmbulanceToHealthCenterArrival.")

        def action(self): #TODO: Ska ha en patient troligtvis
                print(self.__class__.__name__ + ":s actionmetod och patient: " + str(self.patient.id))
                print("end of chain")
                global_variables.ambulance.is_available=True

