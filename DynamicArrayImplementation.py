import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def get_item(self, k):
        if not(0 <= k < self.n):
            return IndexError('Index is out of bounds')

        return self.A[k]

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(self.capacity*2)

        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(self.new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return(new_cap*ctypes.py_object)()


arr = DynamicArray()
