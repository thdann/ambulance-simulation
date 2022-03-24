from events.ambulance_to_hospital_arrival import AmbulanceToHospitalArrival

from src import global_variables


class AmbulanceToHospitalDeparture:
    properties = {
         'id': int,
         'time': float
     }
     
    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        # Transporteringstid (hämtas från Johans data):
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        global_variables.simulation_clock.update_time(self.time)
        transport_time = global_variables.simulation_clock.calculate_time(30) # Tar en halvtimme säger vi
        print("--- hospital departure 1")
        global_variables.simulation_clock.print_current_time_as_time_stamp()
        print("--- hospital departure 2")
        return AmbulanceToHospitalArrival(self.time + transport_time, self.patient)
