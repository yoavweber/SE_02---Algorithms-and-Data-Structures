#ifndef LINKLIST_H
#define LINKLIST_H

class LinkList{
    private:
         typedef struct node{
          int data;
          node* next;  
        }* nodePtr;

        nodePtr head;
        nodePtr curr;
        nodePtr temp;

    public:
        LinkList();
        void AddNode(int addData);
        void DeleteNode(int delData);
        void PrindList();

};

#endif