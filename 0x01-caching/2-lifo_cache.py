#!/usr/bin/env python3


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class. Inherits from BaseCaching. Uses LIFO caching system.
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.keys.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")
        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
