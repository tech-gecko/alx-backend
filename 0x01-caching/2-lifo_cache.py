#!/usr/bin/env python3
""" Module containing the 'LIFOCache' class. """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        LIFO Caching system that defines 'put' and 'get' methods for the
        'self.cache_data' dictionary from the 'BaseCaching' parent class.
    """
    def __init__(self):
        super().__init__()
        # Key list, according to adding or updating time.
        self.key_list = []

    def put(self, key, item):
        """
            Add or update an item in the cache dictionary with key, 'key'.
            If the cache exceeds BaseCaching.MAX_ITEMS, discard the last
            recently added or updated item (LIFO caching algorithm).
        """
        if key is None or item is None:
            return

        # If the key already exists, update it and append key to 'key_list'.
        if key in self.cache_data:
            self.cache_data[key] = item
            self.key_list.append(key)
            return  # No need to check size as only an update was done.

        # If the cache is at or above max capacity, remove the last-added item.
        # The key removed is removed from 'key_list'.
        while len(self.cache_data) >= self.MAX_ITEMS:
            last_key = self.key_list.pop()  # Remove & return last updated key.
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]  # Remove the last item from cache.

        # Add the new key-value pair and append key to 'key_list'.
        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """ Returns the value in the cache dictionary linked to 'key'. """
        return self.cache_data.get(key)
