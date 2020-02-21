import time
import read_file
import os


def shellsort(nums, h):
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


# shell sort record
s_t_1 = []
s_t_3 = []
s_t_7 = []
s_t_all = []
s_cp_1 = []
s_cp_3 = []
s_cp_7 = []
s_cp_all = []

# insertion sort record
i_t = []
i_cp = []

# read file from datasets
path = 'D:\Rutgers/2nd Semester\DATA STRUCT & ALGS\Homework\hwk2\data/'
files = os.listdir(path)

for file in files:
    print(file)
    num_path = path + file

    shellnums = read_file.read_file(num_path)
    insertionnums = read_file.read_file(num_path)

    # loop for shell sort
    t0 = time.perf_counter()
    cp7 = shellsort(shellnums, 7)
    t1 = time.perf_counter()
    cp3 = shellsort(shellnums, 3)
    t2 = time.perf_counter()
    cp1 = shellsort(shellnums, 1)
    t3 = time.perf_counter()

    time1 = t1 - t0
    time2 = t2 - t1
    time3 = t3 - t2
    total_shell_t = time1 + time2 + time3
    total_shell_comp = cp1 + cp3 + cp7

    s_cp_1.append(cp1)
    s_cp_3.append(cp3)
    s_cp_7.append(cp7)
    s_cp_all.append(total_shell_comp)
    s_t_1.append(time3)
    s_t_3.append(time2)
    s_t_7.append(time1)
    s_t_all.append(total_shell_t)

    # loop for insertion sort
    it0 = time.perf_counter()
    cp_inser = shellsort(insertionnums, 1)
    it1 = time.perf_counter()
    inser_time = it1 - it0
    i_cp.append(cp_inser)
    i_t.append(inser_time)

    print('end')

print(s_t_1)
print(s_t_3)
print(s_t_7)
print(s_t_all)
print(s_cp_1)
print(s_cp_3)
print(s_cp_7)
print(s_cp_all)

print(i_cp)
print(i_t)