import bisect

def findContentChildren(g, s):  # g: child greed factor, s: cookie factor
    g.sort()
    s.sort()

    result = 0
    for i in s:
        # 이진 검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1

    return result


if __name__ == "__main__":
    print(findContentChildren([1,3,2], [1,1]))
    print(findContentChildren([2,1], [3,1,2]))
    print(findContentChildren([2,1], [3]))
    print(findContentChildren([3,4], [1]))