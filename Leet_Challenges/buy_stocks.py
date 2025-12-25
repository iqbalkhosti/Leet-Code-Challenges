
# this problem is trying to solve when is the best time to buy stock when given the prices of stocks in an array and their indices are the days that the prices are on

def buy_stocks(nums):

    min_price = float("inf")
    max_profit = 0

    for i in nums:
        if (i<min_price):
            min_price = i
#            print(min_price)        
        else:
            
            max_amount = i-min_price

            if(max_amount>max_profit):
                max_profit = max_amount
    return max_profit

price = [7, 1, 5, 3, 6, 4]

print(buy_stocks(price))

