from ambulance import Ambulance
from events.emergency_call import EmergencyCall
from patient import Patient


def main():
    
    #Create an ambulance is available
    ambulance = Ambulance(1, True)

    # Create a patient for test
    patient = Patient(1,10,13.00)

    # Create an emergency call with patient
    emergencyCall = EmergencyCall(patient)
    emergencyCall.action()

    

main()

