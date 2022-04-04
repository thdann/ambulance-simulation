from random import randint
from events.ambulance_to_healthcenter_departure import AmbulanceToHealthCenterDeparture
from events.ambulance_to_hospital_departure import AmbulanceToHospitalDeparture

from src import global_variables


class AmbulanceToPatientArrival():
    properties = {
        'id': int,
        'time': float
    }

    def __init__(self, event_time, patient):
        self.time = event_time
        self.patient = patient

    def action(self):
        treatment_time = global_variables.simulation_clock.calculate_time(
            19)  # 19 min för vårdtid på plats. Vi tog ett genomsnitt från Åsas data
        global_variables.simulation_clock.update_time(self.time)
        global_variables.simulation_clock.print_current_time_as_time_stamp()

        # Writing to output file:
        global_variables.simulation_clock.write_time_stamp_to_file()

        # if (self.patient.triage_priority == "yellow_or_green") and (
        #         global_variables.simulation_clock.is_health_center_open(self.time)):
        #     print("ITS OPEN! " + str(self.time))
        #     next_event = AmbulanceToHealthCenterDeparture(self.time + treatment_time, self.patient)
        #     global_variables.simulation_clock.write_hospital_of_health_center_to_file("health_center")
        #     global_variables.nbr_of_patients_to_health_center += 1
        # else:
        next_event = AmbulanceToHospitalDeparture(self.time + treatment_time, self.patient)
        global_variables.simulation_clock.write_hospital_of_health_center_to_file("hospital")
        global_variables.nbr_of_patients_to_hospital += 1

        return next_event
