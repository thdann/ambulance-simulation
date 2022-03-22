from events.ambulance_to_patient_departure import AmbulanceToPatientDeparture
import global_variables


class EmergencyCall:
    properties = {
        'id': int,
        'time': float,
        'event_time': []
    }

    def __init__(self, patient, day, hour, minute):
        self.event_time = []
        self.patient = patient
        self.time = 0.05 # 3/60 för att räkna ut 3 minuter i decimalform. TODO: Ta fram riktigt medelvärde
        self.event_time.append(day)
        self.event_time.append(hour)
        self.event_time.append(minute)
        global_variables.simulation_clock.set_start_time(day, hour, minute) # Sätter starttid i klockan.


    def action(self):
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        if global_variables.ambulance.is_available:
            global_variables.simulation_clock.set_start_time(self.event_time[0], self.event_time[1], self.event_time[2])
            global_variables.ambulance.is_available = False
            return AmbulanceToPatientDeparture(self.time, self.patient)