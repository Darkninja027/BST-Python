
def seperate():
    for i in range(10):
        print()

def introduction():
    seperate()
    print("========================================")
    print("Create your own binary search tree (BST)")
    print("========================================")
    print()
    head_value = input("Input the value for the head node (Must be Integer): ")

    try:
        head_value = int(head_value)
        return head_value
    except:
        print("Invalid integer")
        input("press anything to retry")
        introduction()

def check_duplicates(duplist):
    nodups = []
    for elem in duplist:
        if elem not in nodups:
            nodups.append(elem)
    return nodups


def add_initial():
    seperate()
    num_list = []
    print("enter number to add to the initial bst (duplicates not accepted)")
    print("Type 'done' when finished")
    print()
    while(True):
        uinput = input("Enter here: ")
        try:
            if(uinput == "done"):
                break
            uinput = int(uinput)
            num_list.append(uinput)
        except:
            print(uinput + " is an invalid integer")
            print()
            print()

    num_list = check_duplicates(num_list)
    return num_list

