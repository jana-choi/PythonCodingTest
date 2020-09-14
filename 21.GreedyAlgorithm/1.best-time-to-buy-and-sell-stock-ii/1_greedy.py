def maxProfit(prices):
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            result += prices[i+1] - prices[i]
    return result


if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))