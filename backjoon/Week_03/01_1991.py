import sys

N = int(sys.stdin.readline().strip())
tree = {}

for i in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        # 선순위 탐색
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')


# class Node:
#     def __init__(self, data,left_node, right_node):
#         self.data = data
#         self.left_node = left_node
#         self.right_node = right_node
        
# def pre_order(node):
#     print(node.data, end=' ')
#     if node.left_node != None:
#         pre_order(tree[node.left_node])
#     if node.right_node != None:
#         pre_order(tree[node.right_node])

# n = int(input())

# tree = {}

# for i in range(n):
#     data, left_node, right_node = input().split()
#     if left_node == 'None':
#         left_node = None
#     if right_node == 'None':
#         right_node = None
#     tree[data]= Node(data, left_node,right_node)
