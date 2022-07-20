class NotListError(Exception):
    pass

def move_to_end(informed_list):
    if type(informed_list) is not list:
        raise NotListError(f'{informed_list} is not a list ')

    if (len(informed_list) == 0):
        return informed_list

    temp = informed_list[0]
    informed_list.append(temp)
    informed_list.pop(0)

    return informed_list
