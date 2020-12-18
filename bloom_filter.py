from logic import bloom_hash


class BloomFilter:
    def __init__(self, bits, m, k):  # Initialize the bloom-filter with m, k and the bit values in it.
        self.m = m
        self.k = k
        self.bits = bits

    def insert(self, key):
        """ Inserts a key to the bloom-filter
        :param key: The key to insert
        """
        for i in range(1, self.k + 1):  # For each hash function
            self.bits[bloom_hash(key, i, self.m)] = True  # Turn on the bit for the current hash function

    def lookup(self, key):
        """ Searches a key in the bloom-filter, with a slight chance for a false-positive
        :param key: The key to search for
        :return: True or False, False for "definitely not on the nloom-filter"
        and True for "Probably in the bloom-filter"
        """
        does_exist = True
        for i in range(1, self.k + 1):  # For each hash function
            if self.bits[bloom_hash(key, i, self.m)] is False:  # If even one of the bits bloom_hash(key, i, m) is off
                does_exist = False  # The key is certainly not in the bloom-filter
        return does_exist

    def __repr__(self):
        # mainly for internal use, used for debugging and testing
        return f'A bloom-filter of size {self.m}\n{[int(self.bits[i]) for i in range(self.bits.length())]}'
