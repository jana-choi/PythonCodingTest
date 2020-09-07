import bisect
def intersection(nums1, nums2):
    result = set()
    nums2.sort()
    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
    
    return result


if __name__ == "__main__":
    print(intersection([1,2,2,1], [2,2]))
    print(intersection([4,9,5], [9,4,9,8,4]))