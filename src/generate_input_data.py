import json
from dataclasses import replace
from os.path import dirname, join
from datetime import date
from random import choices

from src.input_data import InputData

current_directory = dirname(__file__)
filepath_incoming_calls = join(current_directory, "files/incoming_calls.txt")
filepath_population = join(current_directory, "files/population.txt")
filepath_input_data = join(current_directory, "files/input_data.txt")


# Metoder för att generera vilken centroid samtalet kommer ifrån:
def generate_population_array():
    population_array = []
    file = open(filepath_population, "r")
    for line in file:
        temp_pair = []
        elements = line.split(" ")
        # print(elements[0])
        # print(elements[1])
        centroid = int(elements[0])
        population = int(elements[1])

        temp_pair.append(centroid)
        temp_pair.append(population)

        population_array.append(temp_pair)

    return population_array


def get_random_centroid(centroids, population):
    return choices(centroids, population)[0]


#  Dessa två metoder genererar time (float) för alla emergency_call:s
def get_date_time_array():
    date_time_array = []
    file = open(filepath_incoming_calls, "r")
    for line in file:
        elements = line.split(" ")
        date = elements[0]
        ymd = date.split("-")
        # datearray.append(ymd)

        time = elements[1]
        hhmmss = time.split(":")

        ymd.append(hhmmss[0])  # Append hour
        ymd.append(hhmmss[1])  # Append minute

        date_time_array.append(ymd)

    return date_time_array


def generate_call_list():
    list = []
    array = get_date_time_array()
    d0 = date(2020, 1, 1)  # Startdatum, alla dagar ska jämföras mot denna

    for call in array:
        d1 = date(int(call[0]), int(call[1]), int(call[2]))
        delta = d1 - d0

        hour_to_minutes = int(call[3]) * 60
        total_minutes = hour_to_minutes + int(call[4])
        minutes_of_day = float(total_minutes / 1440)
        result = float(delta.days) + minutes_of_day
        list.append(result)
    return list


def main():
    call_list = generate_call_list()
    population_list = generate_population_array()
    centroids = []
    population = []

    for pairs in population_list:
        centroids.append(pairs[0])
        population.append(pairs[1])

    file = open(filepath_input_data, "a")
    for call in call_list:
        file.write(str(call) + " " + str(get_random_centroid(centroids, population)) + "\n")

    file.close()


# main()



# print(get_random_centroid(centroids, population))

# file.write("Now the file has more content!")
# file.close()
