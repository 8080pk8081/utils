#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 6:13 下午
# @Author :"Liu Jin Yao"
# @Email : 592203122@qq.com
# @File : 二叉树遍历.py


class Node:
    """节点类"""
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None


class BinaryTree:
    """二叉树"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """广度优先遍历方式添加节点"""
        if self.root is None:
            self.root = Node(item)
        else:
            queue = list()
            queue.append(self.root)

            while len(queue) > 0:
                node = queue.pop(0)
                if not node.lchild:
                    node.lchild = Node(item)
                    return
                else:
                    queue.append(node.lchild)
                if not node.rchild:
                    node.rchild = Node(item)
                    return
                else:
                    queue.append(node.rchild)

    def breadh_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = list()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.item, end=" ")
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def preorder_travel(self, root):
        """先序 根 左 右"""
        if root:
            print(root.item, end=" ")
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)

    def inorder_travel(self, root):
        """中序 左 根 右"""
        if root:
            self.inorder_travel(root.lchild)
            print(root.item, end=" ")
            self.inorder_travel(root.rchild)

    def postorder_travel(self, root):
        """后序 左 右 根"""
        if root:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item, end=" ")

if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadh_travel()
    tree.preorder_travel(tree.root)
    print("")
    tree.inorder_travel(tree.root)
    print("")
    tree.postorder_travel(tree.root)
    print("")

