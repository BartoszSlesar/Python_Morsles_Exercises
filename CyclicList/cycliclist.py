from collections import UserList
from itertools import cycle
from itertools import islice


class CyclicList(UserList):
    def __init__(self, iterable):
        super().__init__(iterable)

    def __iter__(self):
        return cycle(self.data)

    def __getitem__(self, item):
        if isinstance(item, int):
            index = item % super().__len__()
            value = self.data[index]
        elif item.start is None and item.stop is None:
            value = self.data
        else:
            length = super().__len__()
            it = self.__check_slice(item)
            value = [self.data[i % length] for i in range(it.start, it.stop, it.step)]
        return value

    def __setitem__(self, key, value):
        index = key % super().__len__()
        self.data[index] = value

    def __check_slice(self, slice_item):
        start = slice_item.start if slice_item.start is not None else 0
        stop = slice_item.stop if slice_item.stop is not None else 0
        step = slice_item.step if slice_item.step is not None else 1
        return slice(start, stop, step)



# Trey solution
# class CyclicList(UserList):
#     def _slice_indices(self, obj):
#         start, stop = obj.start, obj.stop
#         if obj.step is not None:
#             raise ValueError("Step not supported")
#         if start is None:
#             start = 0
#         if stop is None:
#             stop = len(self) if start >= 0 else 0
#         return start, stop, 1
#
#     def __getitem__(self, index):
#         if isinstance(index, slice):
#             return [
#                 self[i]
#                 for i in range(*self._slice_indices(index))
#             ]
#         return self.data[index % len(self)]
#
#     def __setitem__(self, index, value):
#         self.data[index % len(self)] = value
