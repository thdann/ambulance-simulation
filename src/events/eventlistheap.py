""" Input module description """
from math import log, ceil

class EventListHeap():
    """ Input class description """
    def __init__(self, num_patients):
        """ Input method description """
        event_list_length = 2 * num_patients

        self.list = [None for _ in range(event_list_length)]
        self.num_items = 0

    def add(self, new_event):
        """ Input method description """

        print('evenlistheap.py ==> class EventListHeap ==> def add')
        print('evenlistheap.py new event: ', new_event)

        self.list[self.num_items] = new_event

        current_index = self.num_items
        self.num_items = self.num_items + 1

        height = int(ceil(log(self.num_items, 2)))
        for _ in range(height):
            parent_index = int((current_index - 1) / 2)

            if self.list[parent_index].time > self.list[current_index].time:
                temp = self.list[parent_index]
                self.list[parent_index] = self.list[current_index]
                self.list[current_index] = temp
            else:
                return

            current_index = parent_index

    def next(self):
        """ Input method description """
        if self.num_items == 0:
            return None

        obj = self.list[0]
        self.num_items = self.num_items - 1
        self.list[0] = self.list[self.num_items]

        current_index = 0
        max_index = self.num_items - 1

        while 1:
            left_child_index = (2 * current_index) + 1

            if left_child_index > max_index:
                return obj

            right_child_index = (2 * current_index) + 2

            if right_child_index > max_index:
                if self.list[current_index].time > self.list[left_child_index].time:

                    temp = self.list[current_index]
                    self.list[current_index] = self.list[left_child_index]
                    self.list[left_child_index] = temp

                return obj

            if self.list[current_index].time > self.list[left_child_index].time:
                if self.list[left_child_index].time > self.list[right_child_index].time:
                    temp = self.list[current_index]
                    self.list[current_index] = self.list[right_child_index]
                    self.list[right_child_index] = temp
                    current_index = right_child_index

                else:
                    temp = self.list[current_index]
                    self.list[current_index] = self.list[left_child_index]
                    self.list[left_child_index] = temp
                    current_index = left_child_index

            elif self.list[current_index].time > self.list[right_child_index].time:
                temp = self.list[current_index]
                self.list[current_index] = self.list[right_child_index]
                self.list[right_child_index] = temp
                current_index = right_child_index

            else:
                return obj
        return obj

    def check(self):
        """ Input method description """
        max_index = self.num_items - 1
        for i in range(self.num_items):
            left_child_index = (2 * i) + 1
            right_child_index = (2 * i) + 2

            if left_child_index <= max_index:
                if self.list[left_child_index].time < self.list[i].time:
                    print("Invalid heap")
                    return False

            if right_child_index <= max_index:
                if self.list[right_child_index].time < self.list[i].time:
                    print("Invalid heap")
                    return False
        return True
