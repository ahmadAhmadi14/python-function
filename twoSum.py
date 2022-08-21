class TwoSum():
   def __init__(self, listNumber, target):
      self.listNumber = listNumber
      self.target = target

   def solution(self):
      length = len(listNumber)

      for i in range(length-1):
         for j in range(i+1, length):
            if listNumber[i]+listNumber[j] ==self.target:
               new_list = i, j
               return list(new_list)
      return -1         


listNumber = [3,2,4,5,11]
target = 6
listNumberTarget = TwoSum(listNumber, target)
print(listNumberTarget.solution())

