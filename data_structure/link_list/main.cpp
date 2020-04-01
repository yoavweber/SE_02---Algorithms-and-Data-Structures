#include <cstdlib>
#include "./linkList.h"

using namespace std;

int main() {
    LinkList Yoav;

    Yoav.AddNode(3);
    Yoav.AddNode(5);
    Yoav.AddNode(7);

    Yoav.PrindList();

    Yoav.DeleteNode(3);

    Yoav.PrindList();

    return 1;
}