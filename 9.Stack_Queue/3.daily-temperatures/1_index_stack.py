def dailyTemperatures(T):
    answer = [0] * len(T)
    index_stack = []

    for idx, cur in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while index_stack and cur > T[index_stack[-1]]:
            last = index_stack.pop()
            answer[last] = idx - last
        index_stack.append(idx)
    
    return answer


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperatures(T))