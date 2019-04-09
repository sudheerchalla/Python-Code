""" representation of dfs using stack"""
graph={ 'A':['B','C'],
        'B':[],
        'C':['D','E'],
        'D':['F'],
        'E':[],'F':[]}

def bfs(graph,s):
    visited=[]
    queue=[s]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue=queue+graph[node]
    return visited

print (bfs(graph,'A'))
