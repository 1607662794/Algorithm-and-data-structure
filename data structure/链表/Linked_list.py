'''链表实操'''

'''链表定义'''


class Node(object):  # 定义类的三种表达是等价的
    def __init__(self, item):
        self.item = item
        self.next = None


# a = Node(1)
# b = Node(2)
# a.next = b
# print(a.next.item)

'''链表创建'''
'''头插法'''


def creat_linklist_head(li):  # 将输入的列表，每个元素按照头插的方式插入链表首端
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head


print(creat_linklist_head([1, 2, 3]).item)  # 返回的是第一个元素，因此是原列表的倒序

'''尾插法'''


def creat_linklist_tail(li):  # 将输入的列表，每个元素按照尾插的方式插入链表尾端
    tail = Node(li[0])
    head = tail
    for element in li[1:]:
        tail.next = Node(element)
        tail = Node(element)
    return head


print(creat_linklist_tail([1, 2, 3]).item)  # 返回的是第一个元素，因此是原列表的顺序

'''双链表'''
class bi_Node(object):  # 定义类的三种表达是等价的
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prior = Node