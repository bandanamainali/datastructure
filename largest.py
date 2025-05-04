def largest_num(num):
    max=0
    for i in range(0,len(num)):
        
        
         for j in range(i+1,len(num)):
           
            if(num[j]>max):
              max=num[j]
    print("the max number is ", max)
num=[5,7,10,2,3,15]
largest_num(num)
        