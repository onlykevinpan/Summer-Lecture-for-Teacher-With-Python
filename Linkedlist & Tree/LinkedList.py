class Node:
#一個節點含兩個數值及下一個節點所在位置
    def __init__(self):
        self.coeff = None
        self.power = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
#插入節點時即依照次方做排序
    def addNode(self, coeff, power):
        curr = self.head
        if curr is None:
            n = Node()
            n.coeff = coeff
            n.power = power
            self.head = n
            return

        if curr.power < power:
            n = Node()
            n.coeff = coeff
            n.power = power
            n.next = curr
            self.head = n
            return

        while curr.next is not None:
            if curr.next.power < power:
                break
            curr = curr.next
        n = Node()
        n.coeff = coeff
        n.power = power
        n.next = curr.next
        curr.next = n
        return


def output(ll):
#輸出控制
    c = ll.head
    while c is not None:
        che = c.next
        if(che != None):
            if(che.coeff > 0):
                print(str(c.coeff)+"X^"+str(c.power)+"+", end="")
            else:
                print(str(c.coeff)+"X^"+str(c.power), end="")
        else:
            if(c.power == 0):
                print(str(c.coeff))
            else:
                print(str(c.coeff)+"X^"+str(c.power))
        c = c.next


def main():
    #輸入0 0 時結束
    ll = LinkedList()
    coeff, power = map(int, input("input coefficient and power: ").split())
    while coeff != 0:
        ll.addNode(coeff, power)
        coeff, power = map(int, input("input coefficient and power: ").split())

    output(ll)


main()
