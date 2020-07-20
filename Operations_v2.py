import random
# L, denotes a given list eg [1, 2, 4], ['hello', 'hide' 'a', 'my name']
# p, denotes the position in L
# x, denotes an element
# p must be an integer eg. 1, 2, 10, 3, 4 or 5


# insert x at position p on L. if p=END(L) insert at the end of L;
# if L does not have position p, print an error message
def insert(x, p: int, L: list):
    print(L)
    if p < 0:
        return AttributeError("LIST position cannot be negative")
    elif p <= len(L):
        L.insert(p, x)
        return ("Element %s successfully inserted at index %s in the list" % (x, p))
        print(L)
    else:
        return IndexError("Requested position not in range of %s" % L)


# return the position of x in L; if x appears more than once return the position of the first appearance;
# if x does not exist in L print an error message and return return END(L)
def locate(x, L: list):
    print(L)
    if x in L:
        p = L.index(x)
        return ("Element found at index %s in %s" % (p, L))
    elif x not in L:
        end = END(L)
        return ("Element not found in the provided LIST \n%i" % end)
    else:
        return ("Something went wrong")


# return the element at position p on L; if L does not have postion p or
# if p=END(L), then print an error message
def retrieve(p: int, L: list):
    print(L)
    if p < 0:
        return IndexError("LIST position cannot be negative")
    elif p <= len(L):
        return ("%s is the element at position %s in the provided List" % (L[p], p))
    else:
        return ("Something went wrong")


# delete element at positon p on L; if p does not exist on L or if p=END(L), print an error message
def delete(p: int, L: list):
    print(L)
    if p < 0:
        return IndexError("LIST position cannot be negative")
    elif p <= len(L):
        del L[p]
        print(L)
    else:
        return ("Something went wrong")


# return the position following the last position on L
def END(L):
    p = len(L) + 1
    return p


# randomly generated list using insert(x,p,L)
random_List = []
for i in range(0, 6):
    x = random.randint(1, 50)
    insert(x, i, random_List)

print(random_List)
