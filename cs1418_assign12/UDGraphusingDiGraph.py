import Queue
from QuickUnion import QuickUnion
from DiGraph import DiGraph
'''
This is the main function for an undirected graph using methods in the DiGraph class
'''
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
        if AList.has_key(v2):
            AList[v2].append(v1)
        else:
            AList[v2] = [v1]
        if WList.has_key(v2):
            WList[v2].append(w)
        else:

            WList[v2] = [w]
        print 'Do you want to exit? Y/N'

    dg = DiGraph(AList, WList)
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

    dg = DiGraph(RList)
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
        AList.append((v2, v1))
        WList.append(w)
        WList.append(w)


    dg = DiGraph(AList, WList)
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
        dg.add_edge(v2, v1, w)
    elif int(mchoice) == 6:
    	print 'Enter the no of edges'
    	E = raw_input()
    	for rowindex in range(0, int(E)):
    		print 'Enter the vetex of origin of the edge'
        v1 = raw_input()
        print 'Enter the vetex of termination of the edge'
        v2 = raw_input()
        print 'Enter the weight of the edge'
        w = raw_input()
        dg.add_edge(v1, v2, w)
        dg.add_edge(v2, v1, w)
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
        dg.delete_edge(v2, v1)
    elif int(mchoice) == 10:
    	 print 'Enter the no of edges'
    	 E = raw_input()
    	 for rowindex in range(0, int(E)):
    		print 'Enter the vetex of origin of the edge'
    		v1 = raw_input()
    		print 'Enter the vetex of termination of the edge'
    		v2 = raw_input()

    		dg.delete_edge(v1, v2)
    		dg.delete_edge(v2, v1)

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


