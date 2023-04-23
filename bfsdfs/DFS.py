from collections import defaultdict
# graph = {
#   'A' : ['B','C','D'],
#   'B' : ['E', 'F'],
#   'C' : ['F'],
#   'D' : [],
#   'E' : [],
#   'F' : []
# }

visited = []    
queue = []      

def bfs(visited, graph, node, target,cost):
    cost+=1
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0) 
        # print (s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                cost+=1;
                visited.append(neighbour)
                queue.append(neighbour)
                if neighbour == target:
                    print(*visited, sep="->")
                    print("Cost:",cost)
                    break
    if target not in visited:
        print('Target not found')

def dfs(visited, graph, node, target,cost):  
    if node not in visited:
        # print (node)
        cost+=1;
        visited.append(node)
        if node == target:
          print(*visited, sep="->")
          print("Cost:",cost)
          return
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, target, cost)

def comBFS():
    print("Breadth First Search")
    target = int(input('Enter Target Node: '))
    start= int(input('Enter Start Node: '))
    bfs(visited, graph, start, target,0)

def comDFS():
    print("Depth-First Search")
    target = int(input('Enter Target Node: '))
    start= int(input('Enter Start Node: '))
    dfs(visited, graph, start, target,0)
    if target not in visited:
        print('Target not found')

graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
 
def print_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
 
print("Here, A=1 B=2 C=3 D=4 E=5 F=6\n")
n=int(input("\nEnter Number of Node: "))
m=int(input("\nEnter Number of Edges: "))

print("Enter" , m , "Edges :\n")
for i in range(m):
    u, v = map(int, input().split())
    addEdge(graph,u,v)

print("\nAdjacency List of Entered Graph:")
print(print_edges(graph))
print("\nChoose Searching Technique:")
choice = input(" 1.BFS\n 2.DFS\n")
if choice == '1':
    comBFS()
elif choice == '2':
    comDFS()
else:
    print('\nEnter a Valid Option!')
    
