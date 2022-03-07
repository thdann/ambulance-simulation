from src.ambulance import Ambulance
from src.healtcenter import HealthCenter
from src.hospital import Hospital

global hospital
hospital = Hospital(1, 12.703307, 56.0472377)

global health_center
health_center = HealthCenter(1, 56.2844453331, 13.27882942)

global ambulance
# Create an ambulance is available
ambulance = Ambulance(1, True, health_center.latitude, health_center.longitude)