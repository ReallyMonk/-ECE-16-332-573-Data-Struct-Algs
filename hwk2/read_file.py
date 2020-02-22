def read_file(path):
    f = open(path)
    iter_f = iter(f)
    # print(name)
    nums = []
    # insert the numbers from .txt file to nums list
    for num in iter_f:
        nums.append(int(num))
    
    return nums