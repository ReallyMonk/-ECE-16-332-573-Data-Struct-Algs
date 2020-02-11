import time
import os


# solution one for 3-sum problem
def three_sum_1(nums):
    print('1start')
    count = 0
    for i in range(0, len(nums)):
        print('s1:', i)
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                    count = count + 1
                    continue
    print('1end')
    return count


# solutoin two for 3-sum problem
def three_sum_2(nums):
    # print('2start')
    count = 0
    nums.sort()
    for i in range(0, len(nums) - 2):
        # print('s2:', i)
        for j in range(i + 1, len(nums) - 1):
            # initialize binary search
            head = j + 1
            tail = len(nums) - 1
            while head <= tail:
                k = int((head + tail) / 2)
                if nums[i] + nums[j] + nums[k] == 0:
                    # check if we have any other k with same value
                    a = b = k
                    while nums[a] == nums[a - 1] and a != 0:
                        a = a - 1
                    while nums[b] == nums[b + 1] and b != len(nums):
                        b = b + 1
                    count = count + (b - a + 1)
                    break
                elif nums[i] + nums[j] + nums[k] < 0:
                    head = k + 1
                    continue
                elif nums[i] + nums[j] + nums[k] > 0:
                    tail = k - 1
                    continue
    #print('2end')
    return count

# input the address of your dataset
path = 'D:/Rutgers/2nd Semester/DATA STRUCT & ALGS/Homework/hwk1/Question 1/hw1-1.data'
files = os.listdir(path)

N = []
t1 = []
t2 = []
timing = [N, t1, t2]

for file in files:
    f = open(path + "/" + file)
    iter_f = iter(f)
    print(file)
    nums = []
    # insert the numbers from .txt file to nums list
    for num in iter_f:
        nums.append(int(num))

    # record time here
    start = time.perf_counter()
    # code run here
    # 1st solution
    three_sum_1(nums)
    time1 = time.perf_counter()
    # 2nc solution
    three_sum_2(nums)
    time2 = time.perf_counter()
    # record time
    last_time1 = time1 - start
    last_time2 = time2 - time1
    N.append(len(nums))
    t1.append(last_time1)
    t2.append(last_time2)

    # save time result into files
    wpath = 'D:/Rutgers/2nd Semester/DATA STRUCT & ALGS/Homework/hwk1/Question 1/res/'
    fw1 = open(wpath + 'time1.txt', 'a')
    fw1.write(str(last_time1) + '\n')
    fw1.close()
    fw2 = open(wpath + 'time2.txt', 'a')
    fw2.write(str(last_time2) + '\n')
    fw2.close()


