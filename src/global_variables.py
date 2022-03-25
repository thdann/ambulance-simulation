from ambulance import Ambulance
from simulation_clock import SimulationClock
from src.waiting_queue import WaitingQueue

print("***************************** Global variables ****************************")

global ambulance
# Create an ambulance is available
ambulance = Ambulance(1, True)

# global simulation_clock
simulation_clock = SimulationClock()

# global waiting_queue
waiting_queue = WaitingQueue()


