



def capacity_to_ship_packages(weights, days):
    left = max(weights)
    right = sum(weights)
    res = right

    def capShip(cap):
        ships = 1
        currCap = cap
        for w in weights:
            if currCap - w < 0:
                ships += 1
                currCap = cap
            currCap -= w
        return ships <= days

    while left <= right:
        cap = (left + right) // 2
        if capShip(cap):
            res = min(res, cap)
            right = cap - 1
        else:
            left = cap + 1
    return res


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(capacity_to_ship_packages(weights, days))

