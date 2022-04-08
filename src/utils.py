# global hospital_to_centroid_list

from os.path import dirname, join


current_directory = dirname(__file__)
filepath_transport_centroids = join(current_directory, "files/hospital2centroids.txt")
filepath_transport_to_healthcenter = join(current_directory, "files/ambulance_site_to_centroids.txt")



def get_transport_time(centroid):
    # print("centroid: " + str(centroid))
    file = open(filepath_transport_centroids, "r")
    next(file)
    for line in file:
        elements = line.split(",")
        centroid_id = int(elements[2])
        if centroid_id - centroid == 0:
            return float(elements[3])


def get_transport_time_to_health_center(centroid):
    file = open(filepath_transport_to_healthcenter, "r")
    for line in file:
        elements = line.split(" ")
        centroid_id = int(elements[1])
        if centroid_id - centroid == 0:
            return float(elements[2])
