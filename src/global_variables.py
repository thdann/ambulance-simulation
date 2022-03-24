from ambulance import Ambulance
from healtcenter import HealthCenter
from hospital import Hospital
from src.simulation_clock import SimulationClock

print("***************************** Global variables ****************************")

global hospital
hospital = Hospital(1, 56.0472377, 12.703307)

global health_center
health_center = HealthCenter(1, 56.2844453331, 13.27882942)

global ambulance
# Create an ambulance is available
ambulance = Ambulance(1, True, health_center.latitude, health_center.longitude)

global simulation_clock
simulation_clock = SimulationClock()


