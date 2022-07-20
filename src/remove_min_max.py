import math


class NotANumber(Exception):
    pass


class NotListError(Exception):
    pass


def remove_min_max(input_list):
    if type(input_list) != list:
        raise NotListError(f"{input_list} is not a list")

    for i in input_list:
        if type(i) is str or math.isnan(i):
            raise NotANumber(f"{i} is not a number")

    if len(input_list) <= 2:
        return []

    aux = []
    for i in input_list:
        aux.append(i)

    aux.remove(min(aux))
    aux.remove(max(aux))

    return aux
