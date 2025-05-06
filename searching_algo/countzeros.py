def counting_zeros(num):
    count = 0
    for i in range(0,len(num)):
        if num[i]==0:
            count = count +1
    print("the total number of zeros is :",count)
num=[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,0]
counting_zeros(num)