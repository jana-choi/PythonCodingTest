def lengthOfLongestSubstring(s):
    max_length = 0
    for i, c in enumerate(s):
        substring = []
        substring.append(c)
        for t in s[i+1:]:
            if t in substring:
                break
            substring.append(t)
        max_length = max(max_length, len(substring))
    return max_length


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb")) # 3
    print(lengthOfLongestSubstring("bbbbb"))    # 1
    print(lengthOfLongestSubstring("pwwkew"))   # 3