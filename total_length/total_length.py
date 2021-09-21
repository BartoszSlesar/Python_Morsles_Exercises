from operator import length_hint


def total_length(*args, use_hints=False) -> int:
    length = 0
    for n in args:
        try:
            length += len(n)
        except TypeError:
            hint = length_hint(n)
            if use_hints and hint:
                length += hint
            else:
                length += len([a for a in n])
    return length
