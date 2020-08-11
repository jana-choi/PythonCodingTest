from itertools import combinations

def threeSum(nums):
    results = []
    num_comb = combinations(nums, 3)
    for nums in num_comb:
        if sum(nums) == 0:
            num_sort = sorted(nums)
            if num_sort not in results:
                results.append(num_sort)
    
    return results

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))