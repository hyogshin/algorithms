class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def _index(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        i = self._index(key)
        if not self.buckets[i]:
            self.buckets[i] = Node(key)
            return
        curr = self.buckets[i]
        while True:
            if curr.key == key:
                return
            if not curr.next:
                curr.next = Node(key)
                break
            curr = curr.next
        

    def remove(self, key: int) -> None:
        i = self._index(key)
        prev = curr = self.buckets[i]
        if not self.buckets[i]:
            return
        if curr.key == key:
            self.buckets[i] = curr.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev, curr = curr, curr.next
        

    def contains(self, key: int) -> bool:
        i = self._index(key)
        curr = self.buckets[i]
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)