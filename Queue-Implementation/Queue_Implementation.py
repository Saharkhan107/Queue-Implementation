class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def enqueue(self, element):
        # Add an element to the rear (end) of the queue
        self.queue.append(element)

    def dequeue(self):
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.queue.pop(0)  # pop from the front (index 0)
        else:
            return "Queue is empty"

    def peek(self):
        # Return the front element without removing it
        if not self.is_empty():
            return self.queue[0]  # peek at the front (index 0)
        else:
            return "Queue is empty"

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0


# Test case
if __name__ == "__main__":
    # Create a Queue instance
    q = Queue()

    # Enqueue three elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Dequeue one element
    print(f"Dequeued element: {q.dequeue()}")  # Expected output: 10

    # Peek at the front element
    print(f"Front element: {q.peek()}")  # Expected output: 20

