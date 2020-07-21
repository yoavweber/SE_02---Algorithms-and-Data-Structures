#include <cstdlib>
#include "./linkList.h"

using namespace std;

int main() {
    LinkList List;

    List.AddNode(3);
    List.AddNode(5);
    List.AddNode(7);

    List.PrintList();

    Yoav.DeleteNode(3);

    Yoav.PrintList();

    return 1;
}