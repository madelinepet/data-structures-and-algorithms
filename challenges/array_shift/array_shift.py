def insert_shift_array(array, value):
    first_half = array[:len(array)//2]
    second_half = array[len(array)//2:]
    return first_half + [value] + second_half
