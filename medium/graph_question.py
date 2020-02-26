def findTeams(file):
    graph = collections.defaultdict(list)

    for pair in file:
        first, second = pair 
        graph[fist].append(second)
        graph[second].append(first)

    teams = []
    visited = set()

    def dfs(curr, key):
        curr.add(key)
        visited.add(key)
        for teammate in graph[key]:
            if teammate not in visited:
                dfs(curr, teammate)
        if curr:
            teams.append(curr)

    for member in graph:
        dfs(set(), member)
    
    return team

    

