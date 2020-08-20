def isValid(s):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    
    return len(stack) == 0


if __name__ == "__main__":
    s = "()[]{}"
    print(isValid(s))   # True
    s = "{[]}"
    print(isValid(s))   # True
    s = "{([)"
    print(isValid(s))   # False