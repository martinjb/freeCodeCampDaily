from datetime import datetime, date
from datetime import time as dt_time
from time import strptime
def get_shadow(time):
    time = strptime(time, "%H:%M")
    noon = strptime("12:00", "%H:%M")
    am = strptime("06:00", "%H:%M")
    pm = strptime("18:00", "%H:%M")
    if time < noon and time >= am:
        direction = "ft west"
    elif time > noon and time < pm:
        direction = "ft east"
    elif time == noon:
        return "No shadow"
    elif time >= pm or time < am:
        return "No shadow" 
    time = dt_time(hour=time.tm_hour, minute=time.tm_min, second=time.tm_sec)
    noon = dt_time(hour=noon.tm_hour, minute=noon.tm_min, second=noon.tm_sec)
    dtime = datetime.combine(date.today(), time)
    dnoon = datetime.combine(date.today(), noon)
    hours = abs((dtime - dnoon).total_seconds()) / 3600
    if hours % 1 == 0:
        hours = int(hours)
    print(str(hours))
    shadow_ft = str((hours * hours * hours))
    print(shadow_ft, direction)
    return shadow_ft + direction

