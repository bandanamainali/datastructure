def first_repeating_element(num):
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if num[i]==num[j]:
                return num[i]
    return None
element=[2, 5, 6, 3,  7, 8, 5]
result=first_repeating_element(element)
if result:
   print("First duplicate element:", result)
else:
    print("No duplicate element found.")
    
        
    