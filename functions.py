def com_filter(data: list, value):
    """
    The function takes as arguments the iterated sequence and the desired substring in the form of a string,
    implements the execution of the query in accordance with the "filter" command, searches for strings
    that include the desired substring. Returns the found elements in the original sequence as a list.
    """
    return filter(lambda x: value in x, data)


def com_map(data: list, value: int):
    """
    The function takes as arguments the iterated sequence and the index of the string element as an integer,
    implements the execution of the query in accordance with the command "mar", selects the string elements
    having the required index. Returns the elements found in the original sequence as a list.
    """
    res = []
    for line in data:
        for i, item in enumerate(line.split()):
            if i == value:
                res.append(item)
    return res


def com_unique(data: list):
    """
    The function takes an iterated sequence as an argument, implements the execution of the query in accordance
    with the "unique" command, selects unique elements of the original sequence. Returns the result as a list.
    """
    res = set(data)
    return list(res)


def com_limit(data: list, value: int):
    """
    The function takes an iterated sequence and an integer parameter as arguments, implements the execution
    of the query in accordance with the "limit" command, selects the first elements of the original sequence
    in a specified number. Returns the result as a list.
    """
    res = list()
    for i, item in enumerate(data):
        if i < value:
            res.append(item)
    return res


def com_sort(data:list, value: str):
    """
    The function takes as arguments an iterated sequence and a string parameter defining the sorting direction,
    implements the query execution in accordance with the "sort" command, sorts the elements of the original
    sequence in the specified direction. Returns the result as a list.
    """
    if value == "desc":
        return sorted(data, reverse=True)
    else:
        return sorted(data)

