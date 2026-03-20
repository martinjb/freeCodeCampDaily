def largest_number(s):
    #normalize separators
    #s = s.replace("!", ",")
    #s = s.replace("?", ",")
    #s = s.replace(":", ",")
    #s = s.replace(";", ",")
    
    #this is faster for large strings
    translator = str.maketrans("!?:;", ",,,,")
    s = s.translate(translator)
    
    s_list = s.split(',')
    maximum = -2147483648
    c = 0
    while len(s_list) > 1:
        c = float(s_list.pop())
        print(c)
        if c > maximum:
            maximum = c
        print(maximum)
    c = float(s_list.pop())
    if c > maximum:
        maximum = c

    return maximum
#largest_number("1,2") 
#largest_number("4;15:60,26?52!0") 
#largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011") 
#largest_number("12;-50,99.9,49.1!-10.1?88?16") 