from collections import defaultdict

def findItinerary(tickets):
    graph = defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)
    
    # dfs("JFK")
    dfs("A")

    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]

if __name__ == "__main__":
    case1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    case2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(findItinerary(case1))
    print(findItinerary(case2))

    case3 = [["A", "B"], ["B", "C"], ["B", "D"], ["C", "E"], ["D", "F"]]
    print(findItinerary(case3))