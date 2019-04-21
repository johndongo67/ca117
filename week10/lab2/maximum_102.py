def maximum(a):
    if len(a) == 1:
        return a[0]
    else:
        largest = maximum(a[1:])
        large = a[0]
        if largest > large:
            large = largest
        return large
