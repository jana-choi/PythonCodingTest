def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    print(singleNumber([2,2,1]))
    print(singleNumber([4,1,2,1,2]))
    print(singleNumber([3,1,7,3,1]))