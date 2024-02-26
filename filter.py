import datetime

class Filter:
    @staticmethod
    def string_contains(target_string):
        return lambda value: isinstance(value, str) and target_string in value

    @staticmethod
    def numeric_greater_than(threshold):
        return lambda value: isinstance(value, (int, float)) and value > threshold

    @staticmethod
    def date_range(start_date, end_date):
        return lambda value: isinstance(value, datetime.date) and start_date <= value <= end_date

    @staticmethod
    def boolean_equals(target_boolean):
        return lambda value: isinstance(value, bool) and value == target_boolean
    
    @staticmethod
    def most_frequent_items(storage, limit=5):
        """
        Filter to retrieve the most frequently used items from the storage.

        :param storage: The TemporaryStorage object.
        :param limit: The maximum number of items to retrieve.
        :return: A dictionary containing the most frequently used items.
        """
        # Count the frequency of each value in the storage
        frequency_count = {}
        for value in storage.data.values():
            if value in frequency_count:
                frequency_count[value] += 1
            else:
                frequency_count[value] = 1

        # Sort the items by frequency in descending order
        sorted_items = sorted(frequency_count.items(), key=lambda x: x[1], reverse=True)

        # Get the most frequently used items up to the specified limit
        most_frequent_items = dict(sorted_items[:limit])

        return most_frequent_items
