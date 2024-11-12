import os
import hashlib

class BloomFilter:

    def __init__(self, size=1000, num_hashes=3, file_name="bloom_filter_data.txt") -> None:
        self.size = size
        self.num_hashes = num_hashes
        self.file_name = file_name
        self.bit_array = [0] * size
        self.current_path = os.getcwd()
        self.load_filter()

    def _hasher(self, item):
        hash_values = []
        for i in range(self.num_hashes):
            hash_value = int(hashlib.sha256(f"{item}{i}".encode()).hexdigest(), 16) % self.size
            hash_values.append(hash_value)

        return hash_values
    
    def add(self, item):
        for hash_value in self._hasher(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        for has_value in self._hasher(item):
            if self.bit_array[has_value] == 0:
                return False
        return True

    def save_filter(self):
        file_path = os.path.join(self.current_path, self.file_name)
        with open(file_path, 'w') as f:
                f.write(''.join(map(str, self.bit_array)))

    def load_filter(self):
        file_path = os.path.join(self.current_path, self.file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                self.bit_array = list((map(int, f.read())))
            



bloom_filter = BloomFilter(size=10000, num_hashes=3)
email = "rohitgajula27@gmail.com"
if bloom_filter.check(email):
    print("Exists!")
else:
    bloom_filter.add(email)
    bloom_filter.save_filter()
    print("Added!")


