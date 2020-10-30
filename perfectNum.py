def perf(n):
    sum = 0
    arr = []
    for x in range(1, n):
        if n % x == 0:
            sum += x

    if sum == n:
        arr.append(sum)

    return arr


m = 1
v = int(input("Input your range: "))
while m < v:
    for i in range(len(perf(m))):
        print("Ok")
    m += 1
