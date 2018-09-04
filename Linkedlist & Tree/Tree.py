class BinaryTree:
    # 樹節點所需元素 value      : 存放資料
    #               leftChild  : 左子節點
    #               rightChild : 右子節點
    def __init__(self, data):
        self.value = data
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, data):
        # 插入左節點
        # 若子節點為空則直接插入，不為空則建立新的左子節點
        if self.leftChild == None:
            self.leftChild = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.leftChild = self.leftChild
            self.leftChild = tree

    def insertRight(self, data):
        # 插入右節點
        # 若子節點為空則直接插入，不為空則建立新的右子節點
        if self.rightChild == None:
            self.rightChild = BinaryTree(data)
        else:
            tree = BinaryTree(data)
            tree.rightChild = self.rightChild
            self.rightChild = tree


def buildPostfixTree(exp):
    # 以後序方式建立二元樹
    # 遇到運算符就建立樹節點並將數字塞進去
    stack = []
    oper = '+-*/'
    for i in exp:
        if i not in oper:
            tree = BinaryTree(int(i))
            stack.append(tree)
        else:
            rightTree = stack.pop()
            leftTree = stack.pop()
            tree = BinaryTree(i)
            tree.leftChild = leftTree
            tree.rightChild = rightTree
            stack.append(tree)
    return stack.pop()


def evalPostfix(tree):
    # 遞迴取出節點的數值，並進行運算
    leftValue = None
    rightValue = None
    if tree:
        leftValue = evalPostfix(tree.leftChild)
        rightValue = evalPostfix(tree.rightChild)
        if leftValue and rightValue:
            if tree.value == '+':
                return leftValue + rightValue
            elif tree.value == '-':
                return leftValue - rightValue
            elif tree.value == '*':
                return leftValue * rightValue
            elif tree.value == '/':
                return leftValue / rightValue
        else:
            return tree.value


def main():
    # 輸入後序式
    xep = input("input postfix expression: ")
    print(evalPostfix(buildPostfixTree(xep)))


main()
