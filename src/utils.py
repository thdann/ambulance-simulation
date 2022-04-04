# global hospital_to_centroid_list


def get_transport_time(centroid):
    # print("centroid: " + str(centroid))
    file = open("files/hospital2centroids.txt", "r")
    next(file)
    for line in file:
        elements = line.split(",")
        centroid_id = int(elements[2])
        if centroid_id - centroid == 0:
            return float(elements[3])


def get_transport_time_to_health_center(centroid):
    file = open("files/ambulance_site_to_centroids.txt", "r")
    for line in file:
        elements = line.split(" ")
        centroid_id = int(elements[1])
        if centroid_id - centroid == 0:
            return float(elements[2])
