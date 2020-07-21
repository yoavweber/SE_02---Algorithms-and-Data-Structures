#include <iostream>
#include <list>
#include <cstring>
#include "../../link_list/linkList.h"

using namespace std;

class HashTable{
    private:
        static const int hashGroups = 10;
        list<pair<int,string>> table[hashGroups];

    public:
        bool isEmpty() const;
        int hashFunction(int key);
        void insert(int key, string value);
        void remove (int key);
        string searchTable(int key);
        void printTable();
};

bool HashTable::isEmpty() const{
    int sum{};
    for(int i{}; i<hashGroups;i++){
        sum += table[i].size();
    }

    if(!sum){
        return true;
    }
    return false;
}

int HashTable::hashFunction(int key){
    return key%hashGroups;
}

void HashTable::insert(int key, string value){
    int hashValue = hashFunction(key);
    auto& cell = table[hashValue];
    auto bItr = begin(cell);
    bool keyExists = false;
    for(; bItr != end(cell); bItr++) {
        if(bItr -> first == key) {
            keyExists = true;
            bItr -> second = value;
            cout << "[WARNING] key exists. Value replaces." << endl;
            break;
        }
    }
    if(!keyExists){
        cell.emplace_back(key,value);
    }
    return;

}

void HashTable::remove(int key){
    int hashValue = hashFunction(key);
    auto& cell = table[hashValue];
    auto bItr = begin(cell);
    bool keyExists = false;
    for(; bItr != end(cell); bItr++) {
        if(bItr -> first == key) {
            keyExists = true;
            bItr = cell.erase(bItr);
            cout << "[INFO] Item removed." << endl;
            break;
        }
    }
    if(!keyExists){
            cout << "[INFO] Item not found." << endl;
    }
    return;
}

void HashTable::printTable(){
    for(int i{}; i<hashGroups; i++){
        if(table[i].size() == 0) continue;
    
    auto bItr = table[i].begin();
    for(; bItr != table[i].end(); bItr++){
            cout << "key: " << bItr ->first << " Value: " << bItr->second << endl;
        }
    }
    return;
}

int main(){
    HashTable HT;
    LinkList Yoav;

    Yoav.AddNode(5);
    Yoav.AddNode(7);

    Yoav.PrindList();
    
    if(HT.isEmpty()) {
        printf("yes");
    }

    HT.insert(1,"test");
    HT.printTable();

    return 1;
}

