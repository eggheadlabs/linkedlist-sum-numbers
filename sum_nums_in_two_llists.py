# How do you find the sum of two linked lists using Stack?
# Example: 9973 in llist1 (9->9->7->3->None), 856 in llist2 (8->5->6->None)
# sum ==> 10829

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

def sum_two_nums(ll1, ll2, length):
    # convert llist to stack
    s1, s2 = [], []
    node = ll1.head
    while node:
        s1.append(node.data)
        node = node.next
    node = ll2.head
    while node:
        s2.append(node.data)
        node = node.next

    # addition of digits starting at from the right most digit (stack top)
    d, d1, d2 = [0] * (length+1), [0] * (length+1), [0] * (length+1)
    carry = [0] * (length+2)
    i = 0
    while i < length+1:
        if len(s1) > 0: d1[i] = s1.pop()
        if len(s2) > 0: d2[i] = s2.pop()
        d[i] = (d1[i] + d2[i] + carry[i]) % 10
        carry[i+1] = int((d1[i] + d2[i] + carry[i] - d[i]) / 10)
        i += 1
    d.reverse()
    return d

# Preparation: the two linked lists
s1 = [9, 9, 7, 3]
s2 = [8, 5, 6]
s1_str = ''.join(list(map(str, s1)))
s2_str = ''.join(list(map(str, s2)))
ll1 = SinglyLinkedList()
for x in reversed(s1): ll1.push(x)
ll2 = SinglyLinkedList()
for x in reversed(s2): ll2.push(x)
length = max(len(s1), len(s2))

# calculate the sum of numbers in two linkedlists 
res = sum_two_nums(ll1, ll2, length)
sum_str = ''.join(list(map(str, res)))
print(s1_str + ' + ' + s2_str + ' = ' + sum_str)
