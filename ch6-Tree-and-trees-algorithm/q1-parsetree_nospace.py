from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    # Split the string argument into array
    pStack = Stack()
    # Stack in this case is to store the data of the tree 
    #(what is the last tree?.. etc)
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            # Create a new node as the left child of the root
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            # So, if it's a number,
            # Set the value of this node to i
            currentTree.setRootVal(int(i))
            # Get the parent tree from the top of the stack
            parent = pStack.pop()
            # Go back to the root of the tree (Go up)
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            # Set the current node as i (opeartion symbol)
            currentTree.setRootVal(i)
            # Create a new node as the right child of the root
            currentTree.insertRight('')
            # Saves this current tree on the top of the stack
            pStack.push(currentTree)
            # Travels to the right child of the current node
            currentTree = currentTree.getRightChild()
        elif i == ')':
            # Go back one branch if we see a ')'
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree