import math


class float_range(object):

    def __init__(self, stop, start=None, step=1):
        self.stop = stop
        self.current = stop if start is not None else 0
        self.__diff = self.current
        self.start = start
        self.step = step

    def __len__(self):
        n = self.stop if self.start is None else self.start
        v = math.ceil(n / self.step)
        result = abs(v - self.__diff)
        return int(result)

    def __getitem__(self, i):
        len = self.__len__()
        if isinstance(i, slice):
            start, stop, step = i.indices(len)
            new_start = start * self.step + self.stop
            new_stop = stop * self.step + self.stop
            new_step = step * self.step
            return float_range(new_start, new_stop, new_step)
        if len <= i or (i < 0 and (abs(i) > len)):
            raise IndexError("range object index out of range")
        if self.start is None:
            value = 0 if i >= 0 else self.stop
            return value + i
        else:
            if i >= 0:
                return self.stop + (self.step * i)
            else:
                index = len + i
                return self.__getitem__(index)

    def __iter__(self):
        return self

    def __next__(self):
        n = self.current
        if self.step < 0 and self.start > self.stop:
            raise StopIteration
        if (self.start is None and n < self.stop) or (self.start is not None and n < self.start):
            self.current += self.step
            return n
        elif (self.start is not None and self.start < self.stop) and n > self.start:
            self.current += self.step
            return n
        else:
            self.current = self.stop if self.start != 0 else self.start
            raise StopIteration


# my_range = float_range(0.5, 7, 0.75)
r = float_range(0.5, 7, 0.75)
print(list(r[0:2]))
# print(len(floater))
# for a in floater:
#     print(a)
