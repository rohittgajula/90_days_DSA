#  1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

# optimal solution. using sliding window sum, by adding next element and subtraction previous element
# sliding window helps not to recalculate entire subarray.
def numOfSubarrays(arr, k, threshold):
    count = 0
    window_sum = sum(arr[:k])
    target_sum = k * threshold                      # actual equation - (subset_sum / k) >= threshold

    if window_sum >= target_sum:
        count += 1
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        if window_sum >= target_sum:
            count += 1
    return count


# this is my solution ( brute force approach)
def num_of_subarrays(arr, k, threshold):
    
    l = 0
    r = k - 1
    count = 0

    while r < len(arr):
        subset = arr[l:r+1]
        subset_sum = sum(subset)
        if (subset_sum / k) >= threshold:
            count += 1
        l += 1
        r += 1
    return count


arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(num_of_subarrays(arr, k, threshold))
print(numOfSubarrays(arr, k, threshold))