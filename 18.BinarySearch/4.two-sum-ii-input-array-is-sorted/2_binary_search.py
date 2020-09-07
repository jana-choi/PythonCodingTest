def twoSum(numbers, target):
    results = []
    for k, v in enumerate(numbers):
        left, right = k + 1, len(numbers) - 1
        expected = target - v
        
        # 이진 검색으로 나머지 값 판별
        while left <= right:
            mid = left + ((right-left) // 2)
            if numbers[mid] < expected:
                left = mid + 1
            elif numbers[mid] > expected:
                right = mid - 1
            else:
                results.append([k+1, mid+1])
                break
    
    return results


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 9))
    print(twoSum([2,3,6,7,9,11,15], 9))