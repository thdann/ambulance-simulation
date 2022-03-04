from ambulance import Ambulance
from events.emergency_call import EmergencyCall
from patient import Patient
from hospital import Hospital
from healtcenter import HealthCenter
from events.ambulance_to_patient_departure import AmbulanceToPatientDeparture
from src.events.ambulance_to_hospital_departure import AmbulanceToHospitalDeparture
from src.events.ambulance_to_patient_arrival import AmbulanceToPatientArrival


def main():
    #Create Helsingborg hospital
    hospital = Hospital(1, 12.703307, 56.0472377)

    #Create Örkelljunga health center
    health_center = HealthCenter(1, 56.2844453331, 13.27882942)
    
    #Create an ambulance is available
    ambulance = Ambulance(1, True, health_center.latitude, health_center.longitude)

    # Create a patient for test
    patient = Patient(1,56.25097, 13.21273, 13.00)

    # Create an emergency call with patient
    emergency_call = EmergencyCall(patient)
    #emergencyCall.action()
    if (ambulance.is_available):
        #Här behöver det ske en uträkning/hämtaning av data som säger hur lång tid resan kommer ta
        ambulance_to_patient_departure = AmbulanceToPatientDeparture(patient, ambulance)
        ambulance_to_patient_arrival = AmbulanceToPatientArrival(patient, ambulance)
        patient.triage_priority = 1
        if patient.triage_priority < 3:
            ambulance_to_hospital_departure = AmbulanceToHospitalDeparture(patient, ambulance, hospital)




    

main()

