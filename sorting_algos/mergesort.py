def mergesort(input_list):
    """ Takes in a list and splits it into halves recursively, then compares
    parts of the list to each other and merges them sorted into another list
    """
    output = []
    if len(input_list) > 1:
        mid = len(input_list) // 2
        first_half = input_list[:mid]
        second_half = input_list[mid:]
        sorted_first_half = mergesort(first_half)
        sorted_second_half = mergesort(second_half)
        i = 0
        j = 0
        while i < len(sorted_first_half) and j < len(sorted_second_half):
            if sorted_first_half[i] < sorted_second_half[j]:
                output.append(sorted_first_half[i])
                i += 1
            else:
                output.append(sorted_second_half[j])
                j += 1
        if i < len(sorted_first_half):
            output.extend(sorted_first_half[i:])
        else:
            output.extend(sorted_second_half[j:])
        return output
    else:
        return input_list
