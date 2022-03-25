class WaitingQueue:
    properties = {
        'waiting_queue': []
    }

    def __init__(self):
        self.waiting_queue = []

    def add_to_queue(self, event_to_add):
        self.waiting_queue.append(event_to_add)