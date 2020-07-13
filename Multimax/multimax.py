def defoult(val):
    return val
def multimax(values,key=defoult):
    if not values:
        return []
    val = list(values)
    max_val = max(val,key=key)
    if isinstance(max_val,str):
        return [x for x in val if len(x) == len(max_val)]
    else:
        return [x for x in val if x == max_val]
    
