from typing import Deque
from collections import deque
import turtle

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val})'


def deserialize(data):
    if not data : return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in data.strip('[]').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def serialize(root):
    q , ans = deque([root]), []
    while q:
        node = q.popleft()
        if node:
            ans.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else :
            ans.append('null')
    return '[' + ','.join(ans) + ']'


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)


    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    drawtree(deserialize('[4,2,5,1,3,null,null]'))

