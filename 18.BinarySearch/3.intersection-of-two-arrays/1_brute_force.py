def intersection(nums1, nums2):
    result = set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)
    return result


if __name__ == "__main__":
    print(intersection([1,2,2,1], [2,2]))
    print(intersection([4,9,5], [9,4,9,8,4]))