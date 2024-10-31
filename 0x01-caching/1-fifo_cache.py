#!/usr/bin/env python3
""" Module containing the 'FIFOCache' class. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        FIFO Caching system that defines 'put' and 'get' methods for the
        'self.cache_data' dictionary from the 'BaseCaching' parent class.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
            Add an item, 'item' to the cache dictionary with key, 'key'.
            If number of items >= BaseCaching.MAX_ITEMS, we discard the
            first-in item (FIFO caching algorithm).
        """
        if key is None or item is None:
            return

        """
            Removes the first key-value pair if and only if the key-value pair
            to be added is new and the length of the cache dictionary is at or
            above the max limit.
        """
        if (
            key not in self.cache_data and
            len(self.cache_data) >= self.MAX_ITEMS
        ):
            # Remove the first item
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

        # Add or update key-value pair
        self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in the cache dictionary linked to 'key'. """
        return self.cache_data.get(key)
