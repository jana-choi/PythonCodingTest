def arrayPairSum(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    
    return sum

if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    print(arrayPairSum(nums))