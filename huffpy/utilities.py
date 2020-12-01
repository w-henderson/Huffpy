"""Utility functions."""

def swap(_list, indexA, indexB):
    """Swap two items at two indeces in a list, and return the modified list."""

    temp = _list[indexA]
    _list[indexA] = _list[indexB]
    _list[indexB] = temp
    return _list

def bubbleSortDictToList(_dict, reverse=False):
    """Apply a bubble sort on the given dictionary (sorting by values) and return the sorted list."""

    _list = list(dict.items(_dict))

    for iteration in range(len(_list)):
        swaps = 0
        for index in range(len(_list) - 1 - iteration):
            if not reverse:
                if _list[index][1] > _list[index + 1][1]:
                    _list = swap(_list, index, index + 1)
                    swaps += 1
            else:
                if _list[index][1] < _list[index + 1][1]:
                    _list = swap(_list, index, index + 1)
                    swaps += 1
        if swaps == 0:
            return _list

def nodeBubbleSort(_list, reverse=True):
    """Apply a bubble sort on the list of nodes and return the sorted list."""

    for iteration in range(len(_list)):
        swaps = 0
        for index in range(len(_list) - 1 - iteration):
            if not reverse:
                if _list[index].value > _list[index + 1].value:
                    _list = swap(_list, index, index + 1)
                    swaps += 1
            else:
                if _list[index].value < _list[index + 1].value:
                    _list = swap(_list, index, index + 1)
                    swaps += 1
        if swaps == 0:
            return _list

def ndSum(_list):
    """
    Find the sum of everything in an n-dimensional list of nodes.
    Allows for different parts of the list to have differing dimensions, eg [1,2,[3,4,[5,6]]].
    """

    rv = 0
    for item in _list:
        if type(item) != list:
            rv += item[1]
        else:
            rv += ndSum(item)
    return rv

def ndIndex(_list, string):
    """Find the index of a string in an n-dimensional list."""

    moves = ""
    while True:
        if string in _list.left.containedChars:
            moves += "0"
            if _list.left.char == None:
                _list = _list.left
            else:
                break
        else:
            moves += "1"
            if _list.right.char == None:
                _list = _list.right
            else:
                break

    return moves

def crlfToLf(string):
    """Convert CRLF line endings to LF because the program doesn't like CRLF ones for some reason."""
    
    return string.replace("\r\n", "\n")

def splitEveryNChars(str, num):
    """Split a string every n characters."""

    return [ str[start:start+num] for start in range(0, len(str), num) ]