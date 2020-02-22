import random


data = [1 for i in range(1024)]
data.extend([11 for i in range(2048)])
data.extend([111 for i in range(4096)])
data.extend([1111 for i in range(1024)])

random.shuffle(data)


# since we already know the number and the amount of each value
aux = [0 for i in range(8192)]
ptr_1 = 0
ptr_11 = 1024
ptr_111 = 3072
ptr_1111 = 7168
for val in data:
    if val == 1:
        aux[ptr_1] = 1
        ptr_1 = ptr_1 + 1
    elif val == 11:
        aux[ptr_11] = 11
        ptr_11 = ptr_11 + 1
    elif val == 111:
        aux[ptr_111] = 111
        ptr_111 = ptr_111 + 1
    elif val == 1111:
        aux[ptr_1111] = 1111
        ptr_1111 = ptr_1111 + 1
    else:
        print('Error')

print(aux)