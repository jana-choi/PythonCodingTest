def combinationSum(candidates, target):
    results = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            results.append(path)
            return
        
        # 자신부터 하위 원소까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])
    
    dfs(target, 0, [])
    return results

def permutationSum(candidates, target):
    results = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            results.append(path)
            return
        
        # 처음부터 하위 원소까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], 0, path + [candidates[i]])
    
    dfs(target, 0, [])
    return results

if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))
    print(combinationSum([2,3,5], 8))

    print(permutationSum([2,3,6,7], 7))
    print(permutationSum([2,3,5], 8))