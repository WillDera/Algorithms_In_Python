# L, denotes a given list
# p, denotes the position in L

test_list = [1, 2, 3, 4]


# FIRST(L) returns the first element in L
def FIRST(L: list):
    return ("%s is the first element in the provided List" % L[0])


# MAKENULL(L) makes L an empty list
def MAKENULL(L: list):
    L = []
    return ("%s \nProvided list has been made empty" % L)


# RETRIEVE(p, L) returns the element at p in L
def RETRIEVE(p: int, L: list):
    return ("%s is element at position %s in the provided List" % (L[p], p))


def NEXT(p: int, L: list):
    if len(L) > p:
        temp_position = p + 1
        return ("Next position is %s" % temp_position)
    else:
        return ("Provided position not in range of %s" % L)


def PREVIOUS(p: int, L: list):
    temp_position = (p) - 1
    if temp_position <= 0:
        return ("0 is the first position of a List")
    else:
        return ("Provided positon of - %s is out of range of list - %s" % (p, L))


print(NEXT(6, [3, 4, 5, 6, 6, 7]))
