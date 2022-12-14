# def faktorialIteratif(n):
#     result = 1
#     if n > 0:
#         for i in range(2, n + 1):
#             result = result*i
#         return result
#     elif n == 0:
#         return 1

def faktorialRekursif(n):
    if n > 0:
        return n*faktorialRekursif(n - 1)
    elif n == 0:
        return 1

N = int(input("Masukkan nilai N: "))
hasil = faktorialRekursif(N)
print("Nilai {}! = {}".format(N, hasil))
