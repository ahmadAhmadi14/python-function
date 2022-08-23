class TwoSum():
   def __init__(self, listNumber, target):
      self.listNumber = listNumber
      self.target = target

   def solution(self):
      length = len(listNumber)

      for i in range(length):
         for j in range(i+1, length):
            sum = listNumber[i]+listNumber[j]
            if sum == target:
               return [i,j]


listNumber = [3,2,4,5,11]
target = 6
listNumberTarget = TwoSum(listNumber, target)
print(listNumberTarget.solution())

'''angka = [5,4,3,2,1]
target = 6
for x in angka:
   for y in angka:
      sum = x+y
      if sum == target:
         print(sum, target)'''