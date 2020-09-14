def findContentChildren(g, s):  # g: child greed factor, s: cookie factor
    g.sort()
    s.sort()

    child_i = cookie_j = 0
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
    
    return child_i


if __name__ == "__main__":
    print(findContentChildren([1,3,2], [1,1]))
    print(findContentChildren([2,1], [3,1,2]))
    print(findContentChildren([2,1], [3]))