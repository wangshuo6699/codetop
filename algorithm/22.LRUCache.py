class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.used = []
        self.cache = {}
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            i = self.used.index(key)
            del self.used[i]
            self.used.insert(0, key)
            return self.cache[key]
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            i = self.used.index(key)
            del self.used[i]
            self.used.insert(0, key)
            return
        if len(self.cache) < self.capacity:
            self.used.insert(0, key)
            self.cache.update({key: value})
        else:
            _key = self.used.pop()
            self.cache.pop(_key)
            self.cache.update({key: value})
            self.used.insert(0, key)


# Your LRUCache object will be instantiated and called as such:
["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(1, 1)
obj.put(4, 1)
