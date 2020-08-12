import sys

def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    # 최소값과 최대값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))