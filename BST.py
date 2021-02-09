import sys
import conUI as ui

class BST:
    def __init__(self, node):
        self.head = node

    def add(self,head,node):
        if self.head == None: 
            self.head = node
            return

        if head.left_child == None and node.value < head.value:
            head.left_child = node
            print("added left value:" + str(node.value))

        elif head.right_child == None and node.value > head.value:
            head.right_child = node
            print("added right value:" + str(node.value))
        
        elif node.value < head.value:
            head = head.left_child
            print("left")
            self.add(head, node)
        elif node.value > head.value:
            head = head.right_child
            print("right")
            self.add(head, node)
        else:
            print("value already exists")

    '''
        shows the tree with the head value first
    '''

    def traverse_head_first(self, head):
        if head == None: return print("Lists empty")
        print(head.value, end=" ")
        if head.left_child != None: self.traverse_head_first(head.left_child)
        if head.right_child != None: self.traverse_head_first(head.right_child)

    '''
        Shows the tree in ascending order
    '''
    def traverse_acending(self, head):
        if head == None: return print("Lists empty")
        if head.left_child != None: self.traverse_acending(head.left_child)
        print(head.value, end=" ")
        if head.right_child != None: self.traverse_acending(head.right_child)
    
    '''
        Shows the tree in decending order
    '''
    def traverse_decending(self, head):
        if head == None: return print("Lists empty")
        if head.right_child != None: self.traverse_decending(head.right_child)
        print(head.value, end = " ")
        if head.left_child != None: self.traverse_decending(head.left_child)

    def exists(self, head, number):
        if head == None: return False
        if head.value == number: return True
        left = self.exists(head.left_child, number)
        if left: return True
        right = self.exists(head.right_child, number)
        return right

    def get_node(self, current, parent, number):
        p = parent
        c = current
        if c.value == number:
            print("Selected nodes value: " + str(c.value))
            print("No parent node (HEAD)")
            if c.left_child != None: print("Selected nodes left child: " + str(c.left_child.value))
            else: print("Selected node has no left child")
            if c.right_child != None: print("Selected nodes right child: " + str(c.right_child.value))
            else: print("Selected node has no right child")
            return

        while c.value != number:
            if number < c.value:
                p = c
                c = c.left_child
            else:
                p = c
                c = c.right_child
        
        if p.value > c.value: 
            print("Selected nodes value: " + str(c.value) + "\n" + "Parent of selected node: " + str(p.value) + " Selected node is left child of parent")
            if c.left_child != None: 
                print("Selected nodes left child: " + str(c.left_child.value))
            else:
                print("Selected node has no left child")
            if c.right_child != None: 
                print("Selected nodes right child: " + str(c.rightchild.value))
            else:
                print("Selected node has no right child")
        else:
            print("Selected nodes value: " + str(c.value) + "\n" + "Parent of selected node: " + str(p.value) + " Selected node is right child of parent")
            if c.left_child != None: 
                print("Selected nodes left child: " + str(c.left_child.value))
            else:
                print("Selected node has no left child")
            if c.right_child != None: 
                print("Selected nodes right child: " + str(c.rightchild.value))
            else:
                print("Selected node has no right child")
            



    def remove_lesser(self, number):
        current = self.head.left_child
        parent = self.head
        temp = None
        left = False

        while current.value != number:
            if number < current.value:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

        if parent.value > current.value: left = True

        # Logic to see if the node being removed has no children and removes it depending on if its the left
        # or the right child of its parent
        if current.left_child == None and current.right_child == None and left: 
            parent.left_child = None
            return
        elif current.left_child == None and current.right_child == None and not left:
            parent.right_child = None
            return
        #==================================================================================================#

        # The logic depending on if the node to be removed has one child and depending on which child and
        # what side the parent is will depend where the nodes children end up
        if current.left_child == None and left:
            parent.left_child = current.right_child
            return
        elif current.right_child == None and left:
            parent.left_child = current.left_child
            return
        elif current.left_child == None and not left:
            parent.right_child = current.right_child
            return
        elif current.right_child == None and not left:
            parent.right_child = current.left_child
            return
        #==================================================================================================#
        


    def remove_greater(self, number):
        pass

    def remove_head(self):
        if self.head.left_child == None and self.head.right_child == None: self.head = None
        elif self.head.left_child == None: self.head = self.head.right_child
        elif self.head.right_child == None: self.head = self.head.left_child
        else:
            curr = self.head.left_child
            temp = curr.right_child
            parent = None
            while temp != None:
                parent = temp
                temp = temp.right_child
            parent.right_child = self.head.right_child
            self.head = curr

    def remove_main(self, number):

        if not self.exists(self.head,number):
            print()
            print("Node doesnt exist in tree")
            return

        if self.head.value == number: 
            self.remove_head()
            return

        if number < self.head.value: self.remove_lesser(number)
        else: self.remove_greater(number)


        
        
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def do_things(command, bst):
    if command[0].lower() == "add" and len(command) == 2:
        try:
            number = int(command[1])
        except:
            print("'add' was used with an invalid number")
            return
        bst.add(bst.head, Node(number))
    elif command[0].lower() == "exists" and len(command) == 2:
        try:
            number = int(command[1])
        except:
            print("'exists' was used with an invalid number")
            return
        finally:
            ex = bst.exists(bst.head, number)
            if ex:
                print()
                print(str(number) + " Exists in tree")
            else:
                print()
                print(str(number) + " does not exist in tree")
    elif command[0].lower() == "get" and len(command) == 2:
        try:
            number = int(command[1])
        except:
            print("'get' was given an invalid number")
        bst.get_node(bst.head, None, number)
    elif command[0].lower() == "exit":
        sys.exit()
    elif command[0].lower() == "show" and len(command) == 2:
        if command[1].lower() == "asc":
            bst.traverse_acending(bst.head)
        elif command[1].lower() == "dsc":
            bst.traverse_decending(bst.head)
        elif command[1].lower() == "head":
            bst.traverse_head_first(bst.head)
        else:
            print("'show' was given an invalid order")
    elif command[0].lower() == "remove" and len(command) == 2:
        try:
            number = int(command[1])
        except:
            print("'remove' was given an invalid number")
            return
        
        bst.remove_main(number)
        
    else:
        print()
        print("Invalid command")
        

def user_tree_maniuplation(bst):
    ui.seperate()
    commands = ["add","exists", "exit", "show", "remove"]
    command_explained = [" (number) - Adds number with the value given", 
        " (number)  - checks the tree to see if number exists",
        " - exits the application",
        " (order) - shows the tree in a given order: asc, dsc, head",
        " (number) - removes a node in the tree if it exists"]

    while True:
        print()
        print()
        print("From here you can view and manipulate your BST")
        print("Type 'help' for a list of commands")
        uin = input("What would you like to do? - ")
        uin = uin.split()
        if len(uin) == 0:
            print()
            print("Invalid command!")
        elif uin[0].lower() == "help":
            print()
            for com in range(0, len(commands)):
                print(commands[com] + command_explained[com])
        else:
            do_things(uin, bst)
        




def main():
    head_value = ui.introduction()
    head_node = Node(head_value)
    tree = BST(head_node)
    numbers = ui.add_initial()

    for num in numbers:
        tree.add(tree.head, Node(num))
    
    user_tree_maniuplation(tree)

main()


