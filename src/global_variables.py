from ambulance import Ambulance
from healtcenter import HealthCenter
from hospital import Hospital

print("***************************** Global variables ****************************")

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


def add_to_time(current_time_hours, current_time_minutes, time_to_add):
    new_time = current_time_minutes + time_to_add
    decimals = str(new_time).split('.')[1]
    if int(decimals) > 59:
        new_time = new_time + 0.40
    print("--------- RETURNING: " + str(new_time))
    return float("{:.2f}".format(new_time))

