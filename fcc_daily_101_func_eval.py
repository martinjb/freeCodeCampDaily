# This code is for testing the evaluation of a simple function call string.

def simple(a, b):
    return a + b

def evaluate_and_check(func_call_str, expected):
    # only expose known safe symbols
    result = eval(func_call_str)
    return result == expected

print(evaluate_and_check("simple(2, 3)", 5) == True)
