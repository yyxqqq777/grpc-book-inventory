# test.py

import unittest
from unittest.mock import Mock
import sys

# please change the path!!!!
sys.path.insert(0, '/Users/yunxuan/Desktop/f22/api_design/hw/a3/service')
import book_pb2

from inventory_client import InventoryClient
from get_book_titles import get_book_titles


class TestGetBookTitles(unittest.TestCase):
    def test_get_book_titles_mock(self):
        mock_client = Mock(spec=InventoryClient)
        mock_client.get_book.return_value = book_pb2.Book(title="Test Book")
        # Call the get_book_titles function using the mock client
        titles = get_book_titles(mock_client, ["978-0439708180"])

        # Assert that the mock method was called with the expected value
        mock_client.get_book.assert_called_with("978-0439708180")

        # Assert the return is correct
        self.assertEqual(titles, ["Test Book"])

    def test_get_book_titles_live(self):
        client = InventoryClient("localhost", 8082)
        # Call the get_book_titles function using a real client
        titles = get_book_titles(client, ["978-0439708180"])

        # Assert the return is correct
        self.assertEqual(titles, ["Harry Potter and the Sorcerer's Stone"])


if __name__ == "__main__":
    unittest.main()
