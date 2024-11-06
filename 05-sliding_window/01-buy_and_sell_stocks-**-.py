# sliding window


def stocks(prices):
    
    l = 0       # buying
    r = 1       # selling
    max_profit = 0

    while r < len(prices):
        price_difference = prices[r] - prices[l]
        if price_difference > max_profit:
            max_profit = price_difference

        if prices[l] > prices[r]:
            l = r
        r += 1
    return max_profit


prices = [7,1,5,3,6,4]
print(stocks(prices))

