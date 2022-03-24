from dataclasses import replace
from os.path import dirname, join
from datetime import date

current_directory = dirname(__file__)
filepath = join(current_directory, "files/incoming_calls.txt")

def get_date_time_array():
    date_time_array = []
    file = open(filepath, "r")
    for line in file: 
        elements = line.split(" ")
        date = elements[0]
        ymd = date.split("-")
        # datearray.append(ymd)

        time = elements[1]
        hhmmss = time.split(":")

        ymd.append(hhmmss[0]) # Append hour
        ymd.append(hhmmss[1]) # Append minute

        date_time_array.append(ymd)
    
    return date_time_array

def get_day(): 
    day = []
    array = get_date_time_array()
    d0 = date(2020, 1, 1) # Startdatum, alla dagar ska jämföras mot denna
    
    for call in array:
        d1= date(int(call[0]), int(call[1]), int(call[2]))
        delta = d1-d0
        day.append(float(delta.days))
    return day

def get_time(): 
    time=[]
    array = get_date_time_array()
    
    for call in array: 
        hour_to_minutes = int(call[3])*60
        #print(hour_to_minutes)
        total_minutes= hour_to_minutes + int(call[4])
        minutes_of_day = float(total_minutes/1440)
        time.append(minutes_of_day)
    return time
    
def generate_call_list():
    list = []
    array = get_date_time_array()
    d0 = date(2020, 1, 1) # Startdatum, alla dagar ska jämföras mot denna
    
    for call in array:
        d1= date(int(call[0]), int(call[1]), int(call[2]))
        delta = d1-d0

        hour_to_minutes = int(call[3])*60
        total_minutes= hour_to_minutes + int(call[4])
        minutes_of_day = float(total_minutes/1440)
        result = float(delta.days) + minutes_of_day
        list.append(result)
    return list


call_list = generate_call_list()

for call in call_list:
    print(call)








