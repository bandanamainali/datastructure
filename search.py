def search_element(num,target):
    for i in range(0,len(num)):
        
        if num[i]==target:
            print("found the number in index:",i)
        # else:
        #     print("target not in the list")
num=[1,2,3,4]
target=4
search_element(num,target)
    