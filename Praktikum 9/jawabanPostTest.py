def inputMatrix(baris, kolom):
    matrix = np.zeros((baris, kolom), dtype=int)
    for i in range(baris):
        for j in range(kolom):
            matrix[i][j] = int(input("Masukkan baris ke-{} kolom ke-{}: ".format(i, j)))
    return matrix
        

import numpy as np

barisM1 = int(input("Masukkan baris M1: "))
kolomM1 = int(input("Masukkan kolom M1: "))
        
matrixM1 = inputMatrix(barisM1, kolomM1)

barisM2 = int(input("Masukkan baris M2: "))
kolomM2 = int(input("Masukkan kolom M2: "))
        
matrixM2 = inputMatrix(barisM2, kolomM2)

isTranspose = True
if(barisM1 == kolomM2 and kolomM1 == barisM2):
    for i in range(barisM1):
        for j in range(barisM1):
            if matrixM1[i][j] != matrixM2[j][i]:
                isTranspose = False
                break
else:
    isTranspose = False
    
if isTranspose == True:
    print("Matrix M2 adalah transpose dari Matrix M1")
else:
    print("Matrix M2 bukan transpose dari Matrix M1")