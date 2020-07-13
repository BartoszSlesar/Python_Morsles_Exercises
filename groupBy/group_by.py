def default(n):
    return n
def group_by(numbers ,key_func=default):
    dict = {}
    for number in numbers:
        dict.setdefault(key_func(number),[]).append(number)
    return dict
