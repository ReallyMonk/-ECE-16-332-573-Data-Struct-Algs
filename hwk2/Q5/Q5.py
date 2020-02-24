from read_file import read_file
import random
import os
import time


def shellsort(nums, h=1):
    # here we need to indicate the start point
    comparision = 0

    for i in range(h):
        # create loop with step = h
        # and insertion sort
        for j in range(i, len(nums), h):
            bd = j
            # search for where our point should be
            # print('j:  ', j)
            while bd != i:
                # print(bd)
                comparision = comparision + 1
                if nums[bd] < nums[bd - h]:
                    tmp = nums[bd - h]
                    nums[bd - h] = nums[bd]
                    nums[bd] = tmp
                    bd = bd - h
                else:
                    break

    return comparision


class QS:
    def __init__(self):
        self.comparison = 0
        # self.layer = 0
        # random.shuffle(nums)
        # print(nums)
        # print(nums[0:5])

    def shellsort(self, nums, head, tail, h=1):
        # here we need to indicate the start point
        # comparision = 0

        for i in range(h):
            # create loop with step = h
            # and insertion sort
            for j in range(head, tail+1, h):
                bd = j
                # search for where our point should be
                # print('j:  ', j)
                while bd != i:
                    # print(bd)
                    # comparision = comparision + 1
                    if nums[bd] < nums[bd - h]:
                        tmp = nums[bd - h]
                        nums[bd - h] = nums[bd]
                        nums[bd] = tmp
                        bd = bd - h
                    else:
                        break

        return

    def QuickSort(self, nums, head, tail):
        # self.layer = self.layer+1
        # print(self.layer)
        # print(tail)
        if head >= tail:
            # print('do nothing')
            # self.layer = self.layer - 1
            # print(self.layer)
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

        # print('done')
        # self.layer = self.layer - 1
        # print(self.layer)
        return

    def partition(self, nums, head, tail):
        if head >= tail:
            return

        # set the mediam of 3 to be target
        m = int((head + tail) / 2)
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

    def QS_cut_Inser(self, nums, head, tail, cut):
        if tail - head + 1 <= cut:
            #print('shellsort', head, tail)
            self.shellsort(nums, head, tail)
            return

        pos = self.partition(nums, head, tail)
        self.QS_cut_Inser(nums, head, pos - 1, cut)
        self.QS_cut_Inser(nums, pos + 1, tail, cut)

        return


path = 'D:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk2\data\\'
files = os.listdir(path)
'''
times = []
times_shell = []

for file in files:
    print(file)
    nums = read_file(path + file)
    nums_shell = nums.copy()

    t0 = time.perf_counter()
    QSort = QS()
    QSort.QuickSort(nums, 0, len(nums) - 1)
    t1 = time.perf_counter()
    QSort.QS_cut_Inser(nums_shell, 0, len(nums)-1, 7)
    t2 = time.perf_counter()

    times.append(t1 - t0)
    times_shell.append(t2 - t1)

print(times)
print(times_shell)
'''

times = []
times_cut = []
cut_num = []

for i in range(1, 50, 1):
    cut_num.append(i)
    nums = read_file(path + 'data1.32768')
    nums_cut = nums.copy()

    QSort = QS()
    t0 = time.perf_counter()
    QSort.QuickSort(nums, 0, len(nums) - 1)
    t1 = time.perf_counter()
    QSort.QS_cut_Inser(nums_cut, 0, len(nums_cut) - 1, i)
    t2 = time.perf_counter()

    times.append(t1 - t0)
    times_cut.append(t2 - t1)

print(cut_num)
print(times)
print(times_cut)

