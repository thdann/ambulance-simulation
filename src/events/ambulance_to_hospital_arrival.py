from tkinter import EventType
import global_variables

class AmbulanceToHospitalArrival:
    properties = {
         'id': int,
         'time': float
     }

    def __init__(self, event_time, patient):
        # Hämtar koordinater till helsingborgs sjukhus:
        # self.hospital_lat = hospital.latitude
        # self.hospital_long = hospital.longitude
        #
        # self.time = None  # Nån uträknad tid
        self.time = event_time + 00.20 # tiden det tar att köra till sjukhuset, ska räknas ut. 
        self.patient = patient
        #print("init AmbulanceToHospitalDeparture.")

    def action(self):
        #print(self.__class__.__name__ + ":s actionmetod och patient: " + str(self.patient.id))
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        print("End of chain. Total time: ")
        print("\n")
        global_variables.ambulance.is_available=True
        # ambulance.is_available = True
