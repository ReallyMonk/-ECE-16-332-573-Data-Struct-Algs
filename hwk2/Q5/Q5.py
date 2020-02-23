from read_file import read_file
import random
import os
import time


class QS:
    def __init__(self, nums):
        self.comparison = 0
        random.shuffle(nums)
        # print(nums)

    def QuickSort(self, nums, head, tail):
        # print(tail)
        if head >= tail:
            # print('do nothing')
            return
        # print('deal with', nums[head:tail+1])
        # do the partition
        pos = self.partition(nums, head, tail)
        # print(pos)
        # deal with the left part
        # print('left', head, pos-1)
        self.QuickSort(nums, head, pos - 1)
        # deal with the right part
        # print(pos)
        # print('right', pos+1, tail)
        self.QuickSort(nums, pos + 1, tail)

        return

    def partition(self, nums, head, tail):
        if head >= tail:
            return
        # set the mediam of 3 to be target
        m = int((head+tail)/2)
        if nums[head] >= nums[m]:
            tmp1 = head
        else:
            tmp1 = m
        
        if nums[m] >= nums[tail]:
            tmp2 = m
        else:
            tmp2 = tail

        if nums[tmp1] >= nums[tmp2]:
            mid = tmp2
        else:
            mid = tmp1
        
        # set midian to be head
        tmp = nums[head]
        nums[head] = nums[mid]
        nums[mid] = tmp

        tar = head
        head = head + 1
        while tail - head >= 0:
            # when find two values both on wrong side exchange
            if nums[head] > nums[tar] and nums[tail] < nums[tar]:
                # print('1exchange', nums[head], nums[tail])
                tmp = nums[tail]
                nums[tail] = nums[head]
                nums[head] = tmp
                head = head + 1
                tail = tail - 1
                continue

            # search for the value should be on the right side from left
            if nums[head] <= nums[tar]:
                head = head + 1

            # search for the value should be on the left side from right
            if nums[tail] >= nums[tar]:
                tail = tail - 1

        # since the target is always on the most left of the array,
        # we are going to change a smaller value with target
        # print('2exchange', nums[tar], nums[tail])
        tmp = nums[tail]
        nums[tail] = nums[tar]
        nums[tar] = tmp
        # print(nums)
        return tail


path = 'D:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk2\data\\'
files = os.listdir(path)

times = []

for file in files:
    print(file)
    nums = read_file(path + file)

    t0 = time.perf_counter()
    QSort = QS(nums)
    QSort.QuickSort(nums, 0, len(nums)-1)
    t1 = time.perf_counter()

    times.append(t1 - t0)
    
print(times)