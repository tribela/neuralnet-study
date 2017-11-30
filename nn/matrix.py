import copy
import itertools


class Matrix():

    def __init__(self, y_size: int=None, x_size: int=None, init=None):
        if init is None:
            self.__arr = [[None] * x_size for _ in range(y_size)]

        if init is not None:
            y_size = len(init)
            x_size = len(init[0])
            self.__arr = [[None] * x_size for _ in range(y_size)]
            for y, x in itertools.product(range(y_size), range(x_size)):
                self[y, x] = init[y][x]

    @property
    def xsize(self):
        return len(self.__arr[0])

    @property
    def ysize(self):
        return len(self.__arr)

    @property
    def array(self):
        return copy.deepcopy(self.__arr)

    def __getitem__(self, item):
        y, x = item
        return self.__arr[y][x]

    def __setitem__(self, key, value):
        y, x = key
        self.__arr[y][x] = value

    def __mul__(self, other):
        assert isinstance(other, self.__class__)
        assert self.xsize == other.ysize

        newmat = Matrix(self.ysize, other.xsize)

        for y, x in itertools.product(range(self.ysize), range(other.xsize)):
            newmat[y, x] = sum(
                self[y, i] * other[i, x]
                for i in range(self.xsize)
            )

        return newmat