from itertools import permutations

def permute(nums):
    return list(map(list, permutations(nums)))

if __name__ == "__main__":
    print(permute([1,2,3]))