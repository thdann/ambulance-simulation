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
        # print(self.__class__.__name__ + " patient nr: " + str(self.patient.id) + " time: " + str(self.time))
        # TODO: Vårdtid (ska räknas ut eller tas ett genomsnitt):
        treatment_time = global_variables.simulation_clock.calculate_time(30)
        global_variables.simulation_clock.update_time(self.time)
        global_variables.simulation_clock.print_current_time_as_time_stamp()


        #TODO: Här under är kod som ska avändas när körtider till vårdcentralen är implementerade:

        """ 
        if self.patient.triage_priority == "yellow_or_green":
            next_event = AmbulanceToHealthCenterDeparture(self.time + treatment_time, self.patient)
        elif self.patient.triage_priority == "red_or_orange":
            next_event = AmbulanceToHospitalDeparture(self.time + treatment_time, self.patient)
        """

        #TODO: Den här implementationen av triage_priority ska plockas bort:
        self.patient.triage_priority = randint(1, 2)
        # print("PATIENT TRIAGE PRIO: " + str(self.patient.triage_priority))  ## 1&2 to hospital, 3&4 to healtcenter

        if self.patient.triage_priority < 3:
            # print("Ambulance to patient arrival")

            next_event = AmbulanceToHospitalDeparture(self.time + treatment_time, self.patient)
        else:
            next_event = AmbulanceToHealthCenterDeparture(self.time + treatment_time, self.patient)

        return next_event