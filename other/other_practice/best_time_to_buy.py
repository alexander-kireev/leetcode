



def best_time_to_buy(prices):
    
    profit = 0
    
    if len(prices) < 2:
        return profit
    
    lowest = prices[0]

    for i in range(1, len(prices)):
        possible_profit = prices[i] - lowest

        if possible_profit > profit:
            profit = possible_profit

        lowest = min(lowest, prices[i])

    return profit

    







prices = [7, 1, 5, 3, 6, 4]

print(best_time_to_buy(prices))