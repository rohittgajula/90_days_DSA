

import hashlib
import math

class BloomFilter:
    def __init__(self, n, p):
        """
        Initialize the Bloom filter.
        
        Parameters:
        n : int
            The expected number of items to be stored in the Bloom filter.
        p : float
            The desired false positive probability.
        """
        self.size = self.get_size(n, p)
        self.hash_count = self.get_hash_count(self.size, n)
        self.bit_array = [0] * self.size

    def add(self, item):
        """
        Add an item to the Bloom filter.
        
        Parameters:
        item : str
            The item to be added to the filter.
        """
        for i in range(self.hash_count):
            digest = self.hash(item, i)
            self.bit_array[digest % self.size] = 1

    def check(self, item):
        """
        Check if an item is in the Bloom filter.
        
        Parameters:
        item : str
            The item to be checked.
        
        Returns:
        bool
            True if the item might be in the filter, False if the item is definitely not in the filter.
        """
        for i in range(self.hash_count):
            digest = self.hash(item, i)
            if self.bit_array[digest % self.size] == 0:
                return False
        return True

    def hash(self, item, i):
        """
        Generate a hash for an item with a specific seed.
        
        Parameters:
        item : str
            The item to be hashed.
        i : int
            The seed for hashing.
        
        Returns:
        int
            The hash result.
        """
        return int(hashlib.md5((item + str(i)).encode()).hexdigest(), 16)

    @staticmethod
    def get_size(n, p):
        """
        Calculate the size of the bit array for given false positive probability and number of items.
        
        Parameters:
        n : int
            The expected number of items.
        p : float
            The desired false positive probability.
        
        Returns:
        int
            The size of the bit array.
        """
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    @staticmethod
    def get_hash_count(m, n):
        """
        Calculate the number of hash functions needed.
        
        Parameters:
        m : int
            The size of the bit array.
        n : int
            The number of items expected to be inserted.
        
        Returns:
        int
            The number of hash functions.
        """
        k = (m / n) * math.log(2)
        return int(k)

# Example Usage
n = 20  # Expected number of items to be added
p = 0.05  # Desired false positive probability

bloom_filter = BloomFilter(n, p)
elements_to_add = ["apple", "banana", "cherry"]
elements_to_check = ["apple", "banana", "date"]

# Adding elements to the Bloom filter
for item in elements_to_add:
    bloom_filter.add(item)

# Checking for element existence
for item in elements_to_check:
    if bloom_filter.check(item):
        print(f"{item} might be in the set")
    else:
        print(f"{item} is definitely not in the set")
