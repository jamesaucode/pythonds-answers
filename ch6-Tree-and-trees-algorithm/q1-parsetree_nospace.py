from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

# ### = changed
# This question is all about string manipulation

def buildParseTree(fpexp):
    fplist = list(fpexp.replace(" ", "")) ###
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    number = "" ###
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            number += i ###
        elif i in ['+', '-', '*', '/']:
            ###
            if number: 
                currentTree.setRootVal(int(number))
                parent = pStack.pop()
                currentTree = parent
                number = ""
            ###
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            ###
            if number:
                currentTree.setRootVal(int(number))
                parent = pStack.pop()
                currentTree = parent
                number = ""
            ###
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree