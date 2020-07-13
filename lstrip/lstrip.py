import itertools
def lstrip(list_obj,compare):
   if callable(compare):
      return itertools.dropwhile(compare, list_obj)
   else:
      return itertools.dropwhile(lambda n:n==compare, list_obj)
    
