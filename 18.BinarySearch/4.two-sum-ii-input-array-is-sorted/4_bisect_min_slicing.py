import bisect

def twoSum(numbers, target):
    results = []
    for k, v in enumerate(numbers):
        expected = target - v
        nums = numbers[k+1:]
        i = bisect.bisect_left(nums, expected)
        if i < len(nums) and numbers[i+k+1] == expected:
            results.append([k+1, i+k+2]) 
    
    return results


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
    print(twoSum([2,3,6,7,9,11,15], 9))