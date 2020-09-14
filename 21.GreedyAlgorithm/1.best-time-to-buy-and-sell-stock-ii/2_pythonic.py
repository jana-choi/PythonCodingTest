def maxProfit(prices):
    # 0 보다 크면 무조건 합산
    return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))


if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))