from src.events.ambulance_to_hospital_arrival import AmbulanceToHospitalArrival


class AmbulanceToHospitalDeparture:
    # properties = {
    #     'time': float,
    #     'hospital_lat': float,
    #     'hospital_long': float
    # }
    def __init__(self):
        # Hämtar koordinater till helsingborgs sjukhus:
        # self.hospital_lat = hospital.latitude
        # self.hospital_long = hospital.longitude
        #
        # self.time = None #Nån uträknad tid
        print("init AmbulanceToHospitalDeparture.")

    def action(self):
        print(self.__class__.__name__ + ":s actionmetod")
        next_event = AmbulanceToHospitalArrival
        next_event.action()