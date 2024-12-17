# Find the missing number in a list of 1 to n natural numbers.


def missing_number(nums):
    for i in range(1, len(nums)):
        if i not in nums:
            return i


nums = [1,3,4,5,6]
print(missing_number(nums))

