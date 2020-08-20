def removeDuplicateLetters(s):
    return "".join(sorted(set(s)))


if __name__ == "__main__":
    s = "bcabc"
    print(removeDuplicateLetters(s))   # "abc"
    s = "cbacdcbc"
    print(removeDuplicateLetters(s))   # "acdb"