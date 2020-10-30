list1 = [1, 3, 2, 4]
list2 = [1, 3, 1, 5, 6]


def wrong_pair(sequence, k):
    if 0 < k < len(sequence) - 1:
        if sequence[k-1] >= sequence[k+1]:
            return k-1
    for i in range(k+1, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1


def strictlyIncreasing(sequence):
    j = wrong_pair(sequence, -1)
    if j == -1:
        return True
    if wrong_pair(sequence, j) == -1:
        return True
    if wrong_pair(sequence, j+1) == -1:
        return True
    return False


print(strictlyIncreasing(list2))
