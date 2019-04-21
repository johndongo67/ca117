def minimum(a):
    if len(a) == 1:
        return a[0]
    else:
        smallest = minimum(a[1:])
        small = a[0]
        if smallest < small:
            small = smallest
        return small
