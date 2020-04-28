from typing import List

class Node:
    def __init__(self,val):
        self.val = val
        self.next = self.prev = None

class DLList:
    def __init__(self):
        self.head , self.tail = Node(-1) , Node(-1)
        self.head.next , self.tail.prev = self.tail , self.head
        
    def addNode(self, node):
        tmp = self.tail.prev
        node.next = self.tail 
        node.prev = tmp
        tmp.next = node
        self.tail.prev = node


    def deleteNode(self,node):
        pnode = node.prev
        nnode = node.next
        pnode.next = nnode 
        nnode.prev = pnode
    
    def getFirstUnique(self):
        return self.head.next.val
        


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.uniq , self.dups , self.ulist = {} , set(), DLList()
        for n in nums:
            self.add(n)
 
    def showFirstUnique(self) -> int:
        return self.ulist.getFirstUnique()

    def add(self, n: int) -> None:
        if n in self.dups: return
        if n in self.uniq:
            node = self.uniq[n]
            self.ulist.deleteNode(node)
            del self.uniq[n]
            self.dups.add(n)
        else:
            node = Node(n)
            self.uniq[n] = node
            self.ulist.addNode(node)
            


firstUnique = FirstUnique([2,3,5])
print(firstUnique.showFirstUnique() )
firstUnique.add(5)           
print(firstUnique.showFirstUnique())
firstUnique.add(2)
print(firstUnique.showFirstUnique())
firstUnique.add(3);           
print(firstUnique.showFirstUnique())


'''
    #Simpler solution
    def __init__(self, nums: List[int]):
        self.unique = {}
        self.total = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return next(iter(self.unique), -1)  # credit to @cwardgar, @C0R3 and @user1633C for contribution of the concise code.

        
    def add(self, value: int) -> None:
        if value in self.total:
            self.unique.pop(value, 1)
        else:
            self.total.add(value)
            self.unique[value] = 1
            
'''