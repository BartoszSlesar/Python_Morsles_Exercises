from itertools import chain
def interleave(first_list,second_list):
         return chain.from_iterable(zip(first_list, second_list))

print(list(interleave([1, 2, 3, 4],[5, 6, 7, 8])))
