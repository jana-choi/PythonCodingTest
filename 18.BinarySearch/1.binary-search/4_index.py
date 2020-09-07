import bisect

def search(nums, target):
    try:
        return nums.index(target)
    except:
        return -1
    

if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))