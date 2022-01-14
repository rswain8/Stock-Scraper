#include "BST.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

Node* newNode(Stock sto)
{
    Node* temp = (Node*)malloc(sizeof(Node));

    strcpy(temp->sto.name, sto.name);
    strcpy(temp->sto.ticker, sto.ticker);
    temp->sto.price = sto.price;
    temp->sto.change = sto.change;
    temp->sto.open = sto.open;
    temp->sto.high = sto.high;
    temp->sto.low = sto.low;
    temp->sto.volume = sto.volume;
    temp->height = 1;    
    return temp;
}


int getHeight(Node* root)
{
    if (root == NULL)
        return 0;

    return (root->height);

}

int getMax(int x, int y)
{
    if(x > y)
        return x;
    else if(x < y)
        return y;
}

Node* rotateRight(Node* node)
{
    Node* temp = node->left;
    Node* temp2 = temp->right;
    
    temp->right = node;
    node->left = temp2;

    node->height = 1 + getMax(getHeight(node->left), getHeight(node->right));
    temp->height = 1 + getMax(getHeight(temp->left), getHeight(temp->right));


    return temp;
}


Node* rotateLeft(Node* node)
{
    Node* temp = node->right;
    Node* temp2 = node->left;

    temp->left = node;
    node->right = temp2;
    
    node->height = 1 + getMax(getHeight(node->left), getHeight(node->right));
    temp->height = 1 + getMax(getHeight(temp->left), getHeight(temp->right));


    return temp;
}

int getBal(Node* node)
{
    if(node == NULL)
        return 0;

    return (getHeight(node->left) - getHeight(node->right));
    
    
}

Node* insertNodeByName(Node* node, Stock sto)
{
    int balance = 0;

    if(node == NULL)
        return newNode(sto);
    
    if(strcmp(node->sto.name, sto.name) > 0)
        node->left = insertNodeByName(node->left, sto);

    else if(strcmp(node->sto.name, sto.name) < 0)
        node->right = insertNodeByName(node->right, sto);
    else
        return node;

     node->height = 1 + getMax(getHeight(node->left), getHeight(node->right));

     balance = getBal(node);


    if(balance > 1 && strcmp(node->sto.name, node->left->sto.name) > 0)
        return rotateRight(node);

    if(balance < -1 && strcmp(node->sto.name, node->right->sto.name) < 0)
        return rotateLeft(node);

    if(balance > 1 && strcmp(node->sto.name, node->left->sto.name) < 0)
    {
        node->left = rotateLeft(node->left);
        return rotateRight(node);
    }

    if(balance < -1 && strcmp(node->sto.name, node->right->sto.name) > 0)
    {
        node->right = rotateRight(node->right);
        return rotateLeft(node);

    }


    return node;

}
















