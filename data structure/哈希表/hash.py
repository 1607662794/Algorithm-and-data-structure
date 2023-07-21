class LinkList:
    class Node:  # 被LinkList调用的类
        def __init__(self, item):
            self.item = item
            self.next = None

    class LinkListIterator:  # 被LinkList调用的类
        def __init__(self, node):
            self.node = node

        def __next__(self):  # 返回迭代器的值
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):  # 迭代器本身
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):  # 链表的插入
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):  # 依次给每个链表插入值
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    # def find(self,obj):
    #     for n in self:
    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):  # 用于打印时的被动触发
        return "<" + ",".join(map(str, self)) + ">"


'''哈希表：超过规定范围内的关键字值可以经过哈希函数映射于定义域从而实现数据的添加'''


class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]  # 给每个关键字处创建一个链表

    def h(self, k):  # 哈希函数
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("duplicated Insert.")
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)  # 新的数值是在对应的链表中查询的


ht = HashTable()
ht.insert(0)
ht.insert(1)
print(",".join(map(str, ht.T)))  # map是一个映射函数，.join函数是一个拆解函数
