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
        self.patient = patient
        time_to_hospital = float(global_variables.hospital_to_centroid_list[patient.centroid][3])
        self.time = event_time + time_to_hospital
        print("TIME TO HOSPITAL: " + str(time_to_hospital))

    def action(self):
        print(self.__class__.__name__ + ":s actionmetod och patient: " + str(self.patient.id))
        print("PATIENT AVLÄMNAD KLOCKAN: " + str(self.time))
        print("End of chain")
        global_variables.ambulance.is_available=True
        # ambulance.is_available = True
