def selection_sort(unsorted):
    """ Finds the smallest item in the list, puts it in its place, finds the
    next smallest, puts it in its place. Passes through one time for every
    item in the list.
    """
    if type(unsorted) is not list:
        raise TypeError('Please make sure your input is a list!')
    for i in range(0, len(unsorted)):
        minimum = i
        for j in range(i+1, len(unsorted)):
            # check current versus current minimum
            if unsorted[minimum] > unsorted[j]:
                minimum = j
        # swaps minimum and the current
        unsorted[i], unsorted[minimum] = unsorted[minimum], unsorted[i]
    return unsorted
