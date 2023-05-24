"""
Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!
"""


class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

    def __iter__(self):                 # NOTE: Gotcha
        # for item in self.storage:
        #     yield item
        return self.storage.__iter__()


def main():
    pass


if __name__ == '__main__':
    main()

    # Setup
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test peek
    # Should be 1
    print(q.peek())

    # Test dequeue
    # Should be 1
    print(q.dequeue())

    # Test enqueue
    q.enqueue(4)
    # Should be 2
    print(q.dequeue())
    # Should be 3
    print(q.dequeue())
    # Should be 4
    print(q.dequeue())
    q.enqueue(5)
    # Should be 5
    print(q.peek())
    print(f"Test completed")

    print(f"\nTesting iter")
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)

    print(f"iter type of q: {type(q.__iter__())}")
    for i in q:
        print(i)
