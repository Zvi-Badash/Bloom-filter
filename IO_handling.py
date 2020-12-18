import csv
from itertools import compress


def get_filter_attrs():
    """
    This method gets m & k from the user, and returns them
    :return: A tuple, (k, m)
    """

    hash_no = input('Enter the number of hash functions you\'d to use (k): ')
    size = input('Enter the size of the filter i.e. the number of cells in it you\'d like to use (m): ')

    return int(hash_no), int(size)


def get_input_numbers():
    """
    This method gets a file name from the user, and returns it's content as a list
    :return: The list of values in said file
    """
    in_file_name = input('Enter the name of the input file, for example \'in.txt\' or \'in.csv\': ')

    with open(in_file_name, 'r') as f:
        reader = csv.reader(f)  # Using the 'comma-separated-values' library to parse the file
        values = list(reader)

    return [int(item) for sublist in values for item in sublist]  # The csv library returns a list of lists, and it
    # needs to be flattened into a single, 1D list


def write_output_file(lookup_numbers, lookup_mask, n, m, k):
    error = (1 - ((1 - 1 / m) ** (k * n))) ** k  # The value of \epsilon, or the chance for a false positive
    out_file_name = input('Enter the name of the output file, for example \'out.txt\', '
                          'if it doesn\'t exist, it will be created for you. If you wish only to print the results, '
                          'press ENTER: ')  # Get the file name

    output_string = f"""This is the output file containing the results of the lookup in the bloom-filter.

The numbers you searched for were: {lookup_numbers}
The numbers found in the bloom-filter were: {list(compress(lookup_numbers, lookup_mask))}



============================================== SOME STATISTICS ==============================================
The attributes of this bloom-filter are: size (m): {m}, hash functions no. (k): {k}, actual number of elements (n): {n}
Out of the {len(lookup_numbers)} numbers you looked up, {lookup_mask.count(True) / len(lookup_numbers):2.3%} were found.

The bloom-filter lookup may report false positives with an *approximated* {error:20.20%}
chance, but it will not report any true negatives.
                 """
    print('\n\n' + output_string)  # Print the results to the standard output
    if out_file_name == '':
        return

    with open(out_file_name, 'w') as f:
        f.write(output_string)  # Print the results to the output file
