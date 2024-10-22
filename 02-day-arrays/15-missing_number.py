


def missing_number(nums):

    for i in range(1, len(nums)):
        if i not in nums:
            return i
        
def missing_number_optimal(nums):
  n = len(nums)
  expectedSum = n*( n + 1) // 2
  actualSum = sum(nums)
  return expectedSum - actualSum


nums = [3,0,1]
print(missing_number(nums))
print(missing_number_optimal(nums))

