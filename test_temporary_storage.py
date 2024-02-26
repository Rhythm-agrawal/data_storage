import unittest
from datetime import date
from filter import Filter
from temporary_storage import TemporaryStorage

class TestTemporaryStorage(unittest.TestCase):
    def setUp(self):
        self.storage = TemporaryStorage()

    def test_create_read(self):
        self.storage.create("name", "Alice")
        self.assertEqual(self.storage.read("name"), "Alice")

    def test_update(self):
        self.storage.create("age", 25)
        self.storage.update("age", 26)
        self.assertEqual(self.storage.read("age"), 26)

    def test_delete(self):
        self.storage.create("city", "New York")
        self.storage.delete("city")
        self.assertIsNone(self.storage.read("city"))

    def test_filter_string_contains(self):
        self.storage.create("name", "Alice")
        self.storage.create("name2", "Bob")
        self.storage.create("city", "New York")
        filtered_data = self.storage.filter(Filter.string_contains("Alice"))
        self.assertEqual(filtered_data, {"name": "Alice"})

    def test_filter_numeric_greater_than(self):
        self.storage.create("age", 25)
        self.storage.create("age2", 30)
        filtered_data = self.storage.filter(Filter.numeric_greater_than(26))
        self.assertEqual(filtered_data, {"age2": 30})

    def test_filter_date_range(self):
        self.storage.create("dob", date(1990, 5, 15))
        self.storage.create("dob2", date(1985, 8, 10))
        filtered_data = self.storage.filter(Filter.date_range(date(1986, 1, 1), date(1995, 12, 31)))
        self.assertEqual(filtered_data, {"dob": date(1990, 5, 15)})

    def test_filter_boolean_equals(self):
        self.storage.create("active", True)
        self.storage.create("active2", False)
        filtered_data = self.storage.filter(Filter.boolean_equals(True))
        self.assertEqual(filtered_data, {"active": True})

    def test_filter_most_frequent_items(self):
        self.storage.create("item1", "A")
        self.storage.create("item2", "A")
        self.storage.create("item3", "B")
        self.storage.create("item4", "C")
        self.storage.create("item5", "C")

        # Filter for the top 2 most frequent items
        filtered_data = Filter.most_frequent_items(self.storage, limit=2)
        self.assertEqual(filtered_data, {"A": 2, "C": 2})


if __name__ == "__main__":
    unittest.main()
