#!/usr/bin/python
# -*- coding: utf-8 -*-
'''------------------------------------------------------------------
Name: DEBJYOTI PAUL
Roll Number:CS1418
Date of Submission:7/12/2014
Deadline date:  7/12/2014
Program description:UNDIRECTED GRAPH IN PYTHON
Acknowledgements:
--------------------------------------------------------------------'''
import Queue
from QuickUnion import QuickUnion


class UnDirectedGraph:

    def __init__(self, G=None, W=None):
        if G is None:
            self.G = {}
            self.W = {}
        elif type(G) is dict and W != None:#adjacency list input
            self.G = G
            self.W = W
        elif type(G) is list and W is None:#adjacency matrix input
            l = {}
            w = {}
            for i in len(G):
                l[i] = []
                w[i] = w
            index = 0
            for i in G:
                count = 0
                for j in i:
                    if j > 0:
                        l[index].append(count)
                        w[index].append(j)
                        l[count].append(index)
                        w[count].append(j)
                    count = count + 1
            index = index + 1
            self.G = l
            self.W = w
        elif type(G[0]) is tuple and W != None:# input as tuples of edges


            l = {}
            w = {}
            count = 0
            for i in G:
                if l.has_key(i[1]) == False:
                    l[i[0]] = []

                k = l.get(i[0])
                m = w.get(i[0])

                if k != None or k == []:
                    k.append(i[1])
                else:
                    k = [i[1]]
                l[i[0]] = k
                if m != None or m == []:
                    W[count]
                else:
                    m = [W[count]]
                w[i[0]] = m

                k = l.get(i[1])
                m = w.get(i[1])
                if k != None or k == []:
                    k.append(i[0])
                else:
                    k = [i[1]]
                l[i[1]] = k
                if m != None or m == []:
                    W[count]
                else:
                    m = [W[count]]
                    w[i[1]] = m

                count = count + 1
        else:
            print 'Error in input format'
            print 'input format must be:'
            print 'Format 1:'
            print 'A vetex dictionary with vertex as keys and list of adjacent vertices as list'
            print 'A weight dictionary with vertex as keys and list of weight corresponding to each adjacent vertices'
            print 'Format 2:'
            print 'A matrix representing the adjacency matrix in list of list format'
            print 'Format 3:'
            print 'A list of tuples, where each tuple is a two adjacent vertex: adjacent from the first to the second'
            print 'A list of weight corresponding to each vertex pair or edges'
            self.G = {}
            self.W = {}

    def has_edge(v1, v2):# check if it has edge

        return self.G.has_key(v1) == True and v2 in self.G[v1]

    def has_vertex(v):# check if it has vertex
        if self.G.has_key(v1):
            return self.G.has_key(v1)
        else:
            for i in self.G:
                if v in i:
                    return True
                return False

    def add_vertex(self, v=None):# add a single vertex
        if v != None:
            if v in self.G.keys():
                return 1
            self.G[v] = []
            self.W[v] = []
            return 0

    def add_vertices(self):# add multiple vertex

        VList = []
        print 'Enter the no of vetices'
        N = raw_input()
        for rowindex in range(0, int(N)):
            v = raw_input('Enter a vertex')
            if v in self.G.keys():
                print 'vetex' + v + 'already present in Graph'
                return 1
            self.add_vertex(v)
        return 0

    def add_edge(# add a single vertex
        self,
        v1=None,
        v2=None,
        w=None,
        ):
        if v1 == None or v2 == None:
            return 1
        elif v1 in self.G.keys() == False or v2 in self.G.keys() \
            == False:
            print 'vertex not present in Graph'
            return 1
        else:
            k = self.G.get(v1)
            m = self.W.get(v1)
            if k != None or k == []:
                self.G[v1].append(v2)
                self.G[v1] = k
            else:
                k = [v2]
                self.G[v1] = k
            if m != None or m == []:
                m.append(w)
            else:
                m = [w]
                self.W[v1] = m
            k = self.G.get(v2)
            m = self.W.get(v2)
            if k != None or k == []:
                self.G[v2].append(v1)
                self.G[v2] = k
            else:
                k = [v1]
                self.G[v2] = k
            if m != None or m == []:
                m.append(w)
            else:
                m = [w]
                self.W[v1] = m

    def add_edges(self):# add multiple edges
        print 'Enter the no of edges'
        E = raw_input()
        for rowindex in range(0, int(E)):
            print 'Enter the vetex of origin of the edge'
            v1 = raw_input()
            print 'Enter the vetex of termination of the edge'
            v2 = raw_input()
            print 'Enter the weight of the edge'
            w = raw_input()
            if v1 in self.G.keys() == False or v2 in self.G.keys() \
                == False:
                print 'vertices entered not in Graph'
                return 1
            k = self.G.get(v1)
            m = self.W.get(v1)
            if k != None or k == []:
                k.append(v2)
                self.G[v1] = k
            else:
                k = [v2]
                self.G[v1] = k
            if m != None or m == []:
                m.append(w)
                self.W[v1] = m
            else:
                m = [w]
                self.W[v1] = m
            k = self.G.get(v2)
            m = self.W.get(v2)
            if k != None or k == []:
                k.append(v1)
                self.G[v2] = k
            else:
                k = [v1]
                self.G[v2] = k
            if m != None or m == []:
                m.append(w)
                self.W[v2] = m
            else:
                m = [w]
                self.W[v2] = m
            print 'Do you want to exit? Y/N'
            c = raw_input()
            if c == 'Y' or c == 'y':
                break

    def delete_vertex(self, v=None):# delete a vertex
        if v != None:
            if self.G.has_key(v):
                del self.G[v]
                del self.W[v]

    def delete_vertices(self):# delete multiple vertices
        print 'Enter the no of vertices'
        V = raw_input()
        for rowindex in range(0, int(V)):
            print 'Enter the vetex of origin of the edge'
            v = raw_input()
            if self.G.has_key(v):
                del self.G[v]
                del self.W[v]

    def delete_edge(self, v1=None, v2=None):# delete an edge
        if v1 == None and v2 == None:
            return 1
        elif self.has_edge(v1, v2) == False:
            print 'vertex donot have any edge'
            return 1
        else:
            k = self.G.get(v1)
            m = self.W.get(v1)
            if k != None or k != [] and v2 in k:
                i = k.index(v2)
                k.remove(v2)
                self.G[v1] = k
                if m != None or m != []:
                    w = m[i]
                    m.remove(w)
                    self.W[v1] = m
            k = self.G.get(v2)
            m = self.W.get(v2)
            if k != None or k != [] and v2 in k:
                i = k.index(v1)
                k.remove(v1)
                self.G[v2] = k
                if m != None or m != []:
                    w = m[i]
                    m.remove(w)
                    self.W[v2] = m

    def delete_edges(self):# delete multiple edge
        print 'Enter the no of edges'
        E = raw_input()
        for rowindex in range(0, int(E)):
            print 'Enter the vetex of origin of the edge'
            v1 = raw_input()
            print 'Enter the vetex of termination of the edge'
            v2 = raw_input()
            self.delete_edge(v1, v2)

    def degree(self, v):# return a degree
        return len(self.G[v])

    def adjacency_matrix(self):
        count = 0
        AdjMat = []
        Map = {}
        for v in self.G.keys():
            Map[v] = count
            count = count + 1
            AdjMat.append([])
        for v in self.G.keys():
            AdjMat[Map[v]] = []
            for w in self.G.keys():
                if w != v:
                    if w in self.G[v]:
                        i = self.G[v].index(w)
                        j = self.W[v].__getitem__(i)
                        AdjMat[Map[v]].append(i)
                    elif v in self.G[w]:

                        i = self.G[w].index(v)
                        j = self.W[w].__getitem__(i)
                        AdjMat[Map[v]].append(i)
                    else:
                        AdjMat[Map[v]].append(0)
        return AdjMat

    def induced_subgraph(self, *ver):#induced subgraph
        l = {}
        w = {}

        for v1 in ver:
            for v2 in ver:
                print (v1, v2)
                if v1 != v2:
                    if self.G[v1].__contains__(v2):
                        if l.has_key(v1) == False:
                            l[v1] = []
                            w[v1] = []
                        k = l.get(v1)
                        if k == [] or k != None:
                            k.append(v2)
                            l[v1] = k
                        if l.has_key(v2) == False:
                            l[v2] = []
                        else:
                            k = [v2]
                            l[v1] = k
                        i = self.G[v1].index(v2)
                        j = self.W[v1].__getitem__(i)
                        m = w.get(v1)
                        if m == [] or m != None:
                            m.append(j)
                            w[v1] = m
                        else:
                            m = [j]
                            w[v1] = m
                else:

                    continue
        return (l, w)





			 #DFS (to visit a vertex v)
			# Mark v as visited.
			 #Recursively visit all unmarked
 			#	vertices w adjacent to v.





    def dfs(# depth first search auxilary function
        self,
        x,
        Marked,
        dfs_traverse,
        ):
        Marked[x] = True
        dfs_traverse.append(x)
        for w in self.G[x]:
            if Marked[w] == False:
                self.dfs(w, Marked, dfs_traverse)

    def depth_first_search(self, v):#depth first search main function
        Marked = {}
        dfs_traverse = []
        for i in self.G.keys():
            Marked[i] = False
        self.dfs(v, Marked, dfs_traverse)
        return dfs_traverse




#BFS (from source vertex s)
#Put s onto a FIFO queue, and mark s as visited.
#Repeat until the queue is empty:
 # - remove the least recently added vertex v
 # - add each of v's unvisited neighbors to the queue,
  #  and mark them as visited.
    def breadth_first_search(self, v):
        Marked = {}
        q = Queue.Queue()
        bfs_traverse = [v]
        q.put(v)
        for i in self.G.keys():
            Marked[i] = False
        Marked[v] = True
        while q.empty() is False:
            w = q._get()
            for x in self.G[w]:
                if Marked[x] is False:
                    q.put(x)
                    Marked[x] = True
                    bfs_traverse.append(x)
        return bfs_traverse
# utility function for shortest path
    def min_distance(
        self,
        dist,
        visited,
        Map,
        ):

        min = float('inf')
        min_index = self.G.keys()[0]
        for w in self.G.keys():
            if visited[Map[w]] == False and min >= dist[Map[w]]:
                min = dist[Map[w]]
                min_index = w

                return min_index
# auxillary function to return weight
    def get_weight(self, u, v):
        if v in self.G[u]:
            i = self.G[u].index(v)
            return self.W[u].__getitem__(i)
        else:
            return float('inf')
#get all paths between two vertices using Dijkestra's alforithm
#
#
# ********ALGORITH FOR Dijkstra USED ***********************
#1  function Dijkstra(Graph, source):
# 2      dist[source]  := 0                     // Distance from source to source
 #3      for each vertex v in Graph:            // Initializations
 #4          if v ≠ source
 #5              dist[v]  := infinity           // Unknown distance function from source to v
 #6              previous[v]  := undefined      // Previous node in optimal path from source
# 7          end if
 #8          add v to Q                         // All nodes initially in Q (unvisited nodes)
 #9      end for
#10
#11      while Q is not empty:                  // The main loop
#12          u := vertex in Q with min dist[u]  // Source node in first case
#13          remove u from Q
#14
#15          for each neighbor v of u:           // where v has not yet been removed from Q.
#16              alt := dist[u] + length(u, v)
#17              if alt < dist[v]:               // A shorter path to v has been found
#18                  dist[v]  := alt
#19                  previous[v]  := u
#20              end if
#21          end for
#22      end while
#23      return dist[], previous[]
#**********************************************************

    def shortest_path(self, u, v):
        if self.G.has_key(u) == False or self.G.has_key(u) == False:
            print 'vetex entered is not in Graph'
            return None
        dist = [0]
        visited = []
        Map = {}
        index = 0
        previous = {}
        for w in self.G.keys():
            Map[w] = index
            index = index + 1
            if w != u:
                dist.append(float('inf'))
            visited.append(False)
        for w in self.G.keys():
            x = self.min_distance(dist, visited, Map)
            visited[Map[x]] = True
            if self.G[w].__eq__(self.G[v]):
                return (previous, dist[Map[v]])
            for y in self.G[x]:
                alt = dist[Map[x]] + self.get_weight(x, y)
                if dist[Map[y]] > alt:
                    dist[Map[y]] = alt
                    previous[y] = x
 # get all path between two vertices
    def all_path(self, u, v):
        allpath = {}
        S = []
        index = 0
        Map = {}
        Marked = []
        for i in self.G.keys():
            Map[i] = index
            Marked.append(False)
            index = index + 1
        self.findpath(
            u,
            v,
            Marked,
            Map,
            allpath,
            S,
            )
        return allpath
# find path using depth first search
    def findpath(
        self,
        x,
        v,
        Marked,
        Map,
        allpath,
        S,
        ):

        if self.G[v].__eq__(self.G[x]):
            S.append(x)
            print S
            S.pop()
        else:

            Marked[Map[x]] = True
            S.append(x)
            for y in self.G[x]:

                if Marked[Map[y]] == False:
                    self.findpath(
                        y,
                        v,
                        Marked,
                        Map,
                        allpath,
                        S,
                        )
            Marked[Map[x]] = False
            if len(S) != 0:
                S.pop()
# minimum spanning tree using Kruskal's algorithm
#KRUSKAL(G):
#1 A = ∅
#2 foreach v ∈ G.V:
#3   MAKE-SET(v)
#4 foreach (u, v) ordered by weight(u, v), increasing:
#5    if FIND-SET(u) ≠ FIND-SET(v):
#6       A = A ∪ {(u, v)}
#7       UNION(u, v)
#8 return A
#9  end function
    def mst(self):
        l = []
        A = []
        Map = {}
        count = 0
        for w in self.G.keys():
            Map[w] = count
            count = count + 1
            for v in self.G[w]:
                l.append((self.get_weight(w, v), (w, v)))
        l.sort()
        q = QuickUnion(len(self.G.keys()))
        for i in l:
            ed = i[1]
            if q.find(Map[ed[0]], Map[ed[1]]) != True:
                q.union(Map[ed[0]], Map[ed[1]])
                A.append((ed[0], ed[1]))
        return A
# get the nieghbors of a particular vertex
    def neighbors(self, v):

        if self.G.has_key(v):
            outver = self.G[v]
            return outver
        else:
            return None
# connected components using kosaraju's algorith
#Phase1.  Compute reverse postorder in GR

#Phase2.  Run DFS in G, visiting unmarked vertices in reverse postorder of G
    def connected_components(self, v=None):
        Marked = {}
        for i in self.G.keys():
            Marked[i] = False
        count = 0
        id = {}
        for i in self.G.keys():
            if Marked[i] == False:
                self.depth_first_order(i, Marked, id, count)
                count = count + 1
        if v == None:
            return id
        else:
            if self.G.has_key(v):
                lst = []
                j = id[v]
                for i in self.G.keys():
                    if id[i] == j:
                        lst.append(i)
                return lst
            else:
                print 'vertex entered is not in graph'
                return None
# auxillary function for connected components
    def depth_first_order(
        self,
        x,
        Marked,
        id={},
        count=0,
        ):

        Marked[x] = True
        id[x] = count
        for w in self.G[x]:
            if Marked[w] == False:
                self.depth_first_order(w, Marked, id, count)
# check if the graph is strongly connected
    def is_connected(self):# check if strongly connected
        Connected = self.connected_components()
        id = 1
        for w in self.G.keys():
            if (Connected[w] and id) == 0:
                return False
            else:
                id = Connected[w]

        return True

# main function
print '*******UnDirected Graph*************'
print '>>> Enter the data to Initialize the Graph'
print '>>>input format must be:'
print '>>>Format 1:'
print '>>>A vetex dictionary with vertex as keys and list of adjacent vertices as list'
print 'A weight dictionary with vertex as keys and list of weight corresponding to each adjacent vertices'
print '>>>Format 2:'
print '>>>A matrix representing the adjacency matrix in list of list format'
print '>>>>Format 3:'
print '>>>A list of tuples, where each tuple is a two adjacent vertex: adjacent from the first to the second'
print 'A list of weight corresponding to each vertex pair or edges'
choice = input('Enter your choice: enter 1 or 2 or 3 >>> ')
if int(choice) == 1:
    AList = {}
    WList = {}
    print 'Enter the no of vetices'
    V = raw_input()
    for rowindex in range(0, int(V)):
        print 'Enter the ' + V + 'th vetex'
        v1 = raw_input()
        AList[v1] = []
        WList[v1] = []
    print 'Enter the no of edges'
    E = raw_input()
    for rowindex in range(0, int(E)):
        print 'Enter the vetex of origin of the edge'
        v1 = raw_input()
        print 'Enter the vetex of termination of the edge'
        v2 = raw_input()
        print 'Enter the weight of the edge'
        w = raw_input()

        if WList.has_key(v1):
            WList[v1].append(w)
        else:

            WList[v1] = [w]

        if AList.has_key(v1):
            AList[v1].append(v2)
        else:
            AList[v1] = [v2]



    dg = UnDirectedGraph(AList, WList)
elif int(choice) == 2:

    RList = []
    print 'Enter the no of vetices'
    V = raw_input()
    for rowindex in range(0, int(V)):
        RList.append([])
        for coloumnindex in range(0, int(V)):
            print 'Enter the weight of the edge between vertex: ' \
                + str(rowindex) + ' ' + str(coloumnindex)
            w = raw_input()
        RList[rowindex].append(int(w))

    dg = UnDirectedGraph(RList)
elif int(choice) == 3:

    AList[v1] = []
    WList[v1] = []
    print 'Enter the no of vetices'
    V = raw_input()
    for rowindex in range(0, int(V)):
        print 'Enter vetex ' + rowindex
        v1 = raw_input()

    print 'Enter the no of edges'
    E = raw_input()
    for rowindex in range(0, int(E)):
        print 'Enter the vetex of origin of the edge'
        v1 = raw_input()
        print 'Enter the vetex of termination of the edge'
        v2 = raw_input()
        print 'Enter the weight of the edge'
        w = raw_input()
        AList.append((v1, v2))
        WList.append(w)


    dg = UnDirectedGraph(AList, WList)
else:

    print 'wrong choice'
    exit(1)
while True:
    print '*******UnDirected Graph Utilities*************'
    print '1. Has vertex'
    print '2. Has Edge'
    print '3. Add vertex'
    print '4. Add Vertices'
    print '5. Add Edge'
    print '6. Add Edges'
    print '7. Delete Vertex'
    print '8. Delete Vertices'
    print '9. Delete Edge'
    print '10. Delete Edges'
    print '11. Degree'
    print '12. Adjacency Matrix'
    print '13. Induced Subgraph'
    print '14. Depth First Search'
    print '15. Breadth First Search'
    print '16. Shortest Path'
    print '17. All Path'
    print '18. Minimum Spanning Tree'
    print '19. Neighbors'
    print '20. Connected Component'
    print '21. Is Connected'
    print '22. Print Graph'
    print '23. Exit'
    print 'Please enter your choice'
    mchoice = input('Enter your choice >>> ')
    if int(mchoice) == 1:
        v = raw_input('Enter a vertex')
        print dg.has_vertex(v)
    elif int(mchoice) == 2:

        v1 = raw_input('Enter the source vertex')
        v2 = raw_input('Enter the destination vertex')
        print dg.has_edge(v1, v2)
    elif int(mchoice) == 3:

        v = raw_input('Enter a vertex')
        dg.add_vertex(v)
    elif int(mchoice) == 4:

        dg.add_vertices()
    elif int(mchoice) == 5:

        print 'Enter the vetex of origin of the edge'
        v1 = raw_input()
        print 'Enter the vetex of termination of the edge'
        v2 = raw_input()
        print 'Enter the weight of the edge'
        w = raw_input()
        dg.add_edge(v1, v2, w)
    elif int(mchoice) == 6:

        dg.add_edges()
    elif int(mchoice) == 7:

        print 'Enter the vertex to be deleted'
        v = raw_input()
        dg.delete_vertex(v)
    elif int(mchoice) == 8:

        dg.delete_vertices()
    elif int(mchoice) == 9:

        print 'Enter the vetex of origin of the edge'
        v1 = raw_input()
        print 'Enter the vetex of termination of the edge'
        v2 = raw_input()
        dg.delete_edge(v1, v2)
    elif int(mchoice) == 10:

        dg.delete_edges()
    elif int(mchoice) == 11:

        print 'Enter the vetex '
        v = raw_input()
        if dg.degree(v) != None:
            print 'degree'
            print str(dg.degree(v))
    elif int(mchoice) == 12:

        print str(dg.adjacency_matrix())
    elif int(mchoice) == 13:

        VList = []
        print 'Enter the no of vetices'
        N = raw_input()
        for rowindex in range(0, int(N)):

            VList.append(v)
        print str(dg.induced_subgraph(VList))
    elif int(mchoice) == 14:

        v = raw_input('Enter a vertex')
        print str(dg.neighbors(v))
    elif int(mchoice) == 15:

        v = raw_input('Enter a vertex')
        print str(dg.depth_first_search(v))
    elif int(mchoice) == 16:

        v = raw_input('Enter a vertex')
        print str(dg.breadth_first_search(v))
    elif int(mchoice) == 17:

        print str(dg.shortest_path(u, v))
    elif int(mchoice) == 18:

        u = raw_input('Enter a vertex')
        v = raw_input('Enter another vertex')
        print str(dg.all_path(u, v))
    elif int(mchoice) == 19:

        print str(dg.mst())
    elif int(mchoice) == 20:

        v = raw_input('Enter another vertex')
        print str(dg.connected_component(v))
    elif int(mchoice) == 21:

        print str(dg.is_connected())
    elif int(mchoice) == 22:

        print str(dg.G)
        print str(dg.W)
    elif int(mchoice) == 21:

        exit(0)
    else:

        print 'Wrong choice'


