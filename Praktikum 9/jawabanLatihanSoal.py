def isPrime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True

import numpy as np

M = int(input("Masukkan M: "))
N = int(input("Masukkan N: "))

arr = np.empty((M, N), int)

for i in range(M):
    for j in range(N):
        arr[i][j] = int(input())
        
print(arr)

for i in range(M):
    for j in range(N):
        if isPrime(arr[i][j]) == True:
            arr[i][j] = 1
        else:
            arr[i][j] = 0

print(arr)
    

