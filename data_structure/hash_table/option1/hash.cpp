#include <iostream>
#include <string>

#include "./hash.h"

using namespace std;

hashTable::hashTable()
{
    for(int i = 0; i < tableSize; i++)
    {
        HashTable[i] = new item;
        HashTable[i]->name="empty";
        HashTable[i]->drink="empty";
        HashTable[i]->next=NULL;
    }
}

int hashTable::Hash(string key)
{
    int index;
    int hash;

    for(int i = 0; i < key.length(); i++){
        hash += (int)key[i];
    }

    index = hash % tableSize;

    cout << index << endl;
    return index;
    
}

void hashTable::addItem(string name, string drink)
{
    int index = Hash(name);
    if(HashTable[index]->name == "empty"){
        HashTable[index]->name = name;
        HashTable[index]->drink = drink;
    }
    else{
        item* Ptr = HashTable[index];
        item* n = new item;
        n->name = name;
        n->drink = drink;
        n->next = NULL; // can I delete it?

        while(Ptr->next != NULL)
        {
            Ptr = Ptr->next;
        }

        Ptr->next = n;

    }
}