class AmbulanceToPatientDeparture():
    properties = {
        'patient_position_lat': float,
        'patient_position_long': float,
        'ambulance_start_position_lat': float,
        'ambulance_start_position_long': float

    }
    def __init__(self, patient, ambulance):
        self.patient_position_lat = patient.position_lat
        self.patient_position_long = patient.position_long
        self.ambulance_position_lat = ambulance.position_lat
        self.ambulance_position_long = ambulance.position_long
        print("init AmbulanceToPatientDeparture. Patient and ambulance positions have been set.")

        



