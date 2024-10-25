


def can_place_flower(flowerbed, n):
    
    f = [0] + flowerbed + [0]

    for i in range(1, len(f)-1):
        if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0



flowerbed = [1,0,0,0,1]
n = 1
print(can_place_flower(flowerbed, n))

