#Given an array of strings representing chess pieces you still have on the board.

def get_captured_value(pieces):
    total = 0
    #static dicts
    full_board = {'P': 8, 'R': 2, 'N': 2, 'B': 2, 'Q': 1, 'K': 1}
    piece_values = {'P': 1, 'R': 5, 'N': 3, 'B': 3, 'Q': 9, 'K': 0}
    
    #dicts to hold our counts in pieces array
    piece_counts = dict.fromkeys(['P', 'R', 'N', 'B', 'K', 'Q'], 0)
    piece_diffs = dict.fromkeys(['P', 'R', 'N', 'B', 'K', 'Q'], 0)

    #count up our input array into a dict
    for piece in pieces:
        piece_counts[piece] += 1

       #checkmate... check    
    if piece_counts.get('K') == 0:
        return "Checkmate"
    

    #Find differences for calc, piece_diffs will have number of captured pieces
    #We start with 8 pawns, if we have 3 in input array, 5 have been captured.
    #0 means we have all those pieces left.
    for key in piece_counts:
        piece_diffs[key] = full_board.get(key) - piece_counts.get(key)

    for key,value in piece_diffs.items():
        print("key",key,"val",value)
        print(value * piece_values.get(key))
        total += value * piece_values.get(key)
    return total

get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"])