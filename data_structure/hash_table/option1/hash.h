#include <string>

class hashTable {
    private:
        static const int tableSize = 10;
    
    struct item{
        string name;
        string drink;
        item* next;
    };  

    item* HashTable[tableSize];

    public:
        hashTable();
        int Hash(std::string key);
        void addItem(std::string name, std::string drink);
        int heshLength(int index);
};