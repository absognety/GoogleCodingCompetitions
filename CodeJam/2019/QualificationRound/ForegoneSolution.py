def foregone(n,t):
    for num in range(1,n):
        if '4' not in str(num):
            num2 = n - num
            if '4' not in str(num2):
                return " ".join(["Case #{}".format(t+1),str(num),str(num2)])

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N = int(input())
        print (foregone(N,tcase))