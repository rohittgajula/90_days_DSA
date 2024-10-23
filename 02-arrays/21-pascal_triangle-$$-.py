


def pascals_triangle(numRows):
    result = [[1]]

    for i in range(numRows-1):
        temp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        result.append(row)
    return result


numRows = 5
print(pascals_triangle(numRows))

