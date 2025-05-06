def second_largestnumber(num):
    firstmaximum= max(num)
    print(firstmaximum)
    
    num.remove(firstmaximum)  # remove le chai list return gardaina thats why making new_list returns in none value
    secondlargest=max(num)
    
    print("the second largest number is: ",secondlargest)
num=[1,2,3,4,5]
second_largestnumber(num)
    
    