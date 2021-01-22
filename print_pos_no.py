def print_pos():
    List1 = []
    List2 = []
    num = int(input("Enter length of list1 : "))
    print("Enter elements of List1")
    for i in range(num):
        e = int(input())
        List1.append(e)
    num = int(input("Enter length of list2 : "))
    print("Enter elements of List2")
    for i in range(num):
        e = int(input())
        List2.append(e)
    print("Input List1 = ",List1)
    print("output : ")
    for i in List1:
        if(i > 0):
            print(i)
    print("Input List2 = ",List2)
    print("output : ")
    for i in List2:
        if (i > 0):
            print(i)


print_pos()
