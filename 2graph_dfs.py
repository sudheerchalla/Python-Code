""" representation of dfs using stack"""

graph={ 'A':['B','C'], 'B':[], 'C':['D','E'], 'D':['F'], 'F':[], 'E':[]}


def dfs(graph,s):
    stack=[]
    visited=[]
    stack=[s]
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            stack=stack+graph[node]
    return visited

print (graph)
print (dfs(graph,'A'))




