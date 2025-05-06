def floor_in_sorted_array(num,target):
    
    for i in range(0, len(num)):
        if num[i]<=target:
           new_list=[]
           new_list.append(num[i])
           
    floor_num=max(new_list)
    indexof=num.index(floor_num)
    print("the floor number is :",floor_num)
    print("the index of that number is :",indexof)
num= [1, 2, 8, 10, 10, 12, 19]
target=5
floor_in_sorted_array(num,target)