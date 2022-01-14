#include "BST.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>




void printTree(Node* root)
{
    
    if(root == NULL)
        return;
    

    printf("%s\n", root->sto.name);
    printTree(root->left);
    printTree(root->right);

}


int main(int argc, char* argv[])
{
    Stock sto[4];

    strcpy(sto[0].name, "Liam");
    strcpy(sto[0].ticker, "AAA");
    sto[0].price = 1000;
    sto[0].change = 0.15;
    sto[0].open = 1.15;
    sto[0].high = 10;
    sto[0].low = 20;
    sto[0].volume = 10000;

    strcpy(sto[1].name, "Reilly");
    strcpy(sto[1].ticker,"AAA");
    sto[1].price = 1000;
    sto[1].change = 0.15;
    sto[1].open = 1.15;
    sto[1].high = 10;
    sto[1].low = 20;
    sto[1].volume = 10000;

    strcpy(sto[2].name,"Andrew");
    strcpy(sto[2].ticker, "AAA");
    sto[2].price = 1000;
    sto[2].change = 0.15;
    sto[2].open = 1.15;
    sto[2].high = 10;
    sto[2].low = 20;
    sto[2].volume = 10000;

    strcpy(sto[3].name, "Kirill");
    strcpy(sto[3].ticker, "AAA");
    sto[3].price = 1000;
    sto[3].change = 0.15;
    sto[3].open = 1.15;
    sto[3].high = 10;
    sto[3].low = 20;
    sto[3].volume = 10000;


    Node* root = NULL;
    root = insertNodeByName(root, sto[1]);
    root = insertNodeByName(root, sto[0]);
    root = insertNodeByName(root, sto[3]);
    root = insertNodeByName(root, sto[2]);

   printTree(root);


    return 0;
}



























