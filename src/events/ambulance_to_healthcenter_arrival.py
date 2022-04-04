import global_variables


class AmbulanceToHealthCenterArrival():
    properties = {
        'id': int,
        'time': float,
        'minute': int
    }

    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        global_variables.simulation_clock.update_time(self.time)
        time_to_drop_off_patient = global_variables.simulation_clock.calculate_time(5)  # Fem minuter för avlämning #TODO: Hantera detta? Eftersom detta är sista eventet...
        global_variables.simulation_clock.print_current_time_as_time_stamp()

        global_variables.simulation_clock.update_time(self.time + time_to_drop_off_patient)
        global_variables.simulation_clock.write_time_stamp_to_file()
        global_variables.simulation_clock.write_new_line()

        global_variables.ambulance.is_available = True
        print("\n")
