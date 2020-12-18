from sklearn.utils import murmurhash3_32  # From what I could tell, this implementation does guarantee the
# simple-uniform hash assumption


def bloom_hash(key, index, table_size):
    """ This method is hashing the items that go in the filter using sci-kit learn's murmurhash3 implementation

    :param key: The key to hash
    :param index: The index of the hash function, ranges from 1 to k
    :param table_size: the total size of the bloom filter, m
    :return: The hash value
    """

    # I tried using sklearn's murmurhash implementation, and defining the i-th hash function as just the murmurhash,
    # seeded with i. i.e.  "return murmurhash3_32(key, index, positive=True) % table_size"
    # But, the correlation seemed a bit high (got very alike hashes for i and (i + 1) for some reason).
    # So, I'm now using python's built in hash function as the seed to the murmurhash in an attempt to
    # reduce the correlation and make the hashes more distinct.
    return murmurhash3_32(key, hash(index), positive=True) % table_size
