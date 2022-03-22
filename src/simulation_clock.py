class SimulationClock:
    properties = {
        'day': int,  # TODO: Går att göra dessa till typ key/value pairs i en array
        'hour': int,
        'minute': int,
        'recent_stop_time_day': int,
        'recent_stop_time_hour': int,
        'recent_stop_time_minute': int
    }

    def __init__(self):
        self.day = 0  # None
        self.hour = 1  # None
        self.minute = 1  # None

    def set_start_time(self, day, time_hour, time_minute):
        self.day = day
        self.hour = time_hour
        self.minute = time_minute
        print("Simulation clock set_start_time()")
        self.print_current_time()

    def set_stop_time(self, total_time):  # total time är en float, den totala tiden för en kedja
        time_in_minutes = int(total_time * 60)
        self.set_clock(time_in_minutes)
        print("Simulation clock add_to_time() - är detta sluttiden?")
        self.print_current_time()

    def set_clock(self, minutes_to_add):
        self.convert_minutes_to_hour(minutes_to_add)

    def convert_minutes_to_hour(self, minutes):
        if (minutes + self.minute) < 60:  # Ändra så att den tar hänsyn till minuterna som finns nu
            self.minute += minutes
            return
        else:
            self.hour += 1
            minutes -= 60
            self.convert_minutes_to_hour(minutes)  # Rekursivt anrop om ett event tagit mer än två timmar
        self.convert_hours_to_day(self.hour)  # Kollar ifall den inkrementerade timmen gör att klockan passerat midnatt

    def convert_hours_to_day(self, hours):
        if hours < 24:
            return
        else:
            self.day += 1
            self.hour -= 24

    def convert_driving_time_to_minutes(self, driving_time):
        # Not implemented yet
        return

    def print_current_time(self):
        print("Day: %d. Time: %02d.%02d" % (self.day, self.hour, self.minute))
