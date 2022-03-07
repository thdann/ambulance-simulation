from src.events.ambulance_to_healthcenter_arrival import AmbulanceToHealthCenterArrival


class AmbulanceToHealthCenterDeparture:
    properties = {
        'time': float,
        'health_center_lat': float,
        'health_center_long': float
    }
    def __init__(self):
        # Hämtar koordinater till health center

        self.time = None #Nån uträknad tid
        print("init AmbulanceToHealthCenterDeparture.")

    def action(self):
        print(self.__class__.__name__ + ":s actionmetod")
        next_event = AmbulanceToHealthCenterArrival
        next_event.action()