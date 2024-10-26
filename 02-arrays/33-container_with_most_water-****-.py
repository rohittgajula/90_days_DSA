


def container_with_more_water(height):
    
    result = 0
    left = 0
    right = len(height)-1

    while left < right:
        area = (right - left) * min(height[left], height[right])
        result = max(result, area)

        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            right -= 1
    return result


height = [1,8,6,2,5,4,8,3,7]
print(container_with_more_water(height))

