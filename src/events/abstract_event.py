"""__author__: Johan"""

class AbstractEvent:
    """ Abstract event that all other events inherits """
    def __init__(self, event_time):
        """ Input method description """
        self.time = event_time

    def action(self):
        """ Input method description """
        raise NotImplementedError("Please implement Event.action")

    def __repr__(self):
        """ Input method description """
        return "<time: " + str(self.time) + ">"

    def __str__(self):
        """ Input method description """
        return "<time: " + str(self.time) + ">"