# Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

# Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
# A user must wait at least 48 hours before retaking an exam.

import datetime

def can_retake(finish_time, current_time):
    fmt = "%Y-%m-%dT%H:%M:%S"
    dt_finish = datetime.datetime.strptime(finish_time, fmt)
    dt_current = datetime.datetime.strptime(current_time, fmt)

    diff = dt_current - dt_finish
    return diff >= datetime.timedelta(hours=48)

def evaluate_and_check(func_call_str, expected):
    # only expose known safe symbols
    result = eval(func_call_str)
    return result == expected

print(evaluate_and_check("can_retake(\"2026-03-23T08:00:00\", \"2026-03-25T14:00:00\")", True))
print(evaluate_and_check("can_retake(\"2026-03-24T14:00:00\", \"2026-03-25T10:00:00\")", False))
print(evaluate_and_check("can_retake(\"2026-03-23T09:25:00\", \"2026-03-25T09:25:00\")", True))
print(evaluate_and_check("can_retake(\"2026-03-25T11:50:00\", \"2026-03-23T11:49:59\")", False))