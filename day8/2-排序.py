
import random
import time

class Sort:
    def __init__(self,n):
        """
        n是排序的数的数量
        """
        self.len = n
        self.arr = [0]*n
        self.random_data()

    def random_data(self):
        for i in range(self.len):
            self.arr[i] = random.randint(0,99)

    def partition(self,left,right):
        k = i = left
        for i in range(left, right):
            if self.arr[i] < self.arr[right]:
                self.arr[i],self.arr[k] = self.arr[k],self.arr[i]
                k+=1
        self.arr[right], self.arr[k] = self.arr[k], self.arr[right]
        return k

    def quick_sort(self,left,right):
        if left < right:
            pivot = self.partition(left,right)
            self.quick_sort(left,pivot-1)
            self.quick_sort(pivot+1,right)

    def adjust_max_heap(self,pos,arr_len):
        """
        把某个子树调整为大根堆
        """
        arr = self.arr
        dad = pos
        son = dad * 2 + 1
        while son < arr_len:
            if son + 1 < arr_len and arr[son] < arr[son+1]: # 判断右孩子存在且右孩子大于左孩子
                son+=1
            if arr[son] > arr[dad]:
                arr[dad],arr[son] = arr[son],arr[dad]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def heap_sort(self):
        """
        把列表调整为大根堆
        """
        for parent in range(self.len // 2 - 1, -1, -1):
            self.adjust_max_heap(parent,self.len)
        arr = self.arr
        arr[0],arr[self.len-1]=arr[self.len-1],arr[0] # 交换堆顶元素和最后一个元素
        for arr_len in range(self.len - 1, 1, -1):
            self.adjust_max_heap(0,arr_len)
            arr[0],arr[arr_len - 1] = arr[arr_len - 1],arr[0]

if __name__ == '__main__':
    my_sort = Sort(100000)
    start = time.time()
    print(my_sort.arr)
    my_sort.quick_sort(0,9)
    print(my_sort.arr)
    my_sort.heap_sort()
    print(my_sort.arr)
    end = time.time()
    print(f'总计用时{end - start}')