from ambulance import Ambulance
from healtcenter import HealthCenter
from hospital import Hospital

global hospital
hospital = Hospital(1, 56.0472377, 12.703307)

global health_center
health_center = HealthCenter(1, 56.2844453331, 13.27882942)

global ambulance
# Create an ambulance is available
ambulance = Ambulance(1, True, health_center.latitude, health_center.longitude)

global hospital_to_centroid_list
hospital_to_centroid_list = []
file = open("files/hospital2centroids.txt", "r")
for line in file:
    elements = line.split(",")
    hospital_to_centroid_list.append(elements)

