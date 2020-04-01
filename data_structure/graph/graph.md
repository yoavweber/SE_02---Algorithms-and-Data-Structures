summery:
    intro
    terminology
    type of graph
    implementation(hash table with linked list)

BFS:
    how it works
    time complexity

Dijkstra algorithem
    how it works
    time complexity

real use cases
    routing protocol

-----

A graph is a data structure that specializes in relationships, as it easily conveys how data is connected. Graph theory is a large and complicated topic, and this document cover the basic of it

Graph Terminology:
    Vertex: a node 
    Edge: line that connects two Vertices
    Adjacent Vertices: Two vertices are said to be adjacent if there is an edge (arc) connecting them.

Type of Graphs:

**directed vs undirected**
A graph can be directed, which mean that two vertices's are connected in a specific way. the fact that vertex A is connected to B doesn't mean that B is connected to A. Instegram is a practical example for that, the fact that a user following someone, doesn't mean that this someone following him
    &nbsp;
In undirected graph, the connection between A to B is the same. A practical example is adding a friend on Facebook, both user sharing the same connection.
        
**weighted**
In wighted graph, each node have an extra information about the edges, which represent the value of the edge. An example for wighted graph would be a graph that represent distance between citys.

    


## Representation
**Edge Lists**
This is a representation of two arrays, the first represent the edges in the graph. the second array represent the adjacent vertices(and the weight if the graph is weighted).
[[0,2],[0,4],[1,2],[3,4]]

Space: O(E)

Disadvantages:
    1. To find out about a spesific edge we would have to linar searcg through the edge list.
    2. All operetions are depened on the number of edges.

Advantage:
    1. Easy to implement 
    2. The total memory requirements of the edge list depends only on the number of edges in the graph. 

When should I use it:
    This representation is recommended for simple and small graphs
    
**Adjacency Metrices**
A metrix of all the vertices (V*V), where the connection is represented in 1 or 0(or of the weight if the graph is weighted)

[ [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
[0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 0, 1, 0, 0, 1, 0, 0] ]

Space: O(V^2)


Disadvantages:
    1. It takes a lot of space, since also the non-existing edges are represented by 0.
    2. If we want to find out which vertices are adjacent to a given vertex, you would have to go over all of the row.

Advantages: 
    1. Good for graph with many edges
    2. Adjacency matrix allow us to find out if an edge is present in constant time.

When should I use it:
    This representation is recommended for large graphs with a lot of connections.

**Adjacency lists**
A combination of adjacency matrices and edge lists. We have an array of all of the vertecies, and each element is another array with the adjacent vertices. This implemantetion could also made a hash table instead of an array of the vertecies.

[ [1, 6, 8],
  [0, 4, 6, 9],
  [4, 6],
  [4, 5, 8],
  [1, 2, 3, 5, 9],
  [3, 4],
  [0, 1, 2],
  [8, 9],
  [0, 3, 7],
  [1, 4, 7] ]

Space: O(V+E)

Disadvantages:
    1. It takes a lot of space, since also the non-existing edges are represented by 0.
    2. If we want to find out which vertices are adjacent to a given vertex, you would have to go over all of the row.

Advantages: 
    1. We can get to each vertex's adjacency list in constant time
    2. does not take a lot of space - 2E.

When should I use it:
    This representation is recommended for large graphs with a lot of connections.


​        
## Graph travers(BFS)
BFS is a way to travers a graph. it's usesed queues which keeps track of which vertices to process next.

steps:
1. visit each verex adjanent to the current vertex. add the visited adjacent to the queue.
2. if the current vertex has no unvisted adjancent, remove the next vertex from the queue and make it the current vertex.
3. repet step one on the next element in the queue

efficiency: O(V+E)

I have solve a challange using the BFS algorithm in bfs.py

## Dijkstra’s Shortest Path Algorithm
An algorithm to find the shortest path from a vertex to a desired location. 

steps:
1. We make the starting vertex our current vertex
2. We check all the vertices adjacent to the current vertex and calculate the weight from the start to all known location.
3. To determine the next current vertex, we find the cheapest unvisited known vertex that can be reached from our starting veryex.
4. we repeat those step until we reached, if we found a cheaper path between two vertecis we update it
