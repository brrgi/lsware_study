# 3
# 0 2 3
# 2 0 1
# 3 1 0
from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:        #양쪽 간선 연결
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    result=0
    for node in mst:
        result+=node[0]

    return result

# (7, 'A', 'B')
myedges = [

]
a=int(input())
for i in range(a):
    flows=list(map(int, input().split()))
    for j in range(i+1, a):
        if flows[j]!=0:
            myedges.append((flows[j],str(i), str(j)))

print(prim('0', myedges)) #start_node, myedges