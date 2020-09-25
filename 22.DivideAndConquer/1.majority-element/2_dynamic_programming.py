from collections import defaultdict

def majorityElement(nums):
    counts = defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)
        
        if counts[num] > len(nums) // 2:
            return num


if __name__ == "__main__":
    print(majorityElement([3,2,3]))
    print(majorityElement([2,2,1,1,1,2,2]))
    print(majorityElement([1,2,1,3,1,4,1,5]))