import math
from os.path import dirname, join


class SimulationClock:
    properties = {
        'time': float,
        'day': int,
        'hour': int,
        'minute': int,
        'weekend_days': []
    }

    def __init__(self):
        self.time = 0  # None
        self.day = 0  # None
        self.hour = 1  # None
        self.minute = 1  # None
        self.weekend_days = self.get_weekend_days()

    def get_weekend_days(self):
        weekend_array = []
        sat = 3
        sun = 4
        while (sat < 375):
            weekend_array.append(sat)
            weekend_array.append(sun)
            sat += 7
            sun += 7

        return weekend_array

    def calculate_time(self, time):
        # self.print_current_time_as_time_stamp()
        return float(time / 1440)

    def set_start_time(self, time):  # Den här metoden är exakt samma som update_time,
        # men jag sparar den pga kan vara bra att ha
        # om vi vill spara start_time specifikt för jämförelse
        self.time = time

    def update_time(self, time):
        self.time = time

    def print_current_time_as_time_stamp(self):
        time_array = math.modf(self.time)
        day = int(time_array[1])

        #  Konvertering:
        hours = time_array[0] * 24

        # print("HOURS: " + str(hours))
        new_time_array = math.modf(hours)
        minutes = new_time_array[0] * 60
        print("Day: %d. Time: %02d.%02d" % (day, hours, minutes))

    def write_time_stamp_to_file(self):
        time_array = math.modf(self.time)
        day = int(time_array[1])

        #  Konvertering:
        hours = time_array[0] * 24

        # print("HOURS: " + str(hours))
        new_time_array = math.modf(hours)
        minutes = new_time_array[0] * 60
        current_directory = dirname(__file__)
        filepath_population = join(current_directory, "files/result_both_destinations.txt")
        file = open(filepath_population, "a")
        file.write(" %d %02d:%02d" % (day, hours, minutes))
        file.close()

    def write_patient_id_to_file(self, patient):
        current_directory = dirname(__file__)
        filepath_population = join(current_directory, "files/result_both_destinations.txt")
        file = open(filepath_population, "a")
        file.write(str(patient.id))
        file.close()

    def write_hospital_of_health_center_to_file(self, destination):
        current_directory = dirname(__file__)
        filepath_population = join(current_directory, "files/result_both_destinations.txt")
        file = open(filepath_population, "a")
        file.write(" " + destination)
        file.close()

    def write_new_line(self):
        current_directory = dirname(__file__)
        filepath_population = join(current_directory, "files/result_both_destinations.txt")
        file = open(filepath_population, "a")
        file.write("\n")
        file.close()

    def calculate_transport_time(self, transport_time):
        return transport_time * 60

    def is_health_center_open(self, time):
        arr = math.modf(time)
        day = arr[1]
        minutes = arr[0]
        print("day: " + str(day) + ". minutes: " + str(minutes))
        is_open = False

        if self.weekend_days.__contains__(day):
            print("false by day")

        else:
            if (minutes > 0.3333) and (minutes < 0.625):
                is_open = True
            else:
                print("false by time of day")

        return is_open
