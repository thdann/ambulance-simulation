from ambulance import Ambulance
from events.emergency_call import EmergencyCall
from patient import Patient
from hospital import Hospital
from healtcenter import HealthCenter
from events.ambulance_to_patient_departure import AmbulanceToPatientDeparture
from src.events.ambulance_to_hospital_departure import AmbulanceToHospitalDeparture
from src.events.ambulance_to_patient_arrival import AmbulanceToPatientArrival


def main():
    # Create a patient for test
    patient = Patient(1, 56.25097, 13.21273, 13.00)

    # Create an emergency call with patient
    emergency_call = EmergencyCall()  # Se till att generera riktiga ID senare
    emergency_call.action()



main()
