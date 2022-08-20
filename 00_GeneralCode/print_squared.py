from tkinter import N


def noOfLooping(m, n):
    if (m > n ):
        minValue = n
    else:
        maxValue = m

    if (minValue % 2 == 0):
        return minValue/2
    else:
        return (minValue+1)/2

def squarePrint(m, n):
    looping = noOfLooping(m, n)
    i = 0
    # j, k = i, i
    # l, x = j, k
    while i < looping:
        j = i
        while j < m - 1 - i:
            print(str(i) + '' + str(j), end=' ')
            j += 1
        k = i
        while k < m - 1 - i:
            print(str(k) + '' + str(j), end=' ')
            k += 1
        l = j
        while l > i:
            print(str(k) + '' + str(l), end=' ')
            l -=1
        x = k
        while x > i:
            print(str(x) + '' +str(l), end=' ')
            x -= 1
        i += 1

squarePrint(6, 4)
