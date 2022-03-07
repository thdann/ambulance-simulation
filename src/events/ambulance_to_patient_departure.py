# from src import patient, ambulance
from src.events.ambulance_to_patient_arrival import AmbulanceToPatientArrival


class AmbulanceToPatientDeparture:
    # properties = {
    #     'patient_position_lat': float,
    #     'patient_position_long': float,
    #     'ambulance_start_position_lat': float,
    #     'ambulance_start_position_long': float
    #
    # }

    def __init__(self):
        # self.patient_position_lat = patient.position_lat
        # self.patient_position_long = patient.position_long
        # ambulance.is_available = False
        print("init AmbulanceToPatientDeparture. Patient and ambulance positions have been set.")

    def action(self):
        print(self.__class__.__name__ + ":s actionmetod")
        next_event = AmbulanceToPatientArrival()
        next_event.action()

