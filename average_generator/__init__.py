def mean_of_three(arr):
    ''' takes a list of 3 numbers and returns the mean '''
    if len(arr) != 3:
        raise Exception("List of times must contain 3 times")   
    total = 0
    for i in arr:
        total += i
    return round(total/3, 2)


def average_of_five(arr):
    ''' takes a list of 5 numbers, sorts it and removes the highest and lowest, and averages it '''
    if len(arr) != 5:
        raise Exception("List of times must contain 5 times")
    arr.sort()
    arr.pop(len(arr) - 1)
    arr.pop(0)
    total = 0
    for i in arr:
        total += i
    return round(total/3, 2)


def average_of_twelve(arr):
    ''' takes a list of 12 numbers, sorts it and removes the highest and lowest, and averages it '''
    if len(arr) != 12:
        raise Exception("List of times must contain 12 times")
    arr.sort()
    arr.pop(len(arr) - 1)
    arr.pop(0)
    total = 0
    for i in arr:
        total += i
    return round(total/10, 2)