# L, denotes a given list
# p, denotes the position in L

test_list = [1, 2, 3, 4]


# FIRST(L) returns the first element in L
def FIRST(L):
    return L[0]


# MAKENULL(L) makes L and empty list
def MAKENULL(L):
    L = []
    return L


# RETRIEVE(p, L) returns the element at p in L
def RETRIEVE(p: int, L):
    return L[p]


def NEXT(p, L):
    if len(L) > p:
        temp_position = p + 1
        return temp_position
    else:
        for k, v in globals().items():
            if type(v) == list and v == L:
                return ("Position not in range of %s" % k)


def PREVIOUS(p, L):
    temp_postion = (p) - 1
    if temp_postion <= 0:
        return ("0 is the first index of a List")
    elif p > len(L):
        for k, v in globals().items():
            if type(v) == list and v == L:
                return ("Provided positon of index - %s is out of range of list - %s" % (p, k))
    else:
        return ("Previous index is %s" % temp_postion)


print(PREVIOUS(6, [1, 4, 5, 6, 7, 8, 9]))
