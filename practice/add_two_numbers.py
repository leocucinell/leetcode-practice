import sys
sys.path.append('/Users/leocucinell/Desktop/Learning/leetcode/dataStructs')
from linked_list import LinkedList
from linked_list import Node


def add_two_numbers(l1, l2):
    result = Node(0)
    result_pointer = result
    carry = 0

    while l1 or l2 or carry:
        val1 = (l1.val if l1 else 0)
        val2 = (l2.val if l2 else 0)
        add_nums = val1 + val2 + carry
        carry, out = divmod(add_nums, 10)
        result_pointer.next = Node(out)
        result_pointer = result_pointer.next
        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next



def main():
    ll1 = LinkedList()
    ll2 = LinkedList()

    ll1_head = Node(2)
    ll1_next = Node(4)
    ll1_end = Node(3)
    ll1_head.next = ll1_next
    ll1_next.next = ll1_end
    ll1.head = ll1_head

    ll2_head = Node(5)
    ll2_next = Node(6)
    ll2_end = Node(4)
    ll2_head.next = ll2_next
    ll2_next.next = ll2_end
    ll2.head = ll2_head

    result = add_two_numbers(ll1_head, ll2_head)
    print(result)
    print(result.next)
    print(result.next.next)


if __name__ == "__main__":
    main()