def truncate_text(s):
    width = 0
    cutoff = 0
    for idx,char in enumerate(s):
        #print(idx,char,width)
        if width <= 47:
            if char == ' ':
                width += 2
                continue
            elif char == '.':
                width += 1
                continue
            if str(char).isupper():
                if char == 'I':
                    width += 1
                    continue
                elif char in ('J', 'L'):
                    width += 3
                    continue
                else:
                    width += 4
                    continue
            else:
                if char in ('i', 'l'):
                    width += 1
                    continue
                elif char in ('f', 'j', 'r', 't'):
                    width += 2
                    continue
                else:
                    width += 3
                    continue
        else:
            cutoff = idx
            break
    if width <= 50:
         return s
    if cutoff == 0:
        return s[:-3] + "..."
    else:
        return s[:cutoff-1] + "..."

truncate_text("The quick brown fox")
truncate_text("The silky smooth sloth")
truncate_text("THE LOUD BRIGHT BIRD")
truncate_text("The fast striped zebra")
truncate_text("The big black bear")