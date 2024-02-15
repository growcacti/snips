import random

def generate_random_tuples(n, tuple_size, num_range):
    """
    Generate a list of random tuples.

    Parameters:
    n (int): number of tuples in the list.
    tuple_size (int): number of elements in each tuple.
    num_range (tuple): a tuple of two integers (a, b) where each random number will be in the range [a, b].

    Returns:
    list: a list of random tuples.
    """
    
    return [tuple(random.randint(num_range[0], num_range[1]) for _ in range(tuple_size)) for _ in range(n)]

# Example usage:
n = 5  # Number of tuples
tuple_size = 3  # Number of elements in each tuple
num_range = (1, 10)  # Range of random numbers

print(generate_random_tuples(n, tuple_size, num_range))
