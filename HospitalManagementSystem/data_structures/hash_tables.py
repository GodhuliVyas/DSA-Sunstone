#Hash Tables: Use for managing medical inventory.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def add_item(self, key, value):
        hash_key = self._hash_function(key)
        bucket = self.hash_table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get_item(self, key):
        hash_key = self._hash_function(key)
        bucket = self.hash_table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove_item(self, key):
        hash_key = self._hash_function(key)
        bucket = self.hash_table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
