from os.path import dirname, join

from patient import Patient
from events.emergency_call import EmergencyCall
from events.eventlistheap import EventListHeap
from random import randint

from simulation_clock import SimulationClock
from src import global_variables


def main():
    # Create a patient for test: id, latitude, longitude, time of incident
    # print("*****************************************************************************")
    # patient1 = Patient(1, 14)
    # patient2 = Patient(2, 3410)
    # patient3 = Patient(3, 18543)
    # print("*****************************************************************************")

    # Create empty event list using heap data structure
    # scheduled_events = EventListHeap(len(global_variables.problem_data.patients_list) * 2)
    scheduled_events = EventListHeap(935 * 2)

    # Öppna filen med time + centroids
    # För varje rad i filen:
    # skapa nytt emergency_call som i sin konstruktor skapar en patient (med ett id och en centroid)
    # Därefter lägg till emergency call i scheduled_events

    current_directory = dirname(__file__)
    filepath_input_data = join(current_directory,
                               "files/input_data_2.txt")

    file = open(filepath_input_data, "r")
    counter = 1

    for line in file:
        elements = line.split(" ")
        time = float(elements[0])
        centroid = int(elements[1])
        triage_priority = elements[2].strip("\n")  # Osäker på om ny rad behöver tas bort men det känns troligt
        emergency_call = EmergencyCall(Patient(counter, centroid, triage_priority), time)
        scheduled_events.add(emergency_call)
        counter += 1

    # Emergency call for patient no. 1: Day: 1 Time: 00.01
    # Ambulance to patient departure: Day:1. Time: ...

    # Create an emergency call with patient - starts the chain of events. This should be a heap
    # emergency_call = EmergencyCall(patient)  # Se till att generera riktiga ID senare
    # emergency_call.action()

    # print('Before next event in framework.py')
    next_event = scheduled_events.next()
    # print('After next_event, time in framework.py: ', next_event)

    while next_event is not None:
        print(next_event.__class__.__name__ + " for patient no " + str(next_event.patient.id) + ":")
        # Write some code here
        # global_variables.simulation_time = next_event.time

        # print('1: counter in while in framework.py')
        new_event = next_event.action()
        # print('2')
        if new_event:
            scheduled_events.add(new_event)
        # print('3')
        next_event = scheduled_events.next()
        # print('Next_event in framework.py: ', next_event)
        # print('4')

    # print('After while in framework.py')
    # utils.safe_exit()


main()
