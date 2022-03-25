import global_variables


class AmbulanceBackToSiteArrival:
    properties = {
        'id': int,
        'time': float
    }

    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        global_variables.simulation_clock.update_time(self.time)
        global_variables.simulation_clock.print_current_time_as_time_stamp()
        global_variables.ambulance.is_available = True

        print("\n")
