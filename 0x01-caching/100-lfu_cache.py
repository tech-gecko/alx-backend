#!/usr/bin/env python3
""" Module containing the 'LFUCache' class. """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
        LFU Caching system that defines 'put' and 'get' methods for the
        'self.cache_data' dictionary from the 'BaseCaching' parent class.
    """
    def __init__(self):
        super().__init__()
        # Key dict, according to use count.
        self.usage_dict = {}

    def put(self, key, item):
        """
            Add or update an item in the cache dictionary with key, 'key'.
            If the cache exceeds BaseCaching.MAX_ITEMS, discard the least
            frequently used item (LFU caching algorithm).
        """
        if key is None or item is None:
            return

        # If the key already exists, update it.
        # Increment usage count for the key by 1.
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_dict[key] += 1
            return  # No need to check size as only an update was done.

        # If the cache is at or above max capacity, remove the LFU item.
        # The key removed is removed from 'usage_dict'.
        while len(self.cache_data) >= self.MAX_ITEMS:
            # Remove & return LFU key.
            least_used_key = min(self.usage_dict, key=self.usage_dict.get)
            print(f"DISCARD: {least_used_key}")
            # Remove the LFU item from cache.
            del self.cache_data[least_used_key]
            # Remove also from counting dict to synchronize.
            del self.usage_dict[least_used_key]

        # Add the new key-value pair and set key usage count to 1.
        self.cache_data[key] = item
        self.usage_dict[key] = 1

    def get(self, key):
        """
            Returns the value in the cache dictionary linked to 'key'.
            Increments usage count for the key by 1.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_dict[key] += 1
        return self.cache_data.get(key)
