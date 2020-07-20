import random

# L, denotes a given list eg [1, 2, 4], ['hello', 'hide' 'a', 'my name']
# p, denotes the position in L
# x, denotes an element
# p must be an integer eg. 1, 2, 10, 3, 4 or 5


# insert x at position p on L. if p=END(L) insert at the end of L;
# if L does not have position p, print an error message
def insert(x, p: int, L: list):
    if p < 0:
        return AttributeError("LIST position cannot be negative")
    elif p <= len(L):
        print(L)
        L.insert(p, x)
        return ("Element %s successfully inserted at index %s in the list" % (x, p))
        print(L)
    else:
        return IndexError("Requested position not in range of %s" % L)


# return the position of x in L; if x appears more than once return the position of the first appearance;
# if x does not exist in L print an error message and return return END(L)
def locate(x, L: list):
    if L:
        if x in L:
            print(L)

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
    if p < 0:
        return IndexError("LIST position cannot be negative")
    elif p <= len(L):
        print(L)
        return ("%s is the element at position %s in the provided List" % (L[p], p))
    else:
        return ("Something went wrong")


# delete element at positon p on L; if p does not exist on L or if p=END(L), print an error message
def delete(p: int, L: list):
    if p < 0:
        return IndexError("LIST position cannot be negative")
    elif p <= len(L):
        print(L)
        del L[p]
        print(L)
    else:
        return ("Something went wrong")


# print the content of L in order of occurrence; print an error message if L is empty
def PRINT(L):
    if L:
        print(L)
    elif L == []:
        return ("Provided LIST is empty")
    else:
        return ("Something went wrong")


# return the position following the last position on L
def END(L):
    p = len(L) + 1
    return p


# get name of the random LIST we're about to create
class NamedObject:
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj

    def __getattr__(self, attr):
        if attr == 'name':
            return self.name
        else:
            return getattr(self.obj, attr)


# randomly create a unique list and get its name
random.seed(4)
unnamed = random.sample(range(10, 30), 5)
random_List = NamedObject('random_List', unnamed)


# driver function for our operations
def main():
    print("%s: %s" % (random_List.name, unnamed))


main()
