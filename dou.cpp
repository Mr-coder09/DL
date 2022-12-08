#include<iostream>
#include<stdlib.h>
using namespace std;
struct node *create();
void display(struct node *);
struct node *reverse(struct node *);
struct node *comp1(struct node *);
struct node *comp2(struct node *);
struct node * add(struct node *, struct node *);

struct node
{
	int data;
	struct node *next;
	struct node *prev;
}*B1=NULL,*B2=NULL,*C1=NULL,*C2=NULL,*A=NULL;

int main()
{
	int ch;
	cout<<"Enter First Binary no.:\n";
	B1=create();
	cout<<"\n First Binary no. \n";
	display(B1);
	cout<<"\nEnter the Second Binary no.:\n";
	B2=create();
	cout<<"\n Second Binary no. \n";
	display(B2);
	while(1)
	{
		cout<<"\n\nMenu:";
		cout<<"\n1.1's Complement and 2's complement of First Binary number.";
		cout<<"\n2.1's Complement and 2's complement of Second Binary number.";
		cout<<"\n3.Addition of two binary nos.";
		cout<<"\n4.Exit.";
		cout<<"\n\nEnter choice:";
		cin>>ch;
		switch(ch)
		{
		case 1:
			cout<<"\n1's Complement of First Binary number:\n";
			C1=comp1(B1);
			display(C1);
			cout<<"\n2's Complement of First Binary number:\n";
			C2=comp2(B1);
			display(C2);
			break;
		case 2:
			cout<<"\n1's Complement of Second Binary number:\n";
			C1=comp1(B2);
			display(C1);
			cout<<"\n2's Complement of Second Binary number:\n";
			C2=comp2(B2);
			display(C2);
			break;
		case 3:
			A=add(B1,B2);
			display(A);
			break;
		case 4:
			return 0;
		default:
			cout<<"Invalid Choice.";
			break;
		}
	}
}

struct node *create()
{
	char ch;
	struct node *new_node,*current,*start=NULL;
	do
	{
		new_node=(struct node*)malloc(sizeof(struct node));
		label:
		cout<<"\nEnter Binary digit: ";
		cin>>new_node->data;
		new_node->next=NULL;
		new_node->prev=NULL;
		if(new_node->data!=0 && new_node->data!=1)
		{
			cout<<"\nEnter Valid binary digit.\n\n";
			goto label;
		}
		else
		{
			if(start==NULL)
			{
				start=new_node;
				current=new_node;
			}
			else
			{
				current->next=new_node;
				new_node->prev=current;
				current=new_node;
			}
		}
	cout<<"\nDo you want to add more digits?(y/n):";
	cin>>ch;
	}while(ch!='n');
		return start;
}

void display(struct node *new_node)
{
	while(new_node!=NULL)
	{
		cout<<new_node->data<<"\t";
		new_node=new_node->next;
	}
	cout<<"\n";
}

struct node *comp1(struct node *new_node)
{
	struct node *n_node,*current,*start=NULL;
	while(new_node!=NULL)
	{
		n_node=(struct node*)malloc(sizeof(struct node));
		if(new_node->data==1)
		{
			n_node->data=0;
		}
		else
		{
			n_node->data=1;
		}
		n_node->next=NULL;
		n_node->prev=NULL;

			if(start==NULL)
			{
				start=n_node;
				current=n_node;
			}
			else
			{
				current->next=n_node;
				n_node->prev=current;
				current=n_node;}
				new_node=new_node->next;
	}
	return start;
}

struct node *comp2(struct node *temp)
{

	struct node *n1,*c,*start=NULL;
	c=comp1(temp);
	n1=(struct node*)malloc(sizeof(struct node));
	n1->data=1;
	n1->next=NULL;
	n1->prev=NULL;
	start=add(c,n1);
	return start;
}

struct node * add(struct node *start, struct node *start1)
{
	struct node *n, *c,*r=NULL;
	int rem=0;
	while(start->next!=NULL)
		start=start->next;
	while(start1->next!=NULL)
		start1=start1->next;
	while(start!=NULL && start1!=NULL)
	{
		n=(struct node*)malloc(sizeof(struct node));
		n->data=(start->data+start1->data+rem)%2;
		rem=(start->data+start1->data+rem)/2;
		n->next=NULL;
		n->prev=NULL;
		if(r==NULL)
			r=c=n;
		else
		{
			c->prev=n;
			n->next=c;
			c=c->prev;
		}
	start=start->prev;
	start1=start1->prev;
	}
	while(start!=NULL || start!=NULL)
	{
		n=(struct node*)malloc(sizeof(struct node));
		if(start!=NULL)
		{
			n->data=(start->data+rem)%2;
			rem=(start->data+rem)/2;
			start=start->prev;
		}
		else
		{
			n->data=(start1->data+rem)%2;
			rem=(start1->data+rem)/2;
			start1=start1->prev;
		}
		n->prev=NULL;
		c->prev=n;
		n->next=c;
		c=c->prev;
	}
	r=c;
	return r;
}