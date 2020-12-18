from bloom_filter import BloomFilter
from bitarray import bitarray
from IO_handling import *


if __name__ == '__main__':
    print('This is a basic demonstration of a \'bloom-filter\' implementation, allowing insertion and lookup.\n')

    k, m = get_filter_attrs()  # Get the filter attributes from the user.
    T = BloomFilter(bitarray('0') * m, m, k)  # Initialize the bloom-filter.

    print('\nyou\'ll now be asked to enter the name of the file including the numbers to insert to the filter.')
    input_list = get_input_numbers()  # Get the numbers to insert to the bloom-filter.
    n = len(input_list)
    for key in input_list:
        T.insert(key)  # For each key, insert it.

    print(f'\nBloom filter successfully created and filled with {n} keys and {k} hash functions were used.\n'
          f'The first 100 keys (or less) are {input_list[:100]}\n')

    print('\nyou\'ll now be asked to enter the name of the file including the numbers to search for.')
    search_for_list = get_input_numbers()  # Get the numbers to lookup in the bloom-filter
    lookup_mask = [T.lookup(key) for key in search_for_list]  # Make some sort of a mask containing 'True' or 'False'
    # in each index, corresponding to if the number at that index was found in the filter.

    write_output_file(search_for_list, lookup_mask, n, T.m, T.k)  # Write the output file
