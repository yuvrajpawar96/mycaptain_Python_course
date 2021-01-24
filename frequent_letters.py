def most_frequent():
    string_1=input("Enter your string :")
    dict={}
    for i in string_1:
        if i in dict:
            dict[str(i)]+=1
        else:
            dict[str(i)]=1
    print("output :")
    for k,v in dict.items():
                print(k,"=",v)


most_frequent()