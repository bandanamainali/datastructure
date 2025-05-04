def is_sorted(num):
    for i in range(1,len(num)):
        
            if(num[i-1]>num[i]):
                print("not sorted")
                break
            print("sorted")
            
    
num=[10,20,30,40]
number=[20,30,10]
is_sorted(num)
is_sorted(number)
                