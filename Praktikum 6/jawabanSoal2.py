def faktorial(n):
    if n > 0:
        return n*faktorial(n-1)
    else:
        return 1

def euler(k):
    if k >= 0:
        return 1/faktorial(k) + euler(k-1)
    else:
        return 0 
    
n = int(input("Masukkan input n: "))
resultEuler = euler(n)

print("Hasil aproksimasi bilangan Euler hingga {} suku adalah {}.".format(n, round(resultEuler, 48)))
# 2.718281828459042870349549048114567995071411132812
