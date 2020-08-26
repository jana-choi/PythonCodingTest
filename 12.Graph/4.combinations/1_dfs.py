def combine(n, k):
    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
        
        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
    
    dfs([], 1, k)
    return results

if __name__ == "__main__":
    print(combine(4, 2))