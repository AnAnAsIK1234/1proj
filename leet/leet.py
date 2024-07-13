#default
def BinarySearch(mass, key):
    lo = 0
    hi = len(mass) - 1
    while (lo <= hi):
        mi = lo + (hi - lo) // 2
        if mass[mi] == key:
            return mi
        elif key < mass[mi]:
            hi = mi - 1
        else:
            lo = mi + 1
    return -1

#LowerBound
def BinarySearch(mass, key):
    lo = 0
    hi = len(mass) - 1
    while (lo <= hi):
        mi = lo + (hi - lo) // 2
        if mass[mi] == key:
            return mi
        elif key < mass[mi]:
            hi = mi - 1
        else:
            lo = mi + 1
    return -1

