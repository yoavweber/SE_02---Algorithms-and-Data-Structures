A hash table is a list of paired values. It mainly used to gain quick access for a value using the key. In a hash table, the key and value have some significant association with one another.

## How does it work:

once the hash table recive a key value pair, it's take key and convert it using a function(hash function) to the location in the table where it's stored.

## Hash function:

As explaind above, the hash function determined where the value would be stored in the hash table. A good hash function should:

1. minimize collisions
2. uniform distribution of hash values- spearding the data over the hash table
3. easy to calculate

## Collision:

It happens that two keys have the same hash value, the name of this occurrence is collision. There are two common strategies to deal with a collision:

1. _Separate chaining_
   In Separate chaining, the elements are stored into a buckets. In case of collision, the elements are stored into sort of list.

2. _Open addressing_
   In open addressing, the elements are stored in the hash table itself. In case of collision, the element would be stored in the nearest memeroy location to the original location it should have been stored.

## Load Factor

To aviode collotion, it is recommended to create a hash table that would be bigger then the elements that are stored.
the ration between the stored item and the free space is called load factor. A good load factor would be in ration of 0.7: for 7 elements keep a space for 10 elements.

## Operations

1. Insert: O(1)/O(n)
2. Delete: O(1)/O(n)
3. Search: O(1)/O(n)
4. Read: O(1)/O(n)

The reason there are two option for the big O in the operations is beacuse the big O depend on the implementation of the hush function. In case there are no collusions all the operation would take O(1). In case there would be collision all of the operation would take O(n) when N is the number of elements that had collusion in on bucket of the hash table.

## Practical example

In the hashTable.cpp file I created basic hash table with simple hash function. When Collision is happening, I am solving them with Separate chaining, where the elements are stored in linked list.
