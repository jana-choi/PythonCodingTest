def intersection(nums1, nums2):
    result = set()
    # 양쪽 모두 정렬
    nums1.sort()
    nums2.sort()
    i = j = 0
    # 투 포인터를 우측으로 이동하며 일치 여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    
    return result


if __name__ == "__main__":
    print(intersection([1,2,2,1], [2,2]))
    print(intersection([4,9,5], [9,4,9,8,4]))