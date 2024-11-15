


def search_2D_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    top = 0
    bottom = rows - 1
    while top < bottom:
        row = (top + bottom) // 2
        if target > matrix[0][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break

    if not (top <= bottom):
        return False
    
    row = (top + bottom) // 2
    left = 0
    right = cols - 1

    while left <= right:
        middle = (left + right) // 2
        if target > matrix[row][middle]:
            left = middle + 1
        elif target < matrix[row][middle]:
            right = middle - 1
        else:
            return True
    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search_2D_matrix(matrix, target))


