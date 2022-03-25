from events.ambulance_to_patient_departure import AmbulanceToPatientDeparture
import global_variables

class EmergencyCall:
    properties = {
        'id': int,
        'time': float, #11,25
        'event_time': []
    }

    def __init__(self, patient, time):
        self.event_time = []
        self.patient = patient
        self.time = time  # 3/60 för att räkna ut 3 minuter i decimalform. TODO: Ta fram riktigt medelvärde


    def action(self):
        # print(self.__class__.__name__ + " for patient no: " + str(self.patient.id) + ". ")
        if global_variables.ambulance.is_available:
            print("******************** NEW EMERGENCY CALL ********************")
            global_variables.simulation_clock.set_start_time(self.time)
            global_variables.simulation_clock.print_current_time_as_time_stamp()
            time_from_call_to_ambulance_departure = global_variables.simulation_clock.calculate_time(3)  # Tre minuter. Räknas ut som andel av ett dygn i calculate_time
            global_variables.ambulance.is_available = False

            return AmbulanceToPatientDeparture(self.time + time_from_call_to_ambulance_departure, self.patient)
        else:
            print("~~~~~~~~~~~~~~~~~ NEW EMERGENCY CALL QUEUED ~~~~~~~~~~~~~~~~~")
            time_to_add = global_variables.simulation_clock.calculate_time(10)
            self.time += time_to_add
            return self
