import math


def kokoEatingBananas(piles, h):
    left = 1
    right = max(piles)
    res = right

    while left <= right:
        k = (left + right) // 2

        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(float(pile) / k)
        if totalTime <= h:
            res = k
            right = k - 1
        else:
            left = k + 1
    return res

# brute force
def koko_eating_bananas(piles, h):
    speed = 1
    while True:
        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile / speed)
        if totalTime <= h:
            return speed
        speed += 1
    return speed


piles = [3,6,7,11]
h = 8
print(kokoEatingBananas(piles, h))
print(koko_eating_bananas(piles, h))