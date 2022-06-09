#inserting Edge in undirected and weighted Graph


def add_node(v):
    global node_count
    if v in nodes:
        print(v," present in graph.")
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# inserting edge in undirected and weighted graph
def add_edge(v1,v2,cost):
    if v1 not in nodes:
        print(v1,"not present in graph.")
    elif v2 not in nodes:
        print(v2,"not present in graph.")
    else:
        indexV1 = nodes.index(v1)
        indexV2 = nodes.index(v2)
        graph[indexV1][indexV2] = cost
        graph[indexV2][indexV1] = cost

def print_graph():
    print("print graph in adjacency matrix form:")
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end = ' ')
        print()


nodes = []
graph = []
node_count = 0
print("before adding node:")
print("nodes :",nodes)
print("graph :",graph)

add_node("A")
add_node("B")
add_node("C")

print("After adding node:")
print("nodes :",nodes)
print("graph :",graph)

add_edge("A","B",10)
add_edge("B","C",5)

print_graph()

