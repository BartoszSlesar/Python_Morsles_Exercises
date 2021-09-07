from collections import deque


def window(args, n, *, fillvalue=None):
    if not n:  # if n is 0 or none, return empty list
        return []
    windowed = deque(maxlen=n)
    for element in args:
        windowed.append(element)
        if len(windowed) == n:
            yield tuple(windowed)
    if n > len(windowed):
        yield *tuple(windowed), *((fillvalue,) * (n - len(args)))

# a = list(window([1, 2, 3], 6))
# a = list(window([1, 2, 3], 4))
# print(a)
