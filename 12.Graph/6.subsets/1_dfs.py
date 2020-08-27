from itertools import combinations

def subsets(nums):
    results = []
   
    def dfs(index, path):
        # 매번 결과 추가
        results.append(path)

        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])
    
    dfs(0, [])
    return results

if __name__ == "__main__":
    print(subsets([1,2,3]))