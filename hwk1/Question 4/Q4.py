import os
import time


def fathest_pair(nums):
    # to achive this purpose, we are actually
    # finding the min and the max value in this list
    min = max = nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
        elif nums[i] > max:
            max = nums[i]
        else:
            pass
    return min, max

# input the address of your dataset
path = 'D:\Rutgers/2nd Semester\DATA STRUCT & ALGS\Homework\hwk1\Question 4/hw1-1.data'
files = os.listdir(path)

time_all = []
len_all = []

for file in files:
    print(file)
    f = open(path + '/' + file)
    iter_f = iter(f)
    nums = []

    for num in iter_f:
        nums.append(num)

    start = time.perf_counter()
    fathest_pair(nums)
    end = time.perf_counter()

    len_all.append(len(nums))
    time_all.append(end-start)

print(len_all)
print(time_all)