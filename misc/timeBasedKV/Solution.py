from typing import List
import collections 
import bisect

class TimeMap:
    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''

# Your TimeMap object will be instantiated and called as such:
kv = TimeMap()
kv.set('foo','bar',1)
print(kv.get('foo',1))
print(kv.get('foo',3))
kv.set("foo", "bar2", 4)
print(kv.get('foo',4))
print(kv.get('foo',5))

