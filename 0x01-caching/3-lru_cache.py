#!/usr/bin/env python3
""" Module containing the 'LRUCache' class. """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        LRU Caching system that defines 'put' and 'get' methods for the
        'self.cache_data' dictionary from the 'BaseCaching' parent class.
    """
    def __init__(self):
        super().__init__()
        # Key list, according to use time.
        self.usage_list = []

    def put(self, key, item):
        """
            Add or update an item in the cache dictionary with key, 'key'.
            If the cache exceeds BaseCaching.MAX_ITEMS, discard the least
            recently used item (LRU caching algorithm).
        """
        if key is None or item is None:
            return

        # If the key already exists, update it.
        # Remove and append key from/to 'usage_list' to avoid duplicates.
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_list.remove(key)
            self.usage_list.append(key)
            return  # No need to check size as only an update was done.

        # If the cache is at or above max capacity, remove the LRU item.
        # The key removed is removed from 'usage_list'.
        while len(self.cache_data) >= self.MAX_ITEMS:
            first_key = self.usage_list.pop(0)  # Remove & return LRU key.
            print(f"DISCARD: {first_key}")
            del self.cache_data[first_key]  # Remove the LRU item from cache.

        # Add the new key-value pair and append key to 'usage_list'.
        self.cache_data[key] = item
        self.usage_list.append(key)

    def get(self, key):
        """
            Returns the value in the cache dictionary linked to 'key'.
            Removes and appends key from/to 'usage_list' to avoid duplicates.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_list.remove(key)
        self.usage_list.append(key)
        return self.cache_data.get(key)
