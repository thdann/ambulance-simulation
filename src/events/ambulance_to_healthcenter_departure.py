from tkinter import EventType
from events.ambulance_to_healthcenter_arrival import AmbulanceToHealthCenterArrival

import utils, global_variables


class AmbulanceToHealthCenterDeparture:
    properties = {
         'id': int,
         'time': float
     }


    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient


    def action(self):
        global_variables.simulation_clock.update_time(self.time)
        transport_time_from_file = utils.get_transport_time_to_health_center(self.patient.centroid)
        # print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))

        transport_time_as_minutes = global_variables.simulation_clock.calculate_transport_time(
            transport_time_from_file)  # Leta upp den raden i centroid_list i global_variables

        transport_time = global_variables.simulation_clock.calculate_time(
            transport_time_as_minutes)  # Hämta körtid från samma rad

        global_variables.simulation_clock.print_current_time_as_time_stamp()
        return AmbulanceToHealthCenterArrival(self.time + transport_time, self.patient)
