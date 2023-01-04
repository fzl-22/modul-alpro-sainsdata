list_X = []
x = 1
while x != 0:
    x = int(input("Masukkan Data Baru: "))
    list_X.append(x)
    print(f"Output: MIN = {min(list_X)}, MAX = {max(list_X)}, MEAN = {round(sum(list_X)/len(list_X), 2)}")
    print()

print("SELESAI!")