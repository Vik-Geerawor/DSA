"""
The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom.
"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""

        # empty list
        if self.head == None:
            return None

        # non-empty list
        current = self.head
        i = 1
        while i != position:
            if current.next:
                current = current.next
                i += 1
            else:
                current = None

        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""

        pre = self.head
        pre_position = position - 1
        i = 1
        while i != pre_position:
            if pre.next:
                pre = pre.next
                i += 1

        post = pre.next
        pre.next = new_element
        new_element.next = post

    def delete(self, value):
        """Delete the first node with a given value."""

        # if list is empty
        if self.head == None:
            return -1
        # if list is not empty
        elif self.head.value == value:
            self.head = self.head.next
        else:
            pre = self.head
            current = self.head.next
            while current.next:
                if current.value == value:
                    pre.next = current.next
                    break
                pre = current
                current = current.next
            if current.value == value:          # current = last node
                pre.next = None
            else:
                return -1
        return 0

    def __iter__(self):
        if self.head:
            current = self.head
            while current.next:
                yield current.value
                current = current.next
            yield current.value         # last node
        else:
            return -1


if __name__ == '__main__':
    # Test cases
    # Set up some Elements
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    # Start setting up a LinkedList
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    # Test get_position
    # Should print 3
    # print(ll.head.next.next.value)
    # # Should also print 3
    # print(ll.get_position(3).value)

    # # Test insert
    ll.insert(e4, 3)
    # # Should print 4 now
    # print(ll.get_position(3).value)

    for e in ll:
        print(e, end=' ')
    print()

    # # Test delete
    ll.delete(3)
    # # Should print 2 now
    # print(ll.get_position(1).value)
    # # Should print 4 now
    # print(ll.get_position(2).value)
    # # Should print 3 now
    # print(ll.get_position(3).value)

    for e in ll:
        print(e, end=' ')
    print()
