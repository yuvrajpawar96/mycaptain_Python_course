def fibo():
    i = 0
    j = 1
    k = 0
    l = 1
    num = int(input("Enter range of series : "))
    while l < num:

        k = i + j
        print(i)
        print(j)
        print(k)
        l = l + 1
        i = j + k
        j = i + k


fibo()
