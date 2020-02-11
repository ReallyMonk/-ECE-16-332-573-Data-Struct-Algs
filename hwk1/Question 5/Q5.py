import time
import os


# pair sum to target number
def pair_sum(target, nums, head=0):
    tail = len(nums) - 1
    count = 0
    while head < tail:
        if nums[head] + nums[tail] == target:
            h_h = head
            t_t = tail
            while nums[h_h] == nums[h_h + 1] and h_h != len(nums):
                h_h = h_h + 1
            while nums[t_t] == nums[t_t - 1] and t_t != 0:
                t_t = t_t - 1
            count = count + (h_h - head + 1) * (tail - t_t + 1)
            head = h_h + 1
            tail = t_t - 1
        elif nums[head] + nums[tail] < target:
            head = head + 1
        elif nums[head] + nums[tail] > target:
            tail = tail - 1
    return count


# quadratic algorithm based on linear algorithm of zero-sum
def qua_three_sum(nums):
    count = 0
    for i in range(0, len(nums)):
        count = count + pair_sum(-nums[i], nums, i + 1)
    return count

# input the address of your dataset
path = 'D:\Rutgers/2nd Semester\DATA STRUCT & ALGS\Homework\hwk1\Question 5\hw1-1.data'
files = os.listdir(path)

time_all = []

for file in files:
    print(file)
    f = open(path + '/' + file)
    iter_f = iter(f)
    nums = []

    for num in iter_f:
        nums.append(int(num))
    nums.sort()
    #print(nums)

    # run and time record
    start = time.perf_counter()
    qua_three_sum(nums)
    end = time.perf_counter()

    whole_time = end - start
    time_all.append(whole_time)

print(time_all)