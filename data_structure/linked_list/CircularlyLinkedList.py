class Node:
    def __init__(self,value):
        self.value=value
        self.nextnode=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=None

    def add_head_node(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.head.nextnode=self.head
            
        crnt_node=node
        crnt_node.nextnode=self.head        
        first_node=self.head
        while first_node.nextnode is not self.head:
            first_node=first_node.nextnode          
        first_node.nextnode=crnt_node
        self.head=crnt_node

    #Adding elements in linked list to the tail.
    def add_tail_node(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.head.nextnode=self.head
        crnt_node=node
        last_node=self.head
        while last_node.nextnode is not self.head:
            last_node=last_node.nextnode
        #pointing  head's last element to given node
        last_node.nextnode=crnt_node
        #pointing last node next to head nodes of element
        crnt_node.nextnode=self.head

    #Adding elements in linked after given Node.
    def add_after_node(self,after_value,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.head.nextnode=self.head
        new_node=node
        after_node=Node(after_value)
        head_node=self.head
        while head_node.value !=after_node.value:
            head_node=head_node.nextnode
            last_node=head_node.nextnode
        head_node.nextnode=new_node
        new_node.nextnode=last_node
        head_node=head_node.nextnode

    #Adding elements in linked before given Node.
    def add_before_node(self,bfr_value,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.head.nextnode=self.head
        new_node=node
        bfr_node=Node(bfr_value)
        head_node=self.head
        while head_node.nextnode.value!=bfr_node.value:
            head_node=head_node.nextnode
            last_node=head_node.nextnode
        head_node.nextnode=new_node
        new_node.nextnode=last_node
        head_node=head_node.nextnode
        #self.head=head_node.nextnode

    #deleting Head Node of Linked List
    def del_head_node(self):
        if self.head is None:
            print('Can not delete elements from Empty Linked List')
            return
        crnt_node=self.head.nextnode
        pointer_head=self.head.nextnode
        while pointer_head.nextnode.value!=self.head.value:
            pointer_head=pointer_head.nextnode
        pointer_head.nextnode=crnt_node
        self.head=crnt_node
        
    #deleting tail Node of Linked List
    def del_tail_node(self):
        if self.head is None:
            print('Can not delete elements from Empty Linked List')
            return
        crnt_node=self.head.nextnode
        #head_node=self.head
        while crnt_node.nextnode.nextnode.value!=self.head.value:
            crnt_node=crnt_node.nextnode
        crnt_node.nextnode=self.head

    #delete beteween node from Linked List
    def del_bw_node(self,value):
        node=Node(value)
        if self.head is None:
            print('Can not delete elements from Empty Linked List')
            return
        crnt_node=self.head
        while crnt_node.nextnode.value!=node.value:
            crnt_node=crnt_node.nextnode
            last_node=crnt_node.nextnode.nextnode
        crnt_node.nextnode=last_node

    #Function to print linked list node 
    def print_list(self):
        crnt_node=self.head
        while True:
            print(f'{crnt_node.value}->',end='')
            if crnt_node.nextnode is self.head:
                print(f'{self.head.value}',end='')
                break
            crnt_node = crnt_node.nextnode
        print()