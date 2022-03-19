import sys
sys.path.append('/Users/leocucinell/Desktop/Learning/leetcode/dataStructs')

from linked_list import LinkedList
from linked_list import Node

def main():
    ll1 = LinkedList()
    ll1_head = Node(5)
    ll1_next = Node(6)
    ll1_head.next = ll1_next

    ll1.head = ll1_head
    print(ll1)


if __name__ == "__main__":
    main()