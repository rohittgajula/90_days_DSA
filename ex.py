

# my solution
def num_of_subarrays(arr, k, threshold):
    count = 0
    window_sum = sum(arr[:k])
    target_sum = k * threshold
    
    if window_sum >= target_sum:
        count += 1
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide the window
        if window_sum >= target_sum:
            count += 1
    
    return count

# Test the function
arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4
print(num_of_subarrays(arr, k, threshold))  # Output: 3
