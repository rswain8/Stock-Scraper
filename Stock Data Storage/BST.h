#ifndef BST_H
#define BST_H
#include "stock.h"

typedef struct Node
{
    struct Stock sto;
    struct Node* left;
    struct Node* right;
    int height; 
}Node;



Node* newNode(Stock);


int getHeight(Node*);
int getMax(int, int);
int getBal(Node*);

Node* rotateRight(Node*);
Node* rotateLeft(Node*);

Node* insertNodeByName(Node*, Stock);
Node* insertNodeByChange(Node*, Stock);
Node* insertNodeByTicker(Node*, Stock);





#endif
