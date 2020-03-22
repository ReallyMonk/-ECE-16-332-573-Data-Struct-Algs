def read_file():
    path = 'D:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk3\Q5\\select-data.txt'

    f = open(path, 'r')
    num_txt = f.readlines()

    nums = []
    for num in num_txt:
        nums.append(int(num))

    return nums
