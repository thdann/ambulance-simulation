import math


class SimulationClock:
    properties = {
        'time': float,
        'day': int,  # TODO: Går att göra dessa till typ key/value pairs i en array
        'hour': int,
        'minute': int,
        'recent_stop_time_day': int,
        'recent_stop_time_hour': int,
        'recent_stop_time_minute': int
    }

    def __init__(self):
        self.time = 0  # None
        self.day = 0  # None
        self.hour = 1  # None
        self.minute = 1  # None

    def calculate_time(self, time):  # TODO: Ska räkna om time till dagar, timmar och minuter
        # self.print_current_time_as_time_stamp()
        return float(time / 1440)

    def set_start_time(self, time):
        self.time = time
        print("Simulation clock set_start_time()")
        print("Set start time: ")
        self.print_current_time_as_time_stamp()

    def update_time(self, time):
        self.time = time

    def print_current_time_as_time_stamp(self):
        time_array = math.modf(self.time)
        # print("print_current_time_as_time_stamp: " + str(self.time))
        day = int(time_array[1])

        #  Konvertering:
        hours = time_array[0] * 24
        # print("HOURS: " + str(hours))
        new_time_array = math.modf(hours)
        minutes = new_time_array[0] * 60
        # print(self.minute)
        print("Day: %d. Time: %02d.%02d" % (day, hours, minutes))




        #  Det här är bara min sparade kod från den första klockan. Lär kunna tar bort senare, men behåller ett tag pga orolig att något av det kan ha värde senare:

        # def add_to_time(self, total_time):  # total time är en float
        #     time_in_minutes = int(total_time * 60)
        #     self.set_clock(time_in_minutes)
        #     print("Simulation clock add_to_time() - är detta sluttiden?")
        #     self.print_current_time_as_time_stamp()
        #
        # def set_clock(self, minutes_to_add):
        #     self.convert_minutes_to_hour(minutes_to_add)
        #
        # def convert_minutes_to_hour(self, minutes):
        #     if (minutes + self.minute) < 60:  # Ändra så att den tar hänsyn till minuterna som finns nu
        #         self.minute += minutes
        #         return
        #     else:
        #         self.hour += 1
        #         minutes -= 60
        #         self.convert_minutes_to_hour(minutes)  # Rekursivt anrop om ett event tagit mer än två timmar
        #     self.convert_hours_to_day(
        #         self.hour)  # Kollar ifall den inkrementerade timmen gör att klockan passerat midnatt
        #
        # def convert_hours_to_day(self, hours):
        #     if hours < 24:
        #         return
        #     else:
        #         self.day += 1
        #         self.hour -= 24
