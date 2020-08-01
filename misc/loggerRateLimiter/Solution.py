class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [-1] * 10
        self.sets = [set()] * 10
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        t = timestamp % 10
        if timestamp != self.buckets[t]:
            self.buckets[t] = timestamp
            self.sets[t] = set()
        for i in range(10):
            if timestamp - self.buckets[i] < 10 :
                if message in self.sets[i]: return False
        self.sets[t].add(message)
        return True

        

        


# Your Logger object will be instantiated and called as such:
logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2,"bar"))
print(logger.shouldPrintMessage(3,"foo"))
print(logger.shouldPrintMessage(8,"bar"))
print(logger.shouldPrintMessage(10,"foo"))
print(logger.shouldPrintMessage(11,"foo"))