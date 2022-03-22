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
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        global_variables.simulation_clock.add_to_time(self.time)
        global_variables.ambulance.is_available = True
        print("end of chain")
        print("\n")
