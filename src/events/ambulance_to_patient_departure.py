from events.ambulance_to_patient_arrival import AmbulanceToPatientArrival

from src import global_variables


class AmbulanceToPatientDeparture:
    properties = {
        'id': int,
        'time': float
    }

    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        # Räkna ut körtid:
        driving_time = global_variables.simulation_clock.calculate_time(10)
        global_variables.simulation_clock.update_time(self.time)
        print("--- patient departure 1")
        global_variables.simulation_clock.print_current_time_as_time_stamp()
        print("--- patient departure 2")
        # print("Ambulance to patient departure")
        return AmbulanceToPatientArrival(self.time + driving_time, self.patient)
