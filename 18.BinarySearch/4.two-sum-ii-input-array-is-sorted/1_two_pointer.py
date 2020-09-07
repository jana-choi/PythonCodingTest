def twoSum(numbers, target):
    results = []
    left, right = 0, len(numbers)-1
    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            results.append([left+1, right+1])
            left += 1
            right -= 1
    
    return results


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
    print(twoSum([2,3,6,7,9,11,15], 9))