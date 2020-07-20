# L, denotes a given list eg [1, 2, 4], ['hello', 'hide' 'a', 'my name']
# p, denotes the position in L
# x, denotes an element

# p must be an integer eg. 1, 2, 10, 3, 4 or 5
temp_list = [1, "hello", "4", 6, 10]


# insert x at position p on L. if p=END(L) insert at the end of L;
# if L does not have position p, print an error message
def insert(x, p: int, L: list):
    if p < 0:
        return IndexError("LIST position cannot be negative")
    elif p <= len(L):
        L[p] = x
        return ("Element %s successfully inserted at index %s in the list" % (x, p))
    else:
        return IndexError("Requested position not in range of %s" % L)
