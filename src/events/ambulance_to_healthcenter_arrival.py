from abstract_event import AbstractEvent

class AmbulanceToHealthCenter(AbstractEvent):
    def __init__(self, event_time, ambulace):
        super(AmbulanceToHealthCenter, self).__init__(event_time)
        self.ambulance = ambulace


