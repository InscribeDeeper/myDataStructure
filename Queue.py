class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem  # 表示对应的元素值
        self.next = next  # 表示下一个链接的链点


class Queue(object):
    def __init__(self):
        self.head = None  # 头部链点为 None
        self.rear = None  # 尾部链点为 None

    def is_empty(self):
        return self.head is None  # 判断队列是否为空

    def enqueue(self, elem):
        """
        往队尾添加一个元素
        :param elem:
        :return:
        """
        p = Node(elem)  # 初始化一个新的点
        if self.is_empty():
            self.head = p  # 队列头部为新的链点
            self.rear = p  # 队列尾部为新的链点
        else:
            self.rear.next = p  # 队列尾部的后继是这个新的点
            self.rear = p  # 然后让队列尾部指针指向这个新的点

    def dequeue(self):
        """
        从队列头部删除一个元素，并返回这个值，类似于pop
        :return:
        """
        if self.is_empty():  # 判断队列是否为空
            print('Queue_is_empty')  # 若队列为空，则退出 dequeue 操作
        else:
            result = self.head.elem  # result为队列头部元素
            self.head = self.head.next  # 改变队列头部指针位置
            return result  # 返回队列头部元素

    def peek(self):
        """
        查看队列的队头
        :return:
        """
        if self.is_empty():  # 判断队列是否为空
            print('NOT_FOUND')  # 为空则返回 NOT_FOUND
        else:
            return self.head.elem  # 返回队列头部元素

    def print_queue(self):
        print("queue:")
        temp = self.head
        myqueue = []  # 暂时存放队列数据
        while temp is not None:
            myqueue.append(temp.elem)
            temp = temp.next
        print(myqueue)


class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.head = LinkedNode(-1)  # dummy
        self.h = self.head  # true head

    def enqueue(self, item):
        self.h.next = LinkedNode(item)  # 这个 item进来后, queue的尾巴 要指向 这个 item
        self.h = self.h.next

    """
    @return: An integer
    """

    def dequeue(self):
        val = self.h.next.val  # 保存当前值, 因为 第一个是 -1, 需要一个空值 来 初始化
        self.h = self.h.next  # 将head指针 指向 next
        return val
