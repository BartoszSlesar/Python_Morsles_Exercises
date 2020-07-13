INITVALUE = object()
def getValue(Dict,Key,sep='.',default=INITVALUE):
    keys = Key.split(sep)
    for k in keys:
        try:
            Dict = Dict[k]
        except KeyError:
            if default is not INITVALUE:
                return default
            else:
                raise
    return Dict

def pluck(Dict,*Key,sep='.',default=INITVALUE):
    values =  [getValue(Dict,k,sep,default) for k in Key]
    return tuple(values) if len(values)>1 else values[0]
    
    
    
        
data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
print(pluck(data, 'category.name', 'amount'))


