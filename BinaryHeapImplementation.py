class BinHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, current_node):
        parent = current_node // 2
        while parent > 0:
            if self.is_less(current_node, parent):
                self.swap(current_node, parent)

    def is_less(self, current_node, parent):
        return self.heap_list[current_node] < self.heap_list[parent]

    def swap(self, current_node, parent):
        tmp = self.heap_list[parent]
        self.heap_list[parent] = self.heap_list[current_node]
        self.heap_list[current_node] = tmp

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def perc_down(self, top_ele):
        while top_ele * 2 <= self.current_size:
            min_c = self.min_child(top_ele)
            if self.heap_list[top_ele] > self.heap_list[min_c]:
                tmp = self.heap_list[top_ele]
                self.heap_list[top_ele] = self.heap_list[min_c]
                self.heap_list[min_c] = tmp
            top_ele = min_c

    def min_child(self, top_ele):
        if top_ele * 2 + 1 > self.current_size:
            return top_ele * 2
        else:
            if self.heap_list[top_ele * 2 + 1] > self.heap_list[top_ele * 2]:
                return top_ele * 2
            else:
                return top_ele * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, alist):
        i = len(alist) // 2
        print(i)
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i = i - 1
            print(self.heap_list)


binary_h = BinHeap()
binary_h.build_heap([5, 4, 3, 2, 1])

print(binary_h)
