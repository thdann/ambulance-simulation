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
        print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        # Vårdtid (ska räknas ut eller tas ett genomsnitt):
        treatment_time = global_variables.simulation_clock.calculate_time(30)  # 18 minuter
        global_variables.simulation_clock.update_time(self.time)
        print("--- patient arrival 1")
        global_variables.simulation_clock.print_current_time_as_time_stamp()
        print("--- patient arrival 1")

        self.patient.triage_priority = randint(1, 2)
        print("PATIENT TRIAGE PRIO: " + str(self.patient.triage_priority))  ## 1&2 to hospital, 3&4 to healtcenter

        if self.patient.triage_priority < 3:
            # print("Ambulance to patient arrival")

            next_event = AmbulanceToHospitalDeparture(self.time + treatment_time, self.patient)
        else:
            next_event = AmbulanceToHealthCenterDeparture(self.time + treatment_time, self.patient)

        return next_event