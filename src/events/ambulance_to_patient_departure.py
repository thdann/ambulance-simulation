from events.ambulance_to_patient_arrival import AmbulanceToPatientArrival

import global_variables, utils


class AmbulanceToPatientDeparture:
    properties = {
        'id': int,
        'time': float
    }

    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        # TODO: Räkna ut körtid (från datan som saknas)

        driving_time_from_file = utils.get_transport_time_to_health_center(self.patient.centroid)
        # print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))

        driving_time_as_minutes = global_variables.simulation_clock.calculate_transport_time(
            driving_time_from_file)  # Leta upp den raden i centroid_list i global_variables

        driving_time = global_variables.simulation_clock.calculate_time(
            driving_time_as_minutes)  # Hämta körtid från samma rad

        global_variables.simulation_clock.update_time(self.time)
        global_variables.simulation_clock.print_current_time_as_time_stamp()

        # Writing to output file:
        global_variables.simulation_clock.write_time_stamp_to_file()
        return AmbulanceToPatientArrival(self.time + driving_time, self.patient)
