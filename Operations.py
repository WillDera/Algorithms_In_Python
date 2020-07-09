# L, denotes a given list eg [1, 2, 4], ['hello', 'hide' 'a', 'my name']
# p, denotes the position in L

# p must be an integer eg. 1, 2, 10, 3, 4 or 5

# FIRST(L) returns the first element in L
def FIRST(L: list):
    if L == []:
        return ("Provided list is empty")
    else:
        return ("%s is the first element in the provided List" % L[0])


# MAKENULL(L) makes L an empty list
def MAKENULL(L: list):
    if L == []:
        return ("Provided list is already null/empty")
    else:
        return ("Provided list has been made empty")


# RETRIEVE(p, L) returns the element at p in L
def RETRIEVE(p: int, L: list):
    if p < 0:
        return IndexError("LIST position cannot be negative")
    elif p <= len(L):
        return ("%s is the element at position %s in the provided List" % (L[p], p))
    else:
        return IndexError("Requested position not in range of %s" % L)


# NEXT(p, L) returns the next position after the provided p in L
def NEXT(p: int, L: list):
    temp_position = p + 1
    if p < 0:
        return IndexError("LIST position cannot be negative")
    elif len(L) > p:
        return ("Next position is %s" % temp_position)
    else:
        return IndexError("Provided position not in range of %s which has a length of %s" % (L, len(L)))


# PREVIOUS(p, L) returns the previous position before the provided p in L
def PREVIOUS(p: int, L: list):
    temp_position = (p) - 1
    if temp_position < 0:
        return IndexError("LIST position cannot be negative")
    elif p == 0:
        return ("0 is the first index of a LIST")
    else:
        return ("Previous position is %s" % temp_position)
