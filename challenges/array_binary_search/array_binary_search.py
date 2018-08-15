def binary_search(arr, k):
    lowest = 0
    highest = len(arr)-1
    middle = (highest + lowest)//2

    if not len(arr):
        return - 1
    while(arr[middle] != k):
        if(lowest > highest):
            return -1
        elif(arr[middle] > k):
            highest = middle - 1
        elif(arr[middle] < k):
            lowest = middle + 1
        middle = (highest + lowest)//2

    return middle


print(binary_search([1, 2, 3, 4, 5, 6, 7], 2))
