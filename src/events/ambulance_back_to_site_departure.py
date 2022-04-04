import global_variables
from src.events.ambulance_back_to_site_arrival import AmbulanceBackToSiteArrival


class AmbulanceBackToSiteDeparture:
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

        driving_time_back_to_site = 0.581386111 # Körtid från sjukhus till centroid 6726
        transport_time_as_minutes = global_variables.simulation_clock.calculate_transport_time(driving_time_back_to_site)
        transport_time = global_variables.simulation_clock.calculate_time(
            transport_time_as_minutes)  # Hämta körtid från samma rad
        return AmbulanceBackToSiteArrival(self.time + transport_time, self.patient)