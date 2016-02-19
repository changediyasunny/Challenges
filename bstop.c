#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int count = 0;

struct node
{
    char key;
    struct node *left, *right;
};
  
struct node *newNode(char item)
{
    struct node *temp =  (struct node *)malloc(sizeof(struct node));
    temp->key = item;
    temp->left = temp->right = NULL;
    return temp;
}
  
// A utility function to do inorder traversal of BST
void inorder(struct node *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        printf("%c \n", root->key);
        inorder(root->right);
    }
}

struct node *search(struct node *head, char val)
{

	if(head->key == val && head != NULL)
	{
		head->key=-1;
		count++;
	}
	else if( val < head->key && head->left!= NULL)
	{
		search(head->left,val);
	}
	else if(val > head->key && head->right!= NULL)
	{
		search(head->right,val);
	}
	return head;
}

  
/* A utility function to insert a new node with given key in BST */
struct node* insert(struct node* node, char key)
{
    /* If the tree is empty, return a new node */
    if (node == NULL) return newNode(key);
 
    /* Otherwise, recur down the tree */
    if (key < node->key)
        node->left  = insert(node->left, key);
    else if (key > node->key)
        node->right = insert(node->right, key);   
 
    /* return the (unchanged) node pointer */
    return node;
}	



int main()
{
	int i, j;
	char str1[10], str2[10];
	char child[10];
	
	struct node *temp, *root=NULL;
	
	printf("\nString 1:");
	scanf("%s", str1);
	
	char *str = str1;
	
	while(*str != '\0')
	{
		root = insert(root,*str);
		str++;	
	}
	
	printf("\n str2:");
	scanf("%s", str2);
	
	str = str2;
	int cnt;
	
	while(*str != '\0')
	{
		
		root = search(root, *str);
		str++;
	
	}
	
	if(count > 0)
		printf("%d", count);
	//inorder(root);
}

