# 프로그래머스 DFS/BFS 04 여행경로
# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# 제한사항
#     모든 공항은 알파벳 대문자 3글자로 이루어집니다.
#     주어진 공항 수는 3개 이상 10,000개 이하입니다.
#     tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
#     주어진 항공권은 모두 사용해야 합니다.
#     만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
#     모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
# 입출력 예
# tickets 	return
# [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] 	["ICN", "JFK", "HND", "IAD"]
# [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] 	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# 입출력 예 설명
# 예제 #1
# ["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.
# 예제 #2
# ["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만 ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.

def dfs(graph, N, key, footprint):
    if len(footprint) == N + 1:
        return footprint

    if key in graph:
        for idx, country in enumerate(graph[key]):
            graph[key].pop(idx)

            tmp = footprint[:]
            tmp.append(country)

            ret = dfs(graph, N, country, tmp)
            graph[key].insert(idx, country)

            if ret:
                return ret

def solution(tickets):
    answer = []
    graph = {}
    N = len(tickets)
    
    for st, ed in tickets:
        graph.setdefault(st, [])
        graph[st].append(ed)
        graph[st].sort()
        
    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer

tickets=[["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
print(solution(tickets))