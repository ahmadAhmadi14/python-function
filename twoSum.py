def twoSum(listNumber, target):
    for i in range(len(listNumber)):
        for j in range(i+1, len(listNumber)):
            sum = listnumber[i]+listnumber[j]
            if sum == target:
              return [i,j]
            
        
    
    
listnumber = ((5, 7, 10, 50, 80))
target = 60
print(twoSum(listnumber, target))