
import datetime
import time

def evaluate_and_check(func_call_str, expected):
    # only expose known safe symbols
    result = eval(func_call_str)
    return result == expected

def get_movie_night_cost(day, showtime, number_of_tickets):
    if day == "Tuesday":
        return f"${5 * number_of_tickets:.2f}"
    elif day in ["Friday", "Saturday", "Sunday"]:
        fmt = "%I:%M%p"
        dt_finish = time.strptime(showtime, fmt)
        dt_5pm = time.strptime("5:00pm", fmt)
        if dt_finish >= dt_5pm:
            return f"${12 * number_of_tickets:.2f}"
        else:
            return f"${10 * number_of_tickets:.2f}"
    elif day in ["Monday", "Wednesday", "Thursday"]:
        fmt = "%I:%M%p"
        dt_finish = time.strptime(showtime, fmt)
        dt_5pm = time.strptime("5:00pm", fmt)
        if dt_finish >= dt_5pm:
            return f"${10 * number_of_tickets:.2f}"
        else:
            return f"${8 * number_of_tickets:.2f}"
    return day



print(evaluate_and_check('get_movie_night_cost("Saturday", "10:00pm", 1)', "$12.00"))
print(evaluate_and_check('get_movie_night_cost("Sunday", "10:00am", 1)', "$10.00"))
print(evaluate_and_check('get_movie_night_cost("Tuesday", "7:20pm", 2)', "$10.00"))
print(evaluate_and_check('get_movie_night_cost("Wednesday", "5:40pm", 3)', "$30.00"))
print(evaluate_and_check('get_movie_night_cost("Monday", "11:50am", 4)', "$32.00"))
print(evaluate_and_check('get_movie_night_cost("Friday", "4:30pm", 5)', "$50.00")) 
print(evaluate_and_check('get_movie_night_cost("Tuesday", "11:30am", 1)', "$5.00"))