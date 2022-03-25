from events.ambulance_to_hospital_arrival import AmbulanceToHospitalArrival

from src import global_variables, utils


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
        # print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        global_variables.simulation_clock.update_time(self.time)

        # Hämta patientens centroid
        # Leta upp den raden i centroid_list i global_variables
        # Hämta körtid från samma rad
        transport_time_from_file = utils.get_transport_time(self.patient.centroid)
        transport_time_as_minutes = global_variables.simulation_clock.calculate_transport_time(transport_time_from_file)
        transport_time = global_variables.simulation_clock.calculate_time(transport_time_as_minutes)

        global_variables.simulation_clock.print_current_time_as_time_stamp()
        return AmbulanceToHospitalArrival(self.time + transport_time, self.patient)
