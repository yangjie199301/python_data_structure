from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def build_parser_tree(fpexp):
    fplist = fpexp.split()
    pstack = Stack()
    etree = BinaryTree('')
    pstack.push(etree)
    currenttree = etree
    symbols = ['+','-','*','/',]
    for i in fplist:
        if i == '(':
            currenttree.insertLeft('')
            pstack.push(currenttree)
            currenttree =currenttree.getLeftChild()
        elif i not in symbols and != ')':
            currenttree.setRootVal(int(i))
            parent = pstack.pop()
            currenttree = parent
        elif i in symbols:
            currenttree.setRootVal(i)
            currenttree.insertRight('')
            pstack.push(currenttree)
            currenttree = currenttree.getRightChild()
        elif i ==')':
            currenttree = pstack.pop()
        else:
            raise ValueError

    return etree

def evaluate(parsertree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

    leftc = parsertree.getLeftChild()
    rightc = parsertree.getRightChild()

    if leftc and rightc:
        fn = opers[parsertree.getRootVal()]
        return fn(evaluate(leftc),evaluate(rightc))
    else:
        return parsertree.getRootVal()

def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

def printexp(tree):
    sval = ''
    if tree:
        sval = '(' + printexp(tree.getLeftChild())
        sval = sval + str(tree.getRootVal())
        sval = sval + printexp(tree.getRightChild()) + ')'
    return sval