import os
import time
import read_file


def insertionsort(nums, h=1):
    # here we need to indicate the start point
    exchange = 0

    for i in range(h):
        # create loop with step = h
        # and insertion sort
        for j in range(i, len(nums), h):
            bd = j
            # search for where our point should be
            # print('j:  ', j)
            while bd != i:
                # print(bd)
                if nums[bd] < nums[bd - h]:
                    exchange = exchange + 1
                    tmp = nums[bd - h]
                    nums[bd - h] = nums[bd]
                    nums[bd] = tmp
                    bd = bd - h
                else:
                    break

    return exchange


def merge(l, m, r, nums):
    exchange = 0
    # print('start')
    if l == r:
        return 0
    # devide the input sequence into two
    l_1 = l
    r_1 = m
    l_2 = m + 1
    r_2 = r

    aux = []
    l_pointer = l_1
    r_pointer = l_2
    while l_pointer <= r_1 and r_pointer <= r_2:
        #print(l_pointer, r_pointer)
        if nums[l_pointer] <= nums[r_pointer]:
            aux.append(nums[l_pointer])
            l_pointer = l_pointer + 1
        else:
            aux.append(nums[r_pointer])
            r_pointer = r_pointer + 1
            exchange = exchange + r_1 - l_pointer + 1

    # have the rest of the number in the aux
    if l_pointer > r_1:
        aux.extend(nums[r_pointer:r_2 + 1])
    else:
        #print(l_pointer,r_1+1)
        aux.extend(nums[l_pointer:r_1 + 1])
    '''
    print()
    print('aux: ', aux)
    print('ltor: ', nums[l:r+1])
    print('l-r: ', l, r)
    '''
    wb_p = l
    for aux_num in aux:
        nums[wb_p] = aux_num
        wb_p = wb_p + 1

    return exchange


def bot_up_mergesort(nums):
    exchange = 0
    size = 1
    while size < len(nums):
        #print(size)
        size = size * 2
        for i in range(int(len(nums) / size) + 1):
            # decide the merge boundry
            l = i * size
            r = min((i + 1) * size - 1, len(nums) - 1)
            m = l + int(size / 2) - 1
            #print(l, r)
            exchange = exchange + merge(l, m, r, nums)
            #print(nums)
            #print(i)
    return exchange


def KDT_dis(nums0, nums1):
    # we will use nums0's index resort nums1
    nums0_index = [0 for i in range(len(nums0))]
    for i in range(len(nums0)):
        nums0_index[nums0[i] - 1] = i + 1

    # print(nums0_index)

    nums1_resrt = [0 for i in range(len(nums1))]
    for i in range(len(nums1)):
        nums1_resrt[i] = nums0_index[nums1[i] - 1]

    # print(nums1_resrt)

    return insertionsort(nums1_resrt)


path_0 = 'D:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk2\sp_data\\0\\'
path_1 = 'D:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk2\sp_data\\1\\'

_0files = os.listdir(path_0)
_1fiels = os.listdir(path_1)

time_count = []
for (file0, file1) in zip(_0files, _1fiels):
    # read the file for two permutation
    num0_path = path_0 + file0
    num1_path = path_1 + file1
    nums0 = read_file.read_file(num0_path)
    nums1 = read_file.read_file(num1_path)
    print(file0)
    print(file1)

    t0 = time.perf_counter()
    res1 = KDT_dis(nums0, nums1)
    t1 = time.perf_counter()
    time_count.append(t1 - t0)

    print(res1)
    print(t1 - t0)

print(time_count)
