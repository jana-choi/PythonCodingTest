import bisect

def twoSum(numbers, target):
    results = []
    for k, v in enumerate(numbers):
        expected = target - v
        i = bisect.bisect_left(numbers, expected, k+1)
        if i < len(numbers) and numbers[i] == expected:
            results.append([k+1, i+1]) 
    
    return results


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
    print(twoSum([2,3,6,7,9,11,15], 9))