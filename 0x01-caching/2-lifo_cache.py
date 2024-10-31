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

    def put(self, key, item):
        """
            Add or update an item in the cache dictionary with key, 'key'.
            If the cache exceeds BaseCaching.MAX_ITEMS, discard the last
            recently added or updated item (LIFO caching algorithm).
        """
        if key is None or item is None:
            return

        # If key exists, remove it so it can be re-added as the most recent
        if key in self.cache_data:
            del self.cache_data[key]

        # If cache is at max capacity, remove the last-added item
        while len(self.cache_data) > self.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        # Add or update key-value pair as the newest item in cache
        self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in the cache dictionary linked to 'key'. """
        return self.cache_data.get(key)
