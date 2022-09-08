class TimeMap:
    """
    Design a time-based key-value data structure that can store multiple values for the same key at different time
    stamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:
        - TimeMap(): Initializes the object of the data structure.
        - void set(String key, String value, int timestamp): Stores the key with the value at the given time
        timestamp.
        - String get(String key, int timestamp): Returns a value such that set was called previously,
        with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the
        largest timestamp_prev. If there are no values, it returns "".

    Faster than 67.96% of solutions.

    Less memory than 21.99% of solutions.
    """

    def __init__(self):
        """
        Initializes the object of the data structure.
        """
        self.store = {}  # key = string, value = list of [values, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key with the value at the given time timestamp.

        :param key: The key for the data structure.
        :type key: Str.
        :param value: The value to be associated with the key.
        :type value: Str.
        :param timestamp: The timestamp to be associated with the value.
        :type timestamp:  Int.
        :return: NoneType.
        :rtype: NoneType.

        The time complexity is O(1) to check if the key is in the hashmap already.

        The space complexity is O(N) for the data structure.
        """
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple
        such values, it returns the value associated with the largest timestamp_prev. If there are no values,
        it returns "".

        :param key: The key for the data structure.
        :type key: Str.
        :param timestamp: The timestamp associated with the value.
        :type timestamp: Int.
        :return: The string representation of the value at the given key and timestamp.
        :rtype: Str.

        The time complexity is O(LOG(N)) for the binary search.

        The space complexity is O(1) as we don't use any additional data structures.
        """
        res = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1

        # we can use binary search as values is sorted by timestamp
        while l <= r:
            m = l + (r - l) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
