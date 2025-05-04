def reverse_list(num):
    new_list=[]
    for i in range(len(num)-1,-1,-1):
        
        new_list.append(num[i])
    print(new_list)
num=[3,5,11,22,9]
reverse_list(num)
        
        