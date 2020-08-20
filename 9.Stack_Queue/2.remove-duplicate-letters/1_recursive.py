def removeDuplicateLetters(s):
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ""))
    return ""


if __name__ == "__main__":
    s = "bcabc"
    print(removeDuplicateLetters(s))   # "abc"
    s = "cbacdcbc"
    print(removeDuplicateLetters(s))   # "acdb"