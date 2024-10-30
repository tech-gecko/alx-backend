#!/usr/bin/env python3
""" Module containing the 'BasicCache' class. """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Caching system that defines 'put' and 'get' methods for the
        'self.cache_data' dictionary from the 'BaseCaching' parent class.
    """
    def put(self, key, item):
        """ Add an item, 'item' to the cache dictionary with key, 'key'. """
        if key is None or item is None:
            return

        self.cache_data[f"{key}"] = item

        return

    def get(self, key):
        """ Returns the value in the cache dictionary linked to 'key'. """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[f"{key}"]
