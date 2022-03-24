import global_variables


class AmbulanceToHospitalArrival:
    properties = {
        'id': int,
        'time': float,
        'time_hour': int,  # dessa två ints är ett tänkbart sätt att hantera tiden. Vågar inte göra det i nuläget
        'time_minute': int  # pga omfattande och vill vänta till efter mötet med Johan

    }

    def __init__(self, event_time, patient):
        self.time = event_time  # Nån uträknad tid
        self.patient = patient

    def action(self):
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        global_variables.simulation_clock.update_time(self.time)
        time_to_drop_off_patient = global_variables.simulation_clock.calculate_time(5)  # Fem minuter för avlämning
        print("--- hospital arrival 1")
        global_variables.simulation_clock.print_current_time_as_time_stamp()
        print("--- hospital arrival 2")
        # global_variables.simulation_clock.set_stop_time(self.time)
        global_variables.ambulance.is_available = True
        print("end of chain")
        print("\n")
