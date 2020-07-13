import collections
def uniques(list_value):
        seen = set()
        seen_add = seen.add
        return (x for x in list_value if not (x in seen or seen_add(x)))

def uniques_only(iterable):
    seen = set()
    seen_unhashable = []
    #przpisuje funkcje do zmiennej bo to mniej obciążajace dla systemu
    seen_add = seen.add
    for item in iterable:
        if isinstance(item, collections.Hashable) and item not in seen:
            seen_add(item)
            yield item            
        elif not isinstance(item, collections.Hashable) and tuple(item) not in seen_unhashable:
             seen_unhashable.append(tuple(item))   
             yield item
  
        
#list_1 = ['a','b','c']
#list_2 = ['a','c','b']
#list_list = []
#list_list.append(list_1)
#list_list.append(list_2)
#print(list(uniques_only(list_list)))
#a = 2
#b = (2)

#print(isinstance(a, collections.Hashable))
