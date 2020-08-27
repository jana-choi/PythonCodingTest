from collections import defaultdict

def findItinerary(tickets):
    graph = defaultdict(list)
    # 그래프를 뒤집어서 구성
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    
    route = []
    def dfs(a):
        # 마지막 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop()) # O(1)
        route.append(a)
    
    dfs("JFK")

    # 다시 뒤집어 어휘 순 결과로
    return route[::-1]

if __name__ == "__main__":
    case1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    case2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(findItinerary(case1))
    print(findItinerary(case2))