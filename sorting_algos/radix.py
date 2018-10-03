def radix_sort(unsorted):
    output = []
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]

    for i in unsorted:
        tmp = i / placement
        buckets[int(tmp % RADIX)].append(i)
        if maxLength and tmp > 0:
            maxLength = False

    a = 0
    for b in range(RADIX):
        sub_bucket = buckets[b]
        for i in sub_bucket:
            unsorted[a] = i
            a += 1
    placement *= RADIX
    return unsorted
