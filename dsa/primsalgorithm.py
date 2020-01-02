from collections import defaultdict
from queue import PriorityQueue as pq
graph=defaultdict(list)
def addedge(start,dest,weight):
	graph[start].append((dest,weight))
def lazyprims(source,numberofnodes):
	
	mstcost=0
	p1=pq()
	mstedge=[]
	visited=set()
	visited.add(source)
	for edge in graph[source]:
		node,weight=edge
		p1.put((weight,source,node))
	while not p1.empty() :
	
		k =p1.get()
	
		w,s,d=k
		mstedge.append((s,d))
		
		s=d
		mstcost+=w
		
		for edge in graph[s]:
		
			node,weight=edge
			if node in visited :
				continue
			p1.put((weight,d,node))
		
		visited.add(s)
	print("mst cost is {0}".format(mstcost))
	
	return mstedge
addedge(0,1,2)
addedge(0,3,1)
addedge(1,2,4)
addedge(2,3,3)

print("edges included in mst are {0}".format(lazyprims(0,4)))