class EmptyError(Exception):
    pass

class FullError(Exception):
    pass

class Queue:
    def __init__(self, input_capacity):
        self.capacity = input_capacity
        self.size = 0
        self.queue = [None] * self.capacity
        self.front = self.size
        self.rear = self.capacity - 1
    
    def isFull(self):
        """Checks if the current queue is full"""
        return self.size == self.capacity

    def isEmpty(self):
        """Checks if the current queue is empty"""
        return self.size == 0
        
    def enqueue(self, input_value):
        """Add a value onto the rear of the queue"""
        if self.isFull():
            raise FullError("Queue Full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = input_value
        self.size += 1

    def dequeue(self):
        """Remove a value from the front of the queue"""
        if self.isEmpty():
            raise EmptyError("Queue Empty")
        output_value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return output_value

    def peek(self):
        """View the value at the front of the queue"""
        return self.queue[self.front]

    def print_queue(self):
        """Prints out the current state of the queue"""
        output_array = []
        for index in range(self.size):
            actual_index = (self.front + index) % self.capacity
            item = self.queue[actual_index]
            output_array.append(item)
        print(output_array)

if __name__ == "__main__":
    queue = Queue(10)
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.dequeue()
    queue.dequeue()
    queue.print_queue()




        

    
