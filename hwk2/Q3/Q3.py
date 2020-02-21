import time


def merge(l, m, r, nums):
    # print('start')
    if l == r:
        return
    # devide the input sequence into two
    l_1 = l
    r_1 = m
    l_2 = m+1
    r_2 = r

    aux = []
    l_pointer = l_1
    r_pointer = l_2
    while l_pointer <= r_1 and r_pointer <= r_2:
        #print(l_pointer, r_pointer)
        if nums[l_pointer] <= nums[r_pointer]:
            aux.append(nums[l_pointer])
            l_pointer = l_pointer+1
        else:
            aux.append(nums[r_pointer])
            r_pointer = r_pointer+1

    # have the rest of the number in the aux
    if l_pointer > r_1:
        aux.extend(nums[r_pointer:r_2+1])
    else:
        #print(l_pointer,r_1+1)
        aux.extend(nums[l_pointer:r_1+1])
    '''
    print()
    print('aux: ', aux)
    print('ltor: ', nums[l:r+1])
    print('l-r: ', l, r)
    '''
    wb_p = l
    for aux_num in aux:
        nums[wb_p] = aux_num
        wb_p = wb_p+1

    return 

def regular_mergesort(l, r, nums):
    # print('start')
    if l == r:
        return
    # devide the input sequence into two
    l_1 = l
    r_1 = int((l+r)/2)
    l_2 = int((l+r)/2)+1
    r_2 = r
    # deal with the left part
    regular_mergesort(l_1, r_1, nums)
    # deal with the right part
    regular_mergesort(l_2, r_2, nums)

    merge(l_1, r_1, r_2, nums)

    return
    

def bot_up_mergesort(nums):
    size = 1
    while size < len(nums):
        #print(size)
        size = size * 2
        for i in range(int(len(nums)/size)+1):
            # decide the merge boundry
            l = i*size
            r = min((i+1)*size-1, len(nums)-1)
            m = l+int(size/2)-1
            print(l,r)
            merge(l, m, r, nums)
            print(nums)
            print(i)



a = list(range(14,-1,-1))
print(a)

regular_mergesort(0,14,a)
print(a)


print(min(1, 2, 3))
