import math


class SimulationClock:
    properties = {
        'time': float,
        'day': int,
        'hour': int,
        'minute': int
    }

    def __init__(self):
        self.time = 0  # None
        self.day = 0  # None
        self.hour = 1  # None
        self.minute = 1  # None

    def calculate_time(self, time):
        # self.print_current_time_as_time_stamp()
        return float(time / 1440)

    def set_start_time(self, time): # Den här metoden är exakt samma som update_time,
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

    def calculate_transport_time(self, transport_time):
        return transport_time * 60

