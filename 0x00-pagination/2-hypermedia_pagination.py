#!/usr/bin/env python3
""" Module containing the 'index_range' function and 'Server' class. """
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
    """
    start_index = (page * page_size) - page_size
    end_index = page * page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Returns the appropriate page of the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)
        if start_index < 0 or end_index > len(dataset) - 1:
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Returns a dictionary containing the following key-value pairs:
            'page_size': the length of the returned dataset page
            'page': the current page number
            'data': the dataset page (equivalent to return from previous task)
            'next_page': number of the next page, None if no next page
            'prev_page': number of the previous page, None if no previous page
            'total_pages': the total number of pages in the dataset (int)
        """
        dataset = self.dataset()
        page_list = self.get_page(page, page_size)

        page_info_dict = {
            'page_size': page_size,
            'page': page,
            'data': page_list,
            'next_page': page + 1 if len(page_list) < page else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(len(dataset) / page_size)
        }

        return page_info_dict
