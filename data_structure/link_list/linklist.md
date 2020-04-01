Linked list are similar to an array, every application that you use an array can be used with linked list.

the different between those is that while array is located in the same chunk of memory, linked list are not. The elements are spreaded around the memory and each node contain its data and a pointer to the next node.

Unlike array, you can't access an index of an element in an array.

advantage:
Insertetion and Deletion can be in constent time(as along you are adding it to the begining). Unlike array, in which the insertion take n steps(since the process of shifting all of the elements takes n), in link list it takes only one steps.(reaching the element you want to insert would take n steps both in array or linked lists)



read:
O(n)

Travers:
O(n)

insert:
O(n) [O(1) at the end]
In case we would like to insart to the begining of the link list, it would take one step. beacuse all we need to do is to create new node and connect it to the HEAD node.

delete:
O(n) [O(1) at the end]

Although the time complexty of Insertion/Deletion in linked list is similar to an array, in some use cases it has big advantage over the array. In array the insertion/deletion operation takes N steps since it has to shift all of the element after the operetion is done. In case we would need to travers over a data structre and delete specefic element(for example, going over an email list and delete emails with a certian pattern), those opertion would take only one step.

real time uses:
Hashtables that use chaining to resolve hash collisions typically have one linked list per bucket for the elements in that bucket.(you can look at hash map data structure for refrence)

Implementation: I have created a link list class in c++ 

Doubly linked lists
Aother common data structre that can be made from link list is double linked list, which is a link list that has 2 pointers. One to the next node and one to the previous node. it is also keep track of the first and last node.