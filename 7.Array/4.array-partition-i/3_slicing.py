def arrayPairSum(nums):
    return sum(sorted(nums)[::2])

if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    print(arrayPairSum(nums))