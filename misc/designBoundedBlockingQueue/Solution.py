from threading import Semaphore

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.queue = collections.deque()
        self.capacity = capacity
        self.producer = Semaphore(capacity)
        self.consumer = Semaphore(0)

    def enqueue(self, element: int) -> None:
        self.producer.acquire()
        self.queue.append(element)
        self.consumer.release()

        

    def dequeue(self) -> int:
        self.consumer.acquire()
        r = self.queue.popleft()
        self.producer.release()
        return r
        

    def size(self) -> int:
        return len(self.queue)
        
