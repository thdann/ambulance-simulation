import global_variables

from src.events.ambulance_back_to_site_departure import AmbulanceBackToSiteDeparture


class AmbulanceToHospitalArrival:
    properties = {
        'id': int,
        'time': float
    }

    def __init__(self, event_time, patient):
        self.time = event_time  # Nån uträknad tid
        self.patient = patient

    def action(self):
        # print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        global_variables.simulation_clock.update_time(self.time)
        time_to_drop_off_patient = global_variables.simulation_clock.calculate_time(5)  # Fem minuter för avlämning
        global_variables.simulation_clock.print_current_time_as_time_stamp()
        # global_variables.ambulance.is_available = True
        # global_variables.simulation_clock.set_stop_time(self.time)

        return AmbulanceBackToSiteDeparture(self.time + time_to_drop_off_patient, self.patient)

