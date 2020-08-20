from collections import Counter

def removeDuplicateLetters(s):
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1

        if char in seen:    # if char in stack
            continue

        # 뒤에 붙일 문자가 남아있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)
    
    return "".join(stack)


if __name__ == "__main__":
    s = "bcabc"
    print(removeDuplicateLetters(s))   # "abc"
    s = "cbacdcbc"
    print(removeDuplicateLetters(s))   # "acdb"