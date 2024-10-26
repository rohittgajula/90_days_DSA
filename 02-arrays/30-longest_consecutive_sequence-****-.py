


def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0

    for n in nums:
        if (n-1) not in num_set:
            length = 0
            while (n+length) in num_set:
                length += 1
            longest = max(longest, length)
    return longest


nums = [100,4,200,1,3,2]
print(longest_consecutive_sequence(nums))