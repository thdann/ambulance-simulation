from ambulance import Ambulance
from simulation_clock import SimulationClock
from waiting_queue import WaitingQueue

print("***************************** Global variables ****************************")

global ambulance
# Create an ambulance is available
ambulance = Ambulance(1, True)

# global simulation_clock
simulation_clock = SimulationClock()

# global waiting_queue
waiting_queue = WaitingQueue()

nbr_of_patients_to_health_center = 0

nbr_of_patients_to_hospital = 0


