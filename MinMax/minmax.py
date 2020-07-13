import typing
class minimum_maximum(typing.NamedTuple):
    min:int
    max:int
def minmax(args,*,key = lambda s:s):
    args = list(args)
    if not args:
        raise ValueError('')
    return minimum_maximum(
        min(args,key=key),
        max(args,key=key))
