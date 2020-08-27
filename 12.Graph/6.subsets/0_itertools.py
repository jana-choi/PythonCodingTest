from itertools import combinations

def subsets(nums):
    results = []
    for i in range(len(nums)+1):
        # for c in list(map(list, combinations(nums, i))):
        #     results.append(c)
        results += [c for c in list(map(list, combinations(nums, i)))]
    return results

if __name__ == "__main__":
    print(subsets([1,2,3]))