import math

def standard_dev(my_list):
    mean = sum(my_list)/len(my_list)
    
    for i in range(len(my_list)):
        diff = my_list[i] - mean
        my_list[i] = diff**2
    upper = sum(my_list)
    lower = len(my_list)
    result = math.sqrt(upper/lower)
    return result

        
# def standard_dev(my_list):
#     mean = sum(my_list)/len(my_list)
#     for i in range(len(my_list)):
#         diff = my_list[i] - mean
#         my_list[i] = pow(diff, 2)
#     upper = sum(my_list)
#     lower = len(my_list)
#     result = math.sqrt(upper/lower)
#     return round(result, 2)

N = int(input())
my_list = []

for i in range(N):
    x = int(input())
    my_list.append(x)

print(standard_dev(my_list))