Queue allow you to handle data in order, and then get rid of it once you don’t need it anymore.
Quese are ideal for processing any data that should be handled in  order to how it was received.

In a queue, the first one to get in is the first one to go.

* data can only be insereted to the end of the queue
* data can only be read from the front of the line
* data can be only removed from the front of the line


The queue can be implemented using an array or linked list(get back to it after link list)****.



Analysis of Queue Operations(Array based Queue): 

1. Insert: O(1)
2. Delete: O(1)
3. Search: O(n)
4. Read: O(n)

Since you are only allowed to insert or remove data from the top of the stack, the delete and insert operation takes 1 step.

Practical Example:
In the queue.py I presented a simple queue class. I used the class to program the BFS algorithem in the graph hands in: '../graph/bfs.py'.

***explain how you used the queu in the data structure'