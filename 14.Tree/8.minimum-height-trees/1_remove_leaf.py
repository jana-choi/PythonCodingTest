from collections import defaultdict

def findMinHeightTrees(n, edges):
    if n <= 1:
        return [0]

    # 양방향 그래프 구성
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    
    # 첫 번째 리프 노드 추가
    leaves = []
    for i in range(n + 1):
        if len(graph[i]) == 1:
            leaves.append(i)
        
    # 루트 노드만 남을 때까지 반복 제거
    while n > 2:
        n -= len(leaves)
        new_leaves = []

        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        
        leaves = new_leaves
    
    return leaves


if __name__ == "__main__":
    print(findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
    print(findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    print(findMinHeightTrees(10, [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]))