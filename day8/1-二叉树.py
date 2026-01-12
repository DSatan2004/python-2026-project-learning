
class Node:
    def __init__(self,elem=-1, lchild=None, rchile=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchile

class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue = [] # 辅助队列

    def level_build_tree(self,node:Node):
        if self.root is None: #树根为空
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:#如果当前父亲的左孩子是空
                self.help_queue[0].lchild = node # 放入左孩子
            else:
                self.help_queue[0].rchild = node #放入右孩子
                self.help_queue.pop(0) # 当前父亲满了，出队

    def pre_order(self,current_node:Node):
        if current_node:
            print(current_node.elem,end=' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def in_order(self,current_node:Node):
        if current_node:
            self.in_order(current_node.lchild)
            print(current_node.elem,end=' ')
            self.in_order(current_node.rchild)

    def last_order(self,current_node:Node):
        if current_node:
            self.last_order(current_node.lchild)
            self.last_order(current_node.rchild)
            print(current_node.elem,end=' ')

    def lever_order(self):
        help_queue=[]
        help_queue.append(self.root) # 树根入队
        while help_queue:
            out_node:Node = help_queue.pop(0) #出队
            print(out_node.elem,end=' ')
            if out_node.lchild:
                help_queue.append(out_node.lchild)
            if out_node.rchild:
                help_queue.append(out_node.rchild)

if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1,11):
        new_node = Node(i) # 实例化结点
        tree.level_build_tree(new_node) #把结点放入树中
    tree.pre_order(tree.root) #前序遍历，就是深度优先遍历
    print()
    tree.in_order(tree.root)
    print()
    tree.last_order(tree.root)
    print()
    tree.lever_order()