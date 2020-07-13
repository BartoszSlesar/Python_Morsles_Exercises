def all_same(argument):
    val = iter(argument)
    check = object
    for a in val:
        if check != object and a != check:
            return False
        else:
            check = a
    return True
        

