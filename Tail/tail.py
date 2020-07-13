import collections
def tail(argument,n):
    if n<=0:
        return []
    last_n_val = collections.deque(maxlen=n)
    for val in argument:
        last_n_val.append(val)
    return list(last_n_val)
