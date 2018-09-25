def repeated_word(input_string):
    checked = []
    try:
        input_string = input_string.lower()
        input_list = input_string.split(' ')
    except:
        return []
    for word in input_list:
        if word in checked:
            return word
        checked.append(word)
    return []
