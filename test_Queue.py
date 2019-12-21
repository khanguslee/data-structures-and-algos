import pytest

from Queue import Queue, FullError, EmptyError


class TestQueue:
    def test_queue_creation(self):
        test_capacity = 10
        test_queue = Queue(test_capacity)
        assert test_queue.size == 0
        assert test_queue.capacity == test_capacity

    def test_queue_enqueuing(self, capfd):
        test_capacity = 10
        test_queue = Queue(test_capacity)
        test_queue.enqueue(1)
        test_queue.enqueue(2)
        test_queue.enqueue(3)
        test_queue.print_queue()

        out, _ = capfd.readouterr()
        actual_result = out.strip()
        expected_result = str([1, 2, 3])
        assert actual_result == expected_result

    def test_queue_dequeuing(self, capfd):
        test_capacity = 10
        test_queue = Queue(test_capacity)
        test_queue.enqueue(1)
        test_queue.enqueue(2)
        test_queue.enqueue(3)
        test_queue.dequeue()
        test_queue.print_queue()

        out, _ = capfd.readouterr()
        actual_result = out.strip()
        expected_result = str([2, 3])
        assert actual_result == expected_result

    def test_enqueue_full(self):
        with pytest.raises(FullError):
            test_capacity = 5
            test_queue = Queue(test_capacity)
            for index in range(test_capacity + 1):
                test_queue.enqueue(index)

    def test_dequeue_empty(self):
        with pytest.raises(EmptyError):
            test_capacity = 5
            test_queue = Queue(test_capacity)
            test_queue.dequeue()

    def test_isFull(self):
        test_capacity = 5
        test_queue = Queue(test_capacity)
        for index in range(test_capacity):
            test_queue.enqueue(index)
        assert test_queue.isFull() == True

    def test_isEmpty(self):
        test_capacity = 5
        test_queue = Queue(test_capacity)
        assert test_queue.isEmpty() == True

    def test_peek(self):
        test_capacity = 5
        test_queue = Queue(test_capacity)
        test_queue.enqueue(10)
        test_queue.enqueue(20)
        assert test_queue.peek() == 10 
