# global hospital_to_centroid_list


def get_transport_time(centroid):
    print("centroid: " + str(centroid))
    file = open("files/hospital2centroids.txt", "r")
    next(file)
    for line in file:
        elements = line.split(",")
        centroid_id = int(elements[2])
        print("centroid ID: " + str(centroid_id))
        if centroid_id - centroid == 0:
            return elements[3]

        # hospital_to_centroid_list.append(elements)


