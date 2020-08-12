def arrayPairSum(nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    
    return sum

if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    print(arrayPairSum(nums))