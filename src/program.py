from patient import Patient
from events.emergency_call import EmergencyCall
from events.eventlistheap import EventListHeap
from random import randint

from src.simulation_clock import SimulationClock


def main():
    clock = SimulationClock()
    print(clock.print_current_time())
    # Create a patient for test: id, latitude, longitude, time of incident
    print("*****************************************************************************")
    patient1 = Patient(1, 56.25097, 13.21273, 13.00)
    patient2 = Patient(2, 56.30097, 13.21273, 14.00)
    patient3 = Patient(3, 56.40097, 13.21273, 15.00)
    print("*****************************************************************************")

    # Create empty event list using heap data structure
    #scheduled_events = EventListHeap(len(global_variables.problem_data.patients_list) * 2)
    scheduled_events = EventListHeap(3 * 2)
    
    scheduled_events.add(EmergencyCall(patient1, 0, 11, 25))
    # scheduled_events.add(EmergencyCall(patient2, 14.0))
    # scheduled_events.add(EmergencyCall(patient3, 16.0))

  

    # Create an emergency call with patient - starts the chain of events. This should be a heap
    #emergency_call = EmergencyCall(patient)  # Se till att generera riktiga ID senare
    #emergency_call.action()


    #print('Before next event in framework.py')
    next_event = scheduled_events.next()
    #print('After next_event, time in framework.py: ', next_event)

    while next_event is not None:
        # Write some code here
        #global_variables.simulation_time = next_event.time

        #print('1: counter in while in framework.py')
        new_event = next_event.action()
        #print('2')
        if new_event:
            scheduled_events.add(new_event)
        #print('3')
        next_event = scheduled_events.next()
        #print('Next_event in framework.py: ', next_event)
        #print('4')

    # print('After while in framework.py')
    #utils.safe_exit()


main()
