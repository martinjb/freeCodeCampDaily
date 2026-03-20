#Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.
def invert_matrix(matrix):
    status = False
    A = None
    B = None

    for arr in matrix:
        for element in arr:
            if A is None:
                A = element
                print("A", A)
            if B is None and element != A:
                B = element
                print("B", B)
            if A and B:
                status = True
                break
        if status:
            break
    
    for arr in matrix:
        for i, element in enumerate(arr):
            if element == A:
                arr[i] = B
            elif element == B:
                arr[i] = A
                
    print(matrix)    
    return matrix

invert_matrix([["a", "b"], ["a", "a"]]) 
#should return [["b", "a"], ["b", "b"]].
