from operator import itemgetter

from pymath.perfect_numbers import divisor_generator


def is_deficient(n):
    """
    Checks if a number is deficient, i.e. has sum of divisors that is less than n
    Example:

    >>> is_deficient(35)
    True

    :param n: Number to check for deficiency
    :type n int
    :return: True if the sum is less than the number, False otherwise
    :rtype: bool
    """

    return sum_of_divisors(n) < n


def is_abundant(n):
    """
    Checks if a number is abundant, i.e. has sum of divisors that exceed n
    Example:

    >>> is_abundant(12)
    True

    :param n: Number to check for abundancy
    :type n int
    :return: True if the sum exceeds the number, False otherwise
    :rtype: bool
    """
    return sum_of_divisors(n) > n


def sum_of_divisors(n):
    return sum(divisor_generator(n)) + 1


def abundance_of_num(n):
    return sum_of_divisors(n) - n


def abundance(n):
    if n == 0:
        return []

    abundant_numbers = []
    start_number = 12

    while len(abundant_numbers) < n:
        if is_abundant(start_number):
            abundant_numbers.append((start_number, abundance_of_num(start_number)))
        start_number += 1

    return list(map(itemgetter(0), sorted(abundant_numbers, key=lambda x: x[1])))


def rebase(baseA, numbers, baseB):
    """
    converts a list of numbers from basA to baseB
    :param baseA: the base to convert from
    :param numbers: list of numbers to convert
    :param baseB: the base to convert to
    :return: list of numbers converted to baseB
    :rtype: list
    """
    if baseA < 2 or baseB < 2:
        raise ValueError("Invalid base")
    if any(True for num in numbers if num < 0 or num >= baseA):
        raise ValueError("Invalid number input")
    return convert_to_digits(convert_from_digits(numbers, baseA), baseB)


def convert_from_digits(digits, base):
    """
    calculates the sum of the numbers in the list by evaluating their base
    :param digits: digits to convert
    :param base: the base to convert the number to
    :return: an integer
    :rtype: int
    """
    return sum(num * base**indx for indx, num in enumerate(reversed(digits)))


def convert_to_digits(number, base):
    """
    Converst the number to base provided
    :param number: the number to convert
    :param base: the base to convert the number to
    :return: a list of converted numbers to the given base
    :rtype: list
    """
    output = []
    while number > 0:
        output.append(number % base)
        number //= base
    return list(reversed(output))


def sum_amicable_numbers(limit):
    """
    Sums all amicable numbers under the given limit
    :param limit: Upper Limit to find sum of all amicable numbers
    :return: sum of all amicable numbers under given limit
    :rtype: int
    """
    amicable_numbers = set()
    for number in range(limit):
        if number not in amicable_numbers:
            sum_1 = sum_of_divisors_of_number(number)

            sum_2 = sum_of_divisors_of_number(sum_1)

            if number == sum_2 and number != sum_1:
                amicable_numbers.add(number)

    return sum(amicable_numbers)


def sum_of_divisors_of_number(number):
    return sum([x for x in range(1, number) if number % x == 0])


class Divisible5(object):
    def __init__(self, binary_lst):
        self.binary_lst = binary_lst

    def div_five(self):
        return ",".join([x for x in self.binary_lst.split(",") if int(x, 2) % 5 == 0])

    def div_five_tw0(self):
        lst = []
        for x in self.binary_lst.split(","):
            if int(x, 2) % 5 == 0:
                lst.append(x)
        return ",".join(lst)


# TODO: implement parse binary
def parse_binary(num_str):
    pass


def count_bits(n):
    return "{0:b}".format(n).count("1")


def binary_converter(number):
    try:
        return "{0:b}".format(number) if number in range(0, 256) else "Invalid input"
    except TypeError:
        return "Invalid input"


def add_binary(a, b):
    return "{0:b}".format(a + b)


import binascii


class HexToDex(object):
    def __init__(self, hex_string):
        self.hex_string = hex_string

    def hex_to_dec(self):
        return int(self.hex_string, 16)

    # alternative version using binascii
    def hex_to_dec_binascii(self):
        return int.from_bytes(
            binascii.unhexlify(("0" * (len(self.hex_string) % 2)) + self.hex_string),
            byteorder="big",
        )


def calculate_total(books, price_thus_far=0.0):
    """
    Calculates the total amount that one can get from the books. Should return the least discount
    one can get from the book titles
    :param books: list of books
    :param price_thus_far: price so far
    :return: least price from the set of books purchased
    """
    if not books:
        return price_thus_far

    groups = list(set(books))
    min_price = float("inf")

    for x in range(len(groups)):
        # create a copy of the books
        books_remaining = books[:]

        for y in groups[: x + 1]:
            books_remaining.remove(y)

        # calculate the price on the remaining books
        price = calculate_total(books_remaining, price_thus_far + group_price(x + 1))

        # get the minimum price discount
        min_price = min(min_price, price)

    return min_price


def group_price(size):
    """
    Calculates group price of books
    :param size: size of the books
    :return: price of the group of books
    """
    discounts = [0, 0.05, 0.1, 0.2, 0.25]
    if not (0 < size <= 5):
        ValueError("Size must be in range 1...{}".format(len(discounts)))
    return 8 * size * (1 - discounts[size - 1])


TAX_RATES = {
    0 / 100: range(0, 1001),
    10 / 100: range(1000, 10001),
    15 / 100: range(10000, 20201),
    20 / 100: range(20200, 30751),
    25 / 100: range(30750, 50001),
}


# , 30: 50000


def calculate_tax(people_sal):
    """
    Calculate the annual tax

    :param people_sal:
    :return:
    """
    result = {}
    # for each key-value pair in TAX_RATES, calculate the rate
    for tax_rate, band in TAX_RATES.items():
        diff = max(band) - min(band)
        for person, salary in people_sal.items():
            if salary > 50000:
                salary *= 0.3
            # check if the salary is greater than max possible in band
            if salary > max(band):
                rate = tax_rate * diff
                results(person, result, rate)
                salary -= diff
                # remaining salary
            elif salary < max(band):
                rate = (salary - min(band)) * tax_rate
                results(person, result, rate)
                break
    return result


def results(person, result, rate):
    """
    Checks if the current person is in the dict, if not adds them with their current rate
    if they are, adds the current rate to the current person
    :param person: the current person
    :param result: the output result
    :param rate: the current tax rate
    :return: the resulting dict
    """
    if person in result:
        result[person] += int(rate)
    else:
        result[person] = int(rate)
    return result


print(calculate_tax({"James": 20500, "Alex": 500, "Kinuthia": 70000}))


def zero(operation=None):
    if operation is None:
        return 0
    return int(eval(f"0 {operation}"))


def one(operation=None):
    if operation is None:
        return 1
    return int(eval(f"1 {operation}"))


def two(operation=None):
    if operation is None:
        return 2
    return int(eval(f"2 {operation}"))


def three(operation=None):
    if operation is None:
        return 3
    return int(eval(f"3 {operation}"))


def four(operation=None):
    if operation is None:
        return 4
    return int(eval(f"4 {operation}"))


def five(operation=None):
    if operation is None:
        return 5
    return int(eval(f"5 {operation}"))


def six(operation=None):
    if operation is None:
        return 6
    return int(eval(f"6 {operation}"))


def seven(operation=None):
    if operation is None:
        return 7
    return int(eval(f"7 {operation}"))


def eight(operation=None):
    if operation is None:
        return 8
    return int(eval(f"8 {operation}"))


def nine(operation=None):
    if operation is None:
        return 9
    return int(eval(f"9 {operation}"))


def plus(number):
    return f"+ {number}"


def minus(number):
    return f"- {number}"


def times(number):
    return f"* {number}"


def divided_by(number):
    return f"/ {number}"


def circle_of_numbers(n: int, first_number: int) -> int:
    """
    First off, to get to other side, first off you'd want to divide n by 2, then offset it by firstNumber. To account
    for the rotation, you basically want to find the remainder after dividing it because it's always goin to a value
    between 0 and n, which is where modulus comes in.
    """
    return (first_number + (n // 2)) % n


def climb(n):
    c, new_l, n_range = 0, [], list(range(1, n + 1))
    # if n is odd
    if n == 1 or n == 0:
        return new_l.append(n)
    if n % 2 != 0:
        i = (n - 1) / 2
        new_l.append(i)
        # i is now even
        if i % 2 == 0:
            i = i / 2
            new_l.append(i)
        new_l = list(reversed(new_l))
    # else if n is even
    else:
        i = n / 2
        new_l.append(i)
        # i is now odd
        if i % 2 != 0:
            i = (i - 1) / 2
            new_l.append(i)

        new_l = list(reversed(new_l))


def make_pounds(coins, bill):
    """
    Find how many ways there are to make bill from the given list of coins
    :param coins List of coins
    :type coins list
    :param bill Coin/note to make change for
    :type bill int
    :return: Number of ways to make change for the given currency
    :rtype: int
    """
    ways_to_make_bill = [0] * (bill + 1)
    ways_to_make_bill[0] = 1

    for x in range(len(coins)):
        for n in range(coins[x], bill + 1):
            ways_to_make_bill[n] += ways_to_make_bill[n - coins[x]]

    return ways_to_make_bill[bill]


if __name__ == "__main__":
    c = [1, 2, 5, 10, 20, 50, 100, 200]
    b = 200
    ways_to_make_b = make_pounds(c, b)
    print(f"There are {ways_to_make_b} ways to make change for {b} given {c}")
"""
Collatz sequence
finds the starting number under 1M that produces the longest chain
"""
import random


def generate_collatz_sequence(number):
    """
    Generates a Collatz sequence from the starting number
    Example(s)

    >>> generate_collatz_sequence(1)
    [1]

    >>> generate_collatz_sequence(2)
    [2, 1]

    >>> generate_collatz_sequence(13)
    [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    :param number: Starting number
    :return: list of collatz sequence from the starting number
    :rtype: list
    """

    if number is None or not isinstance(number, int):
        raise ValueError(f"Invalid input {number}, this should be an integer")

    sequence = [number]

    if number == 1:
        return sequence

    # if the number is already 1, return it in a list
    while number != 1:
        # if the number is even, ie. number %2 == 0
        if number % 2 == 0:
            number //= 2
            sequence.append(number)

        # if number is odd
        elif number % 2 != 0:
            number = (3 * number) + 1
            sequence.append(number)

    return sequence


# TODO: add memoization to not repeat calculations for sequences, increases speed and reduces call count
def find_starting_number(limit):
    """
    Finds the starting number in a collatz seqence that produces the longest chain
    Example:

    >>> find_starting_number(1000000)
    837799

    :param limit This defines the limit we want to start checking for the starting point with the longest collatz seq
    :return: Starting number with the longest collatz sequence
    :rtype: int
    """
    if limit < 0 or limit is None:
        raise ValueError(
            f"Expected limit to be greater than one or not None instead found {limit}"
        )

    if limit == 1:
        # short circuit, we already have the starting point
        return limit

    # cache = {}
    current_longest = 0
    starting_num = 0
    for x in range(limit, 1, -1):
        sequence = generate_collatz_sequence(x)
        seq_len = len(sequence)

        # cache[x] = sequence
        if seq_len > current_longest:
            current_longest = seq_len
            starting_num = x
    return starting_num


if __name__ == "__main__":
    range_limit = 1000000
    starting_number = find_starting_number(range_limit)
    print(
        f"Starting number with the longest collatz seq under {range_limit} is {starting_number}"
    )


class Complex(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        s = Complex()
        s.real = self.real + other.real
        s.imag = self.imag + other.imag
        return s

    def __sub__(self, other):
        s = Complex()
        s.real = self.real - other.real
        s.imag = self.imag - other.imag
        return s

    def __mul__(self, other):
        s = Complex()
        s.real = self.real * other.real - self.imag * other.imag
        s.imag = self.real * other.imag + self.imag * other.real
        return s

    def __truediv__(self, other):
        s = Complex()
        s.real = (self.real * other.real + self.imag * other.imag) / (
            other.real**2 + other.imag**2
        )
        s.imag = (self.imag * other.real - self.real * other.imag) / (
            other.real**2 + other.imag**2
        )
        return s

    def mod(self):
        s = Complex()
        s.real = math.sqrt(self.real**2 + self.imag**2)
        return s

    def __str__(self):
        return "{0:.2f}{1:+.2f}i".format(self.real, self.imag)


from math import sqrt
from typing import List


def construct_rectangle(area: int) -> List[int]:
    w = int(sqrt(area))

    while area % w != 0:
        w -= 1

    return [area // w, w]


def convert_to_mixed_numeral(parm):
    numerator, denominator = parm.split("/")
    num, dem = int(numerator), int(denominator)
    divide, mod = int(num / dem) or "", int(abs(num) % dem) or 0

    if bool(divide) and bool(mod):
        return "%s %s/%s" % (divide, mod, denominator)
    else:
        return (
            "%s/%s" % (int(mod) if num > 0 else int(-mod), int(denominator))
            if bool(mod)
            else str(divide)
        )


from math import gcd


def coprime(a, b):
    return True if gcd(a, b) == 1 else False


def cycle(n):
    if n % 2 == 0 or not coprime(n, 10):
        return -1

    rem = 1

    for _ in range(1, n + 2):
        rem = (10 * rem) % n

    d = rem
    count = 0
    rem = (10 * rem) % n
    count += 1

    while rem != d:
        rem = (10 * rem) % n
        count += 1

    return count


from pymath.primes.is_prime import is_prime
from pymath.primes.sieve_of_erastothenese import sieve


def find_cyclic_primes(start, limit):
    """
    Finds all cyclic primes in a given range
    :param start: Start of range
    :param limit: Limit to find the cyclic primes
    :return: List of all cyclic primes
    :rtype: list
    """
    all_primes = sieve(limit, start)
    cyclic_primes = []

    for prime in all_primes:
        if is_prime_cyclic(prime):
            cyclic_primes.append(prime)

    return cyclic_primes


def find_number_of_cyclic_primes(start, limit):
    """
    Find the number of cyclic primes within the range or 0 to the given limit
    :param limit: Limit to find cyclic primes to
    :param start: the range to start from
    :return: Integer with the number of primes within the given range
    """
    return len(find_cyclic_primes(start, limit))


def find_sum_of_cyclic_primes(start, limit):
    """
    Finds the number of cyclic primes in a given range
    :param start: Where start is the start of the range
    :param limit: Limit is the end of the range
    :return: sum of cyclic primes in a given range
    :rtype: int
    """
    return sum(find_cyclic_primes(start, limit))


def is_prime_cyclic(prime):
    """
    Checks if a prime number is cyclic
    :param prime: Prime number
    :return: Boolean value True if cyclic, False otherwise
    """
    if not prime:
        return False
    else:
        # rotate the prime number
        number_str = str(prime)
        rotations = len(number_str) - 1

        for _ in range(rotations):
            number_str = number_str[-1] + number_str[:-1]
            if not is_prime(int(number_str)):
                return False
        return True


def rotate(num):
    n = str(num)
    return n[1:] + n[:1]


from math import ceil, log


def evaporator(content, evap_per_day, threshold):
    nth_day = 0
    limit = content * (threshold / 100)

    while content >= limit:
        content -= content * (evap_per_day / 100)
        nth_day += 1

    return nth_day


def evaporator_2(content, evap_per_day, threshold):
    return ceil(log(threshold / 100.0) / log(1.0 - evap_per_day / 100.0))


def square_of_sum(n):
    return sum(range(n + 1)) ** 2


def sum_of_squares(n):
    return sum([x**2 for x in range(n + 1)])


def difference(d):
    return square_of_sum(d) - sum_of_squares(d)


def nb_dig(n, d):
    squares = [x**2 for x in range(0, n + 1)]
    return sum([str(i).count(str(d)) for i in squares if str(d) in str(i)])


def digit_nth_power(nth):
    """
    Finds the sum of all numbers that can be written as the sum of nth power of their digits.
    Uses Brute force to find the sum of all numbers. We first need to find the limit/upper bound. To do that we
    The highest digit is 9  and 9^5=59049 , which has five digits. If we then look at 5 \times 9^5=295245 ,
    which has six digits and a good endpoint for the loop (in the case of nth = 5)

    >>> digit_nth_power(4)
    19316

    :param nth: Power of each digit
    :type nth int
    :return: sum of all numbers
    :raises: ValueError
    :rtype: int
    """
    if nth is None or not isinstance(nth, int):
        raise ValueError("Expected nth power to be an integer")

    # this finds the limit we will use for brute force
    limit = 6 * 9**nth

    result = []

    for number in range(10, limit):
        total = 0
        number_str = str(number)

        total += sum(int(num) ** nth for num in number_str)

        if total == number:
            result.append(number)

    return sum(result)


if __name__ == "__main__":
    power = 5
    sum_of_numbers = digit_nth_power(power)
    print(
        f"Sum of all numbers that can be written as the sum of {power} of their digits is {sum_of_numbers}"
    )
"""
Finds how many distinct powers generated by a^b given the range  2 ≤ a ≤ n and 2 ≤ b ≤ n
where n is a positive integer
"""


def distinct_powers(a, b):
    """
    Finds and returns the number of distinct powers of a and b

    Example:
    >>> distinct_powers(5, 5)
    15

    :param a: Limit of a
    :type a int
    :param b: limit of b
    :type b int
    :return: number of distinct powers
    :rtype: int
    """

    # sanity checks
    if a is None or b is None:
        raise ValueError("Expected a or b to be an integer")

    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Expected a or b to be a integer")

    powers = set(m**n for m in range(2, a + 1) for n in range(2, b + 1))

    return len(powers)


if __name__ == "__main__":
    x = 100
    y = 100
    no_of_distinct_powers = distinct_powers(x, y)
    print(f"Distinct powers given a={x} and b ={y} is {no_of_distinct_powers}")


class Divisible7(object):
    """
    class that gets all the numbers divisible by 7, but not by 5 in a range
    """

    def __init__(self, rnge):
        self.rnge = rnge

    def div7(self):
        return ",".join([str(x) for x in self.rnge if x % 7 == 0 and x % 5 != 0])

    # solution two
    def div7_two(self):
        l = []
        for i in self.rnge:
            if (i % 7 == 0) and (i % 5 != 0):
                l.append(str(i))
        return ",".join(l)


lst = Divisible7(range(2000, 3201))
print(lst.div7())


class EvenDigits(object):
    def __init__(self, number_range):
        self.number_range = number_range

    def evens(self):
        return ",".join(
            [
                str(x)
                for x in self.number_range
                if int(str(x)[0]) % 2 == 0
                and int(str(x)[1]) % 2 == 0
                and int(str(x)[2]) % 2 == 0
            ]
        )


evn = EvenDigits(range(1000, 3001))
print(evn.evens())


def evil(n):
    return "It's Evil!" if "{0:b}".format(n).count("1") % 2 == 0 else "It's Odious!"
    # return "It's %s!" % ["Evil","Odious"][bin(n).count("1")%2]


def expanded_form(num):
    """
    Expands the form of a number placing all digits in the number into their place values
    :param num: Integer
    :return String representation of the number broken down into its place values
    :rtype: str
    """
    str_num = str(num)
    length = len(str_num)
    result = []

    for digit in str_num:
        if digit != "0":
            result.append(str(int(digit) * int("1{}".format("0" * (length - 1)))))
        length -= 1

    return " + ".join(result)


def expanded_form_2(num):
    """Second implementation of expanded form"""
    result = []
    for a in range(len(str(num)) - 1, -1, -1):
        current = 10**a
        quo, num = divmod(num, current)

        if quo:
            result.append(str(quo * current))

    return " + ".join(result)


from functools import wraps
from math import factorial as math_factorial, sqrt, pi, e


def memoize(func):
    cache = func.cache = {}

    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


def memodict(f):
    """Memoization decorator for a function taking a single argument"""

    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def stirling_approximation(num):
    """
    Uses Stirling approximation to find the factorial of a number. Will NOT return the exact factorial, but an
    approximation of it
    :param num: Number to get factorial of
    :type num int
    :return: Factorial approximation of num
    :rtype: float
    """
    return sqrt(2 * pi * num) * ((num / e) ** num)


# @memoize
def factorial(num):
    """
    find the factorial of the given number
    :param num: Number
    :return: Factorial of num
    :rtype: int
    """
    cache = {}

    if num in cache:
        return cache[num]

    if num == 0:
        return 1

    else:
        x = num * factorial(num - 1)
        cache[num] = x
        return x
    # return 1 if num == 0 else num * factorial(num - 1)


def factorial_digit_sum(num):
    """
    Finds the sum of the digits in the factorial of num

    An example:
    >>> factorial_digit_sum(10)
    27

    :param num: Number
    :type num int
    :return: sum of digits in the factorial of num
    :rtype: int
    """

    # sanity checks
    if num is None or not isinstance(num, (int, float)):
        raise ValueError(f"Expected number to be a number, instead got {num}")

    # convert to integer, in the case of floats
    num = int(num)

    # find the factorial of the number
    num_factorial = factorial(num)

    return sum(map(int, str(num_factorial)))


def factorial_length(num):
    """
    Finds the length of the factorial of number num

    >>> factorial_length(5)
    3

    :param num:
    :type num int
    :return: Length of factorial i.e. number of digits in factorial
    :rtype: int
    """
    n_factorial = math_factorial(num)

    return len(str(n_factorial))


def zeros(n: int) -> int:
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


def filter_me(num_list):
    evens = filter(lambda x: x % 2 == 0, num_list)
    return list(evens)


def median(lst):
    """
    func to find median in a list
    """
    sort_list = sorted(lst)
    med = 0
    if len(sort_list) == 1:
        med = sort_list[0]
    elif len(sort_list) % 2 == 0:
        f_mid_index = len(sort_list) / 2
        s_mid_index = f_mid_index - 1
        med = (sort_list[f_mid_index] + sort_list[s_mid_index]) / 2.0
    elif len(sort_list) % 2 != 0:
        f_mid_index = len(sort_list) / 2
        med = sort_list[f_mid_index]
    return med


# from itertools import cycle, zip, count, islice


class FizzBuzz(object):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def simple_fizz(self):
        out = []
        for i in range(1, self.endpoint + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(i)
        return out

    """
    Using String concatenation
    """

    def string_concat(self):
        return [
            "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i
            for i in range(1, self.endpoint)
        ]

    def string_concat_2(self):
        return [
            i % 3 // 2 * "Fizz" + i % 5 // 4 * "Buzz" or i + 1
            for i in range(self.endpoint)
        ]

    """
    You can also create a lazy, unbounded sequence by using generator expressions:
    """
    """
    def lazy(self):
        fizzes = cycle([""] * 2 + ["Fizz"])
        buzzes = cycle([""] * 4 + ["Buzz"])
        both = (f + b for f, b in izip(fizzes, buzzes))
        out = []
        # if the string is "", yield the number
        # otherwise yield the string
        fizzbuzz = (word or n for word, n in izip(both, count(1)))

        # print the first 100
        for i in islice(fizzbuzz, self.endpoint):
            out.append(i)
    """


"""
TESTS
Tests for the fizzbuzz challenges
"""
fizzy = FizzBuzz(10)
print(fizzy.simple_fizz())
"""
Gets the next prime number
"""

from math import sqrt


def get_next_prime(n):
    """
    Gets the next prime number from the given prime number
    :param n: Number
    :return: Next prime number in series
    :rtype: int
    """
    if n % 2 == 0:
        return 2
    for x in range(3, int(sqrt(n) + 1), 2):
        if n % x == 0:
            return x
    return n


def i_or_f(arr):
    try:
        return isinstance(float(arr), float) or isinstance(int(arr), int)
    except ValueError:
        return False


from fractions import Fraction


def sum_fracts(lst):
    """
    checks if the list is None of has no elements, returns None if so
    loops through each element in the list adding the fraction to the initialized total variable
    accumuletes this variable to the end of the list
    Perform checks for the denominator and numerator, returning either the whole number or the irreducible fraction
    :param lst: list of list with numerator and denominator
    :return: the irreducible form of the rational numbers
    """
    total, n = 0, 0
    if lst is None or len(lst) == 0:
        return None
    for fract in lst:
        total += Fraction(fract[0], fract[1])
    denom = total.denominator
    numer = total.numerator
    if denom is 1:
        return numer
    else:
        return [numer, denom]


def sum_fracts_2(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return (
            ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]
        )


def is_divisible(*args):
    f = args[0]
    return all(f % x == 0 for x in args[1:])


from typing import List


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Sort the points by distance, then take the closest K points.
    """
    points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
    return points[:k]


import heapq


class MaxProd(object):
    def __init__(self, array):
        self.array = array

    # slowest implementation
    def max_product_slow(self):
        n = sorted(self.array, reverse=True)
        return n[0] * n[1]

    # average of the three solutions
    def max_product_avg(self):
        count = 0
        m1 = m2 = float("-inf")
        for x in self.array:
            count += 1
            if x > m2:
                if x >= m1:
                    m1, m2 = x, m1
                else:
                    m2 = x
        return m1 * m2

    # faster solution
    def max_product_fast(self):
        first = max(self.array)
        second = max(n for n in self.array if n != first)
        return first * second

    # fastest solution
    def max_product_fastest(self):
        x = heapq.nlargest(2, self.array)
        return x[0] * x[1]


# fastest solution
def max_product(array):
    first = max(array)
    second = max(n for n in array if n != first)
    return second * first


"""
Finds the largest palindrome product of 2 n-digit nubers
"""


def find_largest_palindrome_product(n):
    """
    Finds the largest palindrome product of 2 n-digit numbers
    :param n: N digit number which specifies the number of digits of a given number
    :return: Largest Palindrome product of 2 n-digit numbers
    :rtype: int

    >>> find_largest_palindrome_product(2)
    9009
    """

    # first find the upper and lower limits for numbers with n digits
    upper_limit = 0

    for _ in range(1, n + 1):
        upper_limit *= 10
        upper_limit += 9

    # lower limit is 1 + the upper limit floor division of 10
    lower_limit = 1 + upper_limit // 10

    # initialize the max product
    max_product = 0

    for x in range(upper_limit, lower_limit - 1, -1):
        for y in range(x, lower_limit - 1, -1):
            product = x * y

            # short circuit early if the product is less than the max_product, no need to continue computation as this
            # already fails
            if product < max_product:
                break

            number_str = str(product)

            # check if this is a palindrome and is greater than the max_product currently
            if number_str == number_str[::-1] and product > max_product:
                max_product = product

    return max_product


"""
Finds the largest product of 4 adjacent numbers in a grid of 20x20 numbers
"""


def largest_product_in_grid(grid: list):
    """
    Finds the largest product of 4 adjacent numbers in a grid
    :param grid Grid of numbers,
    :return: Largest product of 4 adjacent numbers in a grid
    :rtype int
    """
    max_product = 0

    for x in range(20):
        for y in range(17):
            horizontal_product = (
                grid[x][y] * grid[x][y + 1] * grid[x][y + 2] * grid[x][y + 3]
            )
            vertical_product = (
                grid[y][x] * grid[y + 1][x] * grid[y + 2][x] * grid[y + 3][x]
            )

            if horizontal_product > max_product:
                max_product = horizontal_product

            if vertical_product > max_product:
                max_product = vertical_product

    for a in range(17):
        for b in range(17):
            diag_left_product = (
                grid[a][b]
                * grid[a + 1][b + 1]
                * grid[a + 2][b + 2]
                * grid[a + 3][b + 3]
            )
            diag_right_product = (
                grid[a][b + 3]
                * grid[a + 1][b + 2]
                * grid[a + 2][b + 1]
                * grid[a + 3][b]
            )

            if diag_left_product > max_product:
                max_product = diag_left_product

            if diag_right_product > max_product:
                max_product = diag_right_product

    return max_product


number_grid = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
]

if __name__ == "__main__":
    print(f"Largest product in a 20x20 grid {largest_product_in_grid(number_grid)}")
from functools import reduce


def largest_product(num_str, sub_length):
    """
    Passes the number string and substring length to the slice_me() function
    looping though each substring to obtain the maximum possible product
    :param num_str:
    :param sub_length:
    :return: largest product
    """
    return (
        max(reduce(lambda x, y: x * y, sli) for sli in slice_me(num_str, sub_length))
        if sub_length != 0
        else 1
    )


def slice_me(series, length):
    """
    Performs the validation for the length to slice through,
    if the length is out of the bound (1, len(series)) raise a ValueError
    else get consecutive substrings from the series
    :param series:
    :param length:
    :return: slices of the series
    """
    numbers = [int(digit) for digit in series]
    if not 1 <= length <= len(series):
        raise ValueError("Invalid length to slice %s" % str(length))
    return [numbers[i : i + length] for i in range(len(numbers) - length + 1)]


large_numbers = [
    37107287533902102798797998220837590246510135740250,
    46376937677490009712648124896970078050417018260538,
    74324986199524741059474233309513058123726617309629,
    91942213363574161572522430563301811072406154908250,
    23067588207539346171171980310421047513778063246676,
    89261670696623633820136378418383684178734361726757,
    28112879812849979408065481931592621691275889832738,
    44274228917432520321923589422876796487670272189318,
    47451445736001306439091167216856844588711603153276,
    70386486105843025439939619828917593665686757934951,
    62176457141856560629502157223196586755079324193331,
    64906352462741904929101432445813822663347944758178,
    92575867718337217661963751590579239728245598838407,
    58203565325359399008402633568948830189458628227828,
    80181199384826282014278194139940567587151170094390,
    35398664372827112653829987240784473053190104293586,
    86515506006295864861532075273371959191420517255829,
    71693888707715466499115593487603532921714970056938,
    54370070576826684624621495650076471787294438377604,
    53282654108756828443191190634694037855217779295145,
    36123272525000296071075082563815656710885258350721,
    45876576172410976447339110607218265236877223636045,
    17423706905851860660448207621209813287860733969412,
    81142660418086830619328460811191061556940512689692,
    51934325451728388641918047049293215058642563049483,
    62467221648435076201727918039944693004732956340691,
    15732444386908125794514089057706229429197107928209,
    55037687525678773091862540744969844508330393682126,
    18336384825330154686196124348767681297534375946515,
    80386287592878490201521685554828717201219257766954,
    78182833757993103614740356856449095527097864797581,
    16726320100436897842553539920931837441497806860984,
    48403098129077791799088218795327364475675590848030,
    87086987551392711854517078544161852424320693150332,
    59959406895756536782107074926966537676326235447210,
    69793950679652694742597709739166693763042633987085,
    41052684708299085211399427365734116182760315001271,
    65378607361501080857009149939512557028198746004375,
    35829035317434717326932123578154982629742552737307,
    94953759765105305946966067683156574377167401875275,
    88902802571733229619176668713819931811048770190271,
    25267680276078003013678680992525463401061632866526,
    36270218540497705585629946580636237993140746255962,
    24074486908231174977792365466257246923322810917141,
    91430288197103288597806669760892938638285025333403,
    34413065578016127815921815005561868836468420090470,
    23053081172816430487623791969842487255036638784583,
    11487696932154902810424020138335124462181441773470,
    63783299490636259666498587618221225225512486764533,
    67720186971698544312419572409913959008952310058822,
    95548255300263520781532296796249481641953868218774,
    76085327132285723110424803456124867697064507995236,
    37774242535411291684276865538926205024910326572967,
    23701913275725675285653248258265463092207058596522,
    29798860272258331913126375147341994889534765745501,
    18495701454879288984856827726077713721403798879715,
    38298203783031473527721580348144513491373226651381,
    34829543829199918180278916522431027392251122869539,
    40957953066405232632538044100059654939159879593635,
    29746152185502371307642255121183693803580388584903,
    41698116222072977186158236678424689157993532961922,
    62467957194401269043877107275048102390895523597457,
    23189706772547915061505504953922979530901129967519,
    86188088225875314529584099251203829009407770775672,
    11306739708304724483816533873502340845647058077308,
    82959174767140363198008187129011875491310547126581,
    97623331044818386269515456334926366572897563400500,
    42846280183517070527831839425882145521227251250327,
    55121603546981200581762165212827652751691296897789,
    32238195734329339946437501907836945765883352399886,
    75506164965184775180738168837861091527357929701337,
    62177842752192623401942399639168044983993173312731,
    32924185707147349566916674687634660915035914677504,
    99518671430235219628894890102423325116913619626622,
    73267460800591547471830798392868535206946944540724,
    76841822524674417161514036427982273348055556214818,
    97142617910342598647204516893989422179826088076852,
    87783646182799346313767754307809363333018982642090,
    10848802521674670883215120185883543223812876952786,
    71329612474782464538636993009049310363619763878039,
    62184073572399794223406235393808339651327408011116,
    66627891981488087797941876876144230030984490851411,
    60661826293682836764744779239180335110989069790714,
    85786944089552990653640447425576083659976645795096,
    66024396409905389607120198219976047599490197230297,
    64913982680032973156037120041377903785566085089252,
    16730939319872750275468906903707539413042652315011,
    94809377245048795150954100921645863754710598436791,
    78639167021187492431995700641917969777599028300699,
    15368713711936614952811305876380278410754449733078,
    40789923115535562561142322423255033685442488917353,
    44889911501440648020369068063960672322193204149535,
    41503128880339536053299340368006977710650566631954,
    81234880673210146739058568557934581403627822703280,
    82616570773948327592232845941706525094512325230608,
    22918802058777319719839450180888072429661980811197,
    77158542502016545090413245809786882778948721859617,
    72107838435069186155435662884062257473692284509516,
    20849603980134001723930671666823555245252804609722,
    53503534226472524250874054075591789781264330331690,
]


def large_sum():
    return str(sum(large_numbers))[:10]


if __name__ == "__main__":
    print(f"1st 10 digits of sum of 100 50-digit numbers is {large_sum()}")


class MakeLarger(object):
    def __init__(self, number):
        self.number = number

    # shorter time to complete
    def make_larger_v0(self):
        l = []
        for x in str(self.number):
            l.append(x)
        s = sorted(l, reverse=True)
        return int("".join(s))

    def make_larger_v1(self):
        str_number = str(self.number)
        sorted_lst = sorted([x for x in str_number], reverse=True)
        return int("".join(sorted_lst))

    # takes a longer time to complete the problem
    def make_larger_v2(self):
        return int("".join(sorted([x for x in str(self.number)], reverse=True)))


def map_squares(numbers):
    """
    :param numbers: list of numbers
    :return: square of the numbers
    """
    return list(map(lambda x: x**2, numbers))


x = int(input("Enter the value of row: "))
y = int(input("Enter the value of column: "))

a = [[0 for row in range(0, x)] for col in range(0, y)]
b = [[0 for row in range(0, x)] for col in range(0, y)]
result = [[0 for row in range(0, x)] for col in range(0, y)]

print("Enter elements of first matrix: ")
for i in range(x):
    for j in range(y):
        a[i][j] = int(input())

print("Enter the elements of second matrix: ")
for i in range(x):
    for j in range(y):
        b[i][j] = int(input())

print("Elements of First matrix is: ")
for row in a:
    print(row)

print("Elements of second matrix")
for row in b:
    print(row)

# iterate through rows
for i in range(len(a)):
    # iterate through columns
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]

# print the sum of 2 matrices
print("Sum of the two matrices is: ")
for r in result:
    print(r)


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = [[int(n) for n in row.split()] for row in matrix.split("\n")]
        self.columns = [list(tup) for tup in zip(*self.rows)]

    def alternative(self):
        rows = [map(int, item.split()) for item in self.matrix.split("\n")]
        columns = [map(list, zip(*rows))]

    def alternative_2(self):
        rows = [[int(x) for x in line.split()] for line in self.matrix.split("\n")]
        columns = [[rows[r][c] for r in range(len(rows))] for c in range(len(rows[0]))]


from bisect import insort


def find_median(arr):
    """
    Finds the median of an array.
    """
    len_of_list = len(arr)

    if len_of_list % 2 == 0:
        l = arr[len_of_list // 2]
        r = arr[(len_of_list // 2) - 1]
        return (l + r) / 2.0
    elif len_of_list % 2 != 0:
        return float(arr[len_of_list // 2])


n = int(input().strip())
heap = []
for _ in range(n):
    x = int(input().strip())
    insort(heap, x)
    print(find_median(heap))


def year_days(year):
    days = 365
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days += 1
    return "%d has %d days" % (year, days)


def multiply(n):
    return 5 ** len(str(n)) * n if n > 1 else (5 ** (len(str(n)) - 1)) * n


def narcissistic(value):
    l = len(str(value))  # length of number
    return sum([pow(int(i), l) for i in str(value)]) == value


from pymath.abundant_numbers import is_abundant


def find_sum_cant_be_written(lower_limit, upper_limit):
    """
    Finds the sum of all positive integers within the given range, which can not be written as the sum of 2 abundant
    numbers,
    :param lower_limit: Lower limit bound
    :type lower_limit int
    :param upper_limit: upper limit bound
    :type upper_limit int
    :return: sum of all positive integers within range, which can't be written as sum of 2 abundant numbers
    :rtype: int
    """
    # sanity checks

    if lower_limit is None or upper_limit is None:
        raise ValueError("Expected non-None types for bounds lower and upper limit")

    if not isinstance(lower_limit, (int, float)) or not isinstance(
        upper_limit, (int, float)
    ):
        raise TypeError("Expected number type for upper and lower limits")

    if lower_limit < 0:
        raise ValueError(
            f"Expected lower limit to be positive, instead got {lower_limit}"
        )

    if upper_limit > 28123:
        raise ValueError(
            f"Expected upper limit to be less than 28123, instead got {upper_limit}"
        )

    # convert the upper and lower limits to integers, this is for float type inputs
    lower_limit, upper_limit = int(lower_limit), int(upper_limit)

    # find all abundant numbers within the given range
    abundant_numbers = set(x for x in range(lower_limit, upper_limit) if is_abundant(x))

    # list that stores all numbers that can't be written as the sum of 2 abundant numbers
    cant_be_written = []

    for x in range(lower_limit, upper_limit + 1):
        if not any((x - number) in abundant_numbers for number in abundant_numbers):
            cant_be_written.append(x)

    # return the sum of numbers
    return sum(cant_be_written)


def nth_even(n):
    return 2 * (n - 1)


def climb(n):
    return [1] if n == 1 else climb(int(n / 2)) + [n]


print(list(climb(13)))
from algorithms.say_number import say


def number_letter_counts(start, end):
    """
    counts all the letters used in the range of start to end, when each number is converted to words
    1 would become one, 2 would become two, etc,
    A range of 1 to 5 is one, two, three, four, five, number of letters used in total are 3 + 3 + 5 + 4 + 4 = 19

    An example:
    >>> number_letter_counts(1, 5)
    19

    :param start: Where to start the range
    :param end: Limit/end of the range
    :return: Returns the number of letters used in the range
    :rtype: int
    """
    # sanity checks

    # short circuit early if the start and end are the same
    if start == end or end == 0:
        return len(say(start))

    # if invalid values used, ie. None
    if end is None or start is None:
        raise ValueError(f"Start or end can not be None")

    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise ValueError(f"Expected number input")

    # enforce converting the input to integer
    start = int(start)
    end = int(end)

    # get the range
    num_range = range(start, end + 1)

    # map each number in range to say, converting it to words
    numbers_in_words = map(say, num_range)

    # iterate through each number, counting the number of letters used
    letters = 0

    # for each number in the range of words used
    for number in numbers_in_words:
        # count the number of letters used, excluding hyphens and spaces
        # find the letters used for this number
        letters_used = len(number) - (number.count(" ") + number.count("-"))

        letters += letters_used

    return letters


def diagonal_sum(n):
    """
    Finds the diagonal sum of a spiral of n by n

    An example:
    >>> diagonal_sum(5)
    101

    :param n: Number of rows and columns of the grid
    :type n int
    :return: Total of the numbers along the diagonal
    :rtype: int
    """
    count = 1
    last = 1
    total = last

    while count < 2 * n - 1:
        i = int(count * 0.5 + 1.5)
        for _ in range(4):
            last += i
            total += last
            count += 1
    return total


if __name__ == "__main__":
    number = 1001
    diag = diagonal_sum(number)
    print(f"Diagonal sum of {number} by {number} spiral is {diag}")


def pandigital_products(limit=10000):
    """
    Find all pandigital products for the given upper limit
    :param limit: upper limit, defaults to 10000
    :type limit int
    :return: sum of all pandigital products
    :rtype: int
    """
    products = set()
    pandigital = "123456789"

    for x in range(limit):
        for y in range(limit):
            product = x * y
            num_str = "".join(sorted(str(x) + str(y) + str(product)))
            if num_str == pandigital:
                products.add(product)

    return sum(products)


if __name__ == "__main__":
    upper_limit = 10000
    pan_products = pandigital_products(upper_limit)
    print(
        f"Sum of pandigital products for upper limit of {upper_limit} is {pan_products}"
    )
from math import factorial as fac


def binomial(x, y):
    try:
        return fac(x) // fac(y) // fac(x - y)
    except ValueError:
        return 0


def pascals_triangle(nth: int) -> list:
    """
    Generate Pascal's triangle of binomial coefficients upto the nth row
    :param nth: Nth row to generate Pascal's triangle
    :return: returns list of lists of each row or binomial coefficients of Pascal's triangle
    """
    result = []
    for x in range(nth + 1):
        result.append([binomial(x, y) for y in range(x + 1)])

    return result


def pascal_nth_row(nth: int) -> list:
    """
    Get's Pascal's Triangle Nth row and returns it
    This is much faster than calculating the whole triangle and then fetching by it's index.
    Instead we use the formula
    NCr = (NCr - 1 * (N - r + 1)) / r where 1 ≤ r ≤ N
    as the nth row consists of the following sequence:
    NC0, NC1, ......, NCN - 1, NCN
    """
    ncr_1 = 1
    row = [ncr_1]

    for i in range(1, nth + 1):
        ncr = (ncr_1 * (nth - i + 1)) // i
        row.append(ncr)
        ncr_1 = ncr

    return row


def is_perfect(number):
    if number <= 1:
        return False
    return sum(divisor_generator(number)) + 1 == number


def divisor_generator(n):
    """Returns an unordered list of divisors for n (1 < n)."""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            if i * i != n:
                yield n // i


from math import sqrt


# function to check if a number is a perfect square
def is_square(n):
    if n < 0:
        return False
    else:
        return sqrt(n).is_integer()


from itertools import count, islice
from math import sqrt


class Pernicious(object):
    """
    get the range of the number from 3 to the number, converting each to binary
    for
    """

    def __init__(self, number):
        self.number = number

    # long method
    def is_pernicious(self):
        primes = []
        if self.number <= 2:
            return "No pernicious numbers"
        for x in range(3, int(self.number) + 1):
            if Pernicious.is_prime(sum([int(i) for i in "{0:b}".format(x)])):
                primes.append(x)
        return primes

    # using ternary and lambda
    def is_pernicious_v2(self):
        m = lambda i: "{0:b}".format(i)
        if self.number <= 1:
            return "No pernicious numbers"
        return [
            x
            for x in range(3, int(self.number) + 1)
            if Pernicious.is_prime(sum([int(y) for y in m(x)]))
        ]

    def is_pernicious_v3(self):
        return [
            x
            for x in range(int(self.number) + 1)
            if bin(x).count("1") in [2, 3, 5, 7, 11, 13]
        ] or "No pernicious numbers"

    @staticmethod
    def is_prime(num):
        return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))


def nb_year(p0, percent, aug, p):
    n = 0
    while p0 < p:
        p0 += p0 * (percent / 100) + aug
        n += 1
    return n


from functools import reduce


def power_digit_sum(base, exponent):
    """
    Finds the sum of digits of the exponentiation of base to exponent
    Example:

    >>> power_digit_sum(2, 15)
    26

    :param base: Base
    :param exponent: Exponent
    :return: sum of digits of the exponent
    :rtype: int
    """
    result = pow(base, exponent)
    return reduce(lambda x, y: x + y, map(int, [i for i in str(result)]))


def pofi(n):
    return ["1", "i", "-1", "-i"][n % 4]


import cProfile
from functools import reduce


def power_sum_dig_term(n):
    return power_of_sum()[n - 1]


def power_of_sum():
    lst_n = []
    for base in range(2, 100):
        num = base
        for _ in range(2, 30):
            num *= base
            if sum(map(int, str(num))) == base:
                lst_n.append(num)
    return sorted(lst_n)


# Alternatively
series = [0]
for a in range(2, 99):
    for b in range(2, 42):
        c = a**b
        if a == sum(map(int, str(c))):
            series.append(c)
power_sumDigTerm = sorted(series).__getitem__

# alternative 2
sum_dig = lambda n: reduce(lambda x, y: x + int(y), str(n), 0)

memo = []

for i in range(2, 100):
    for j in range(1, 100):
        p = i**j
        if p > 10 and sum_dig(p) == i:
            memo += [p]

memo.sort()


def power_sumDigTerm_2(n):
    return memo[n - 1]


def main():
    cProfile.run("power_of_sum()")


if __name__ == "__main__":
    main()
import re
from itertools import count, islice
from math import sqrt


def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))


def is_prime_v2(x):
    if x < 2:
        return False
    for n in range(2, (x - 1)):
        if x % n == 0:
            return False
    else:
        return True


def is_prime_with_re(num):
    """
    Determines a prime number with regular expression
    :param num: The number to evaluate for primarity
    :return: True /False
    :rtype: bool
    """
    return re.match(r"^1?$|^(11+?)\1+$", "1" * num) is None


def divisors(n):
    return (
        len([1, n]) if is_prime(n) else len([x for x in range(1, n + 1) if n % x == 0])
    )


from ..is_prime import is_prime


def step(g, m, n):
    if (n - m) < g:
        return None

    if (n - m) == g and (is_prime(m) and is_prime(n)):
        return [m, n]

    for x in range(m, n + 1):
        second = x + g

        if is_prime(x) and is_prime(second):
            return [x, second]

    return None


from itertools import count
from typing import List

from ..is_prime import is_prime


def primes_up_to(n: int) -> List[int]:
    """
    Returns a list of prime numbers from 2, up to n
    """
    known = []
    candidates = primes()

    while len(known) < n:
        x = next(candidates)
        if is_prime(x):
            known.append(x)
    return known


def nth_prime(n):
    """
    Returns the nth prime number
    """
    known = primes_up_to(n)
    return known[n - 1]


def primes():
    yield 2
    yield 3
    for x in count(6, 6):
        yield x - 1
        yield x + 1


from ..is_prime import is_prime


def sieve(limit, start=2):
    """
    Finds all the prime numbers from start (defaults to 2) up to the given limit
    :param limit: Limit to get primes up to
    :param start: Start of the range
    :return: List of all primes from start up to limit
    """
    to_sieve = range(start, limit + 1)
    return list(filter(is_prime, to_sieve))


"""
Finds the prime factors of a given number and returns a list of the numbers
"""


def prime_factors(number):
    """
    Finds the prime factors of a number
    :param number: Integer number to find prime factors for
    :return: list of primes factors for the given number
    :rtype: list

    An example
    >>> prime_factors(13195)
    [5, 7, 13, 29]
    """
    c, res = 2, []
    while c * c <= number:
        while (number % c) == 0:
            # repeats multiple factors
            res.append(c)
            number /= c
        c += 1
    if number > 1:
        res.append(number)
    return res


from typing import List


def find_k_primes(k: int, start: int, end: int) -> List[int]:
    pass


from functools import reduce

from pymath.primes.nth_prime import primes_up_to


def multiplier(x, y):
    return x * y


def num_primorial(n):
    known = primes_up_to(n)

    return reduce(multiplier, known)


import cProfile
from functools import reduce
from itertools import islice, count, product
from math import sqrt, pow
from operator import mul


def is_prime(num):
    return num > 1 and all(num % i for i in islice(count(2), int(sqrt(num) - 1)))


PRIMES = [num for num in range(2, 1001) if is_prime(num)]


def factors_powers(num):
    global PRIMES
    if num == 1:
        return (1,), (0,)
    factors, powers, idx = [], [], 0
    while num > 1:
        prime = PRIMES[idx]
        idx += 1
        if num % prime != 0:
            continue
        factors.append(prime)
        p = 0
        while num % prime == 0:
            p += 1
            num /= prime
        powers.append(p)
    return factors, powers


def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError("Argument must be divisible by 4")
    prime_factors, powers = factors_powers(b / 2)
    args = [(1, pow(prime_factors[x], powers[x])) for x in range(len(powers))]
    a = sorted([reduce(mul, p) for p in product(*args)])
    factors = [(m, n) for m, n in zip(reversed(a), a) if m > n]
    ts = set()
    for m, n in factors:
        l = sorted([b, m * m - n * n, m * m + n * n])
        ts.update([tuple(l)])
    return ts


def is_pythagorean_triplet(abc):
    """
    Checks if a tuple triplet is a pythagorean triplet, i.e. adheres to the rule of a**2 + b**2 = c**2

    An example:

    >>> abc = (29, 20, 21)
    >>> is_pythagorean_triplet(abc)
    True

    >>> abc = (25, 25, 1225)
    >>> is_pythagorean_triplet(abc)
    False

    :param abc: Tuple with the three numbers to check
    :return: True if the tuple meet the given condition
    :rtype: bool
    """
    t = sorted(abc)
    a, b, c = t
    return c * c == a * a + b * b


def triplets_in_range(mini, maxi):
    """
    Finds all the triplets in a given range that meet the condition a ** 2 + b ** 2 = c ** 2

    >>> triplets_in_range(2, 10)
    {(3, 4, 5), (6, 8, 10)}

    :param mini: The minimum in the range
    :param maxi: Maximum in the rnage
    :return: a set of tuples (with length 3) of numbers that meet the given condition
    :rtype: set
    """
    res = set()
    for a in range(mini, maxi + 1):
        for b in range(a + 1, maxi + 1):
            c = int(sqrt(a * a + b * b) + 0.5)
            if c * c == a * a + b * b and mini <= c <= maxi:
                res.update(
                    [
                        (
                            a,
                            b,
                            c,
                        )
                    ]
                )
    return res


if __name__ == "__main__":
    cProfile.run("is_prime(1000)")
import math


class QFormula(object):
    """
    calculates the square root of the value from the formula [(2 * C * D)/H]
    """

    def __init__(self, number_list):
        self.number_list = number_list
        self.constant_c = 50
        self.constant_h = 30

    # using list compression
    def q_formula_compress(self):
        return ",".join(
            [
                str(math.sqrt((float(x) * self.constant_c * 2) / self.constant_h))
                for x in self.number_list
            ]
        )

    # using simple for loop
    def q_formula_simple(self):
        values = []
        for y in self.number_list:
            n = math.sqrt((float(y) * self.constant_c * 2) / self.constant_h)
            values.append(n)
        return ",".join(values)


"""
Given the formula n^2 + an + b, where |a| < 1000 and |b| ≤ 1000
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n=0.
"""
from pymath.primes.is_prime import is_prime


def find_coef_a_b_with_max_primes(n=0):
    """
    Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of
    primes for consecutive values of n, starting with n=0.
    :param n: Starting point, defaults to 0
    :type n int
    :return: product of a and b
    :rtype: int
    """
    num = n
    max_primes = 0
    product = 0

    for a in range(-999, 1001):
        for b in range(-999, 1001):
            while True:
                s = num**2 + a * num + b
                if not is_prime(s):
                    break

                if num > max_primes:
                    max_primes = num
                    product = a * b
                num += 1
    return product


if __name__ == "__main__":
    start = 0
    product_a_b = find_coef_a_b_with_max_primes(start)
    print(
        f"Product of coefficient a and b with maximum primes with starting point n of {start} is {product_a_b}"
    )
from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        gcd, b = sorted([numer, denom])

        while b != 0:
            gcd, b = b, gcd % b

        if denom < 0 < gcd:
            gcd = -gcd

        self.numer = numer // gcd
        self.denom = denom // gcd

    def __eq__(self, other):
        return self.numer == other.numer and other.denom == self.denom

    def __repr__(self):
        return f"{self.numer}/{self.denom}"

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        return self + Rational(-1, 1) * other

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return self * (other**-1)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        if power < 0:
            self.numer, self.denom = self.denom, self.numer
            power = -power
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)


"""
Finds the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from pymath.primes.sieve_of_erastothenese import sieve


def longest_recurring_cycle(limit=1000):
    """
    Finds the longest recurring cycle for a fraction
    An example:
    >>> longest_recurring_cycle(10)
    7

    >>> longest_recurring_cycle(7)
    3

    :param limit: The limit of the denominator, if None is provided, the limit will default to 1000
    :type limit int
    :return: Returns the value of d for which the longest recurring cycle exists in the decimal fraction part
    :rtype: int
    """
    # sanity checks, because we don't want unexpected crashes
    if not isinstance(limit, int) or limit <= 1:
        raise ValueError("Expected limit to be greater than 1 and an integer")

    # we return 3 because that is the smallest d that repeats with the longest recurring cycle. 1/2 (0.5), 1/4 (0.25),
    # 1/5 (0.2) don’t repeat. 1/3 (0.33~), 1/6 (0.166~) both repeat with a cycle of 1 of which 3
    # is the smallest value of d. 3 is not a reptend prime.
    if limit < 8:
        return 3

    prime_sieve = sieve(limit)

    for denominator in prime_sieve[::-1]:
        period = 1
        while pow(10, period) % denominator != 1:
            period += 1
        if denominator - 1 == period:
            return denominator


if __name__ == "__main__":
    limit_ = 1000
    digit_with_recurring_cycle = longest_recurring_cycle(limit_)
    print(
        f"Digit with longest recurring cycle in its decimal fraction part within range of 2 to {limit_} "
        f"is {digit_with_recurring_cycle}"
    )
from fractions import Fraction


def reduce(fraction):
    num, den = fraction[0], fraction[1]
    if num == den:
        return [1, 1]
    if num > den:
        num, den = fraction[1], fraction[0]
        return [
            Fraction(num % den, den)._denominator,
            Fraction(num % den, den)._numerator,
        ]
    else:
        return [
            Fraction(num % den, den)._numerator,
            Fraction(num % den, den)._denominator,
        ]


ROMAN_MAP = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def numeral(arabic):
    roman_number = ""
    for number, roman in ROMAN_MAP:
        while arabic >= number:
            roman_number += roman
            arabic -= number
    return roman_number


class Numerals(object):
    @staticmethod
    def int_to_roman(number):
        if type(number) != type(1):
            raise TypeError("expected integer, got %s" % type(number))
        if not 0 < number < 4000:
            raise ValueError("Argument must be between 1 and 3999")
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        result = ""
        for i in range(len(ints)):
            count = int(number / ints[i])
            result += nums[i] * count
            number -= ints[i] * count
        return result


class RomanNumeral(object):
    """
    Create a dictionary that contains the Roman numerals conversions and their Arabic numbers
    the Keys will be ones, tens and hundreds and thousands
    :translate_roman_numeral checks if the roman numeral is in dictionary, retuns the value
    if not, loops through the dictionary, checking each string

    :translate_roman_numeral_2, uses a ROMAN_LIST to loop through each value and number and checks
    """

    ROMANS = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XX": 20,
        "XXX": 30,
        "XL": 40,
        "L": 50,
        "LX": 60,
        "LXX": 70,
        "LXXX": 80,
        "XC": 90,
        "C": 100,
        "CC": 200,
        "CCC": 300,
        "CD": 400,
        "D": 500,
        "DC": 600,
        "DCC": 700,
        "DCCC": 800,
        "CM": 900,
        "M": 1000,
        "MM": 2000,
        "MMM": 3000,
    }

    ROMAN_LIST = [
        ["M", 1000],
        ["D", 500],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["X", 10],
        ["V", 5],
        ["IV", 4],
        ["I", 1],
    ]

    def __init__(self, number):
        self.number = number

    # todo: test fails for roman numerals with unit digit being less than 5
    def translate_roman_numeral(self):
        arabic_no = 0
        if self.number in self.ROMANS:
            return self.ROMANS.get(self.number)
        else:
            for x in self.number:
                arabic_no += self.ROMANS.get(x)
        return arabic_no

    # variation two of the translate roman numeral
    def translate_roman_numeral_v2(self):
        num_str = self.number.upper()
        arabic_no = 0
        if isinstance(int(num_str), int):
            raise TypeError("Please input a string")
        else:
            for letter, value in self.ROMAN_LIST:
                if num_str.startswith(letter):
                    num_str = num_str[1:]
                    arabic_no += value
        return arabic_no

    def translate_roman_numeral_v3(self):
        if type(self.number) != type(""):
            raise TypeError("expected string, got %s" % type(self.number))
        else:
            num = self.number
            nums = ["M", "D", "C", "L", "X", "V", "I"]
            ints = [1000, 500, 100, 50, 10, 5, 1]
            places = []
            for c in num:
                if not c in nums:
                    raise ValueError(
                        "input is not a valid roman numeral: %s" % self.number
                    )
            for i in range(len(num)):
                c = num[i]
                value = ints[nums.index(c)]
                # If the next place holds a larger number, this value is negative.
                try:
                    nextvalue = ints[nums.index(num[i + 1])]
                    if nextvalue > value:
                        value *= -1
                except IndexError:
                    # there is no next place.
                    pass
                places.append(value)
            sum = 0

            # Easiest test for validity...
            for n in places:
                sum += n
            if Numerals.int_to_roman(sum) == input:
                return sum
            else:
                raise ValueError("input is not a valid roman numeral: %s" % self.number)


def saddle_points(matrix):
    if not matrix:
        return set()
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Irregular matrices are not allowed")
    # gets the maximum val per row
    mmax = [max(row) for row in matrix]
    # gets the min value per col
    mmin = [min(col) for col in zip(*matrix)]
    points = [
        (i, j)
        for i in range(len(matrix))
        for j in range(len(matrix[0]))
        if mmax[i] == mmin[j]
    ]

    return set(points)


from typing import List


def self_dividing_numbers(left: int, right: int) -> List[int]:
    """
    Alternate implementation of self_dividing:
    def self_dividing(n):
        x = n
        while x > 0:
            x, d = divmod(x, 10)
            if d == 0 or n % d > 0:
                return False
        return True
    """

    def self_dividing(number: int):
        for digit in str(number):
            if digit == "0" or number % int(digit) > 0:
                return False
        return True

    result = []

    for num in range(left, right + 1):
        if self_dividing(num):
            result.append(num)

    return result  # or filter(self_dividing, range(left, right + 1)


"""
Finds the smallest multiple in a range of numbers
"""
from functools import reduce

try:
    from math import gcd
except ImportError:
    from fractions import gcd


def smallest_multiple(limit):
    """
    Find the smallest positive number that is evenly divisible by all numbers from 1 to the given
    limit
    :return: smallest positive number
    :rtype: int
    """
    numbers = range(1, limit)
    return reduce(lambda a, b: int(a * b / gcd(a, b)), numbers)


if __name__ == "__main__":
    limit = 21
    result = smallest_multiple(limit)
    print(f"Smallest positive number in range of 1 to {limit} is {result}")


# todo: work on this to fix splitting even numbers
def split_all_even_numbers(numbers, way):
    """
    Splits even numbers found in the array into odd numbers based on the way provided:
    the ways provided, if the even number provided is 8
        0 -> Split into two odd numbers, that are closest to each other.
        (e.g.: 8 -> 3,5)
        1 -> Split into two odd numbers, that are most far from each other.
        (e.g.: 8 -> 1,7)
        2 -> All new odd numbers from the splitting should be equal and the maximum possible number.
        (e.g.: 8 -> 1, 1, 1, 1, 1, 1, 1, 1)
        3 -> Split into 1s.
        (e.g.: 8 -> 1, 1, 1, 1, 1, 1, 1, 1)
    :param numbers: the array of numbers
    :param way: way to split the even numbers found
    :return: a new list with only odd numbers
    :rtype:list
    """
    # create a copy of the numbers array
    result = numbers[:]

    # if the way is 0, split the even number into the odd numbers that are closet to each other
    # loop through the numbers array and check for even numbers
    # use a range from 1 up to the even number (excluding it) and check only for odd numbers
    if way == 0:
        for num in result:
            # if the number is even
            if num % 2 == 0:
                print("Even num: ", num)

                # get the position of the even number
                even_pos = result.index(num)
                print("Index position of even number", even_pos)

                # create a range for only odd numbers in the range upto the number
                rnge, indx = list(range(1, num, 2)), 0
                print("Odd numbers in the range: ", rnge)
                for _ in rnge:
                    print("Sum of two odds: ", sum(rnge[indx : indx + 2]))
                    # if the sum of the 2 closest odd numbers sums to the odd number
                    if rnge[indx] + rnge[indx + 2] == num:
                        # replace the num with the 2 odd numbers
                        result[even_pos : even_pos + 1] = rnge[indx : indx + 2]
                        break
                    indx += 1
    elif way == 1:
        pass
    elif way == 2:
        pass
    elif way == 3:
        pass

    return result


# [1, 5, 5, 1, 3]
print(split_all_even_numbers([1, 10, 1, 3], 0))
"""
This finds the sum of all primes below a target limit
"""
import cProfile

from pymath.primes.sieve_of_erastothenese import sieve


def find_sum_of_primes(limit):
    """
    Finds the sum of all primes below a target limit. It is always assumed that the starting point in the range will
    be 2, as there is no prime number below 2

    An example:
    >>> find_sum_of_primes(10)
    17

    :param limit: Target limit
    :return: Sum of all primes below the given limit
    :rtype: int
    """

    # find all the primes below the target limit
    all_primes = sieve(limit)

    return sum(all_primes)


if __name__ == "__main__":
    limit_ = 2_000_000
    print(
        f"Sum of all prime numbers in the given range of 2 to {limit_} is {find_sum_of_primes(limit_)}"
    )

    cProfile.run("find_sum_of_primes(2_000_000)")
from random import choice


def sum_between(array):
    """
    The function takes in a list of 2 numbers, Sums the numbers in between the list including the numbers and returns
    result. The numbers in the array may not be in the same order, so a check will be performed to test which number
    is lower and create a range to the greater number
    If the array input has 3 or more numbers an error will be raised and program will exit
    if the array has length or 0 or 1, raise an error
    :param array: Array to sum all numbers in between the 2 numbers in array
    :return: sum of all numbers from the array 'range'
    :rtype: int
    :raises: TypeError: if the array input is invalid
    """

    # test if the input is a list
    if array is None or not isinstance(array, list):
        raise TypeError("Expected input to be a list instead got {}".format(array))
    # test if the array is of a valid length
    elif len(array) < 2 or len(array) > 2:
        raise TypeError(
            "Expect array to be of length 2 instead got array of length: {}".format(
                str(len(array))
            )
        )

    # If the first number is less than second sum up to the 2nd
    if array[0] < array[1]:
        return sum(range(array[0], array[1] + 1))
    # if the second number is less than 1st
    elif array[1] < array[0]:
        return sum(range(array[1], array[0] + 1))
    # if both numbers are the same
    elif array[1] == array[0]:
        return choice(array)


def summation(x):
    return sum(range(1, x + 1)) if isinstance(x, int) else "Error 404"


def sum_of_multiples(limit, multiples):
    if multiples[0] == 0:
        multiples = multiples[1:]
    return sum(
        value
        for value in range(limit)
        if any(value % multiple == 0 for multiple in multiples)
    )


def sum_same(num, times):
    c, total = 1, 0
    while c <= times:
        n = str(num) * c
        total += int(n)
        c += 1
    return total


n = int(input("Enter a number: "))


def sum_me(n):
    total = 0.0
    for i in range(1, n + 1):
        total += float(float(i) / (i + 1))
    return total


print(sum_me(n))


def super_size(n):
    out = [i for i in str(n)]
    m = int("".join(list(sorted(out))[::-1]))
    return m


print(super_size(2150))
from math import sqrt, pi, acos, floor


def tankvol(h, d, vt):
    radius = d / 2
    cylinder_height = vt / (pi * (radius**2))
    triangle_height = radius - h
    theta = acos(triangle_height / radius)

    # or base = radius * sin(theta)
    base = sqrt((radius**2) - (triangle_height**2))

    triangle_area = (base * triangle_height) / 2
    sector_area = (radius * radius * theta) / 2

    remainder_area = (sector_area - triangle_area) * 2
    return floor(cylinder_height * remainder_area)


from collections import Counter
from typing import List

from datastructures.trees.heaps.min_heap import MinHeap


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)

    return [x for x, y in counter.most_common(k)]


def top_k_frequent_with_min_heap(nums: List[int], k: int) -> List[int]:
    """
    Uses a Min Heap to get the top k frequent elements
    """
    counter = Counter(nums)
    arr = []

    for num, count in counter.items():
        arr.append([-count, num])

    min_heap = MinHeap(arr)
    ans = []

    for _ in range(k):
        a = min_heap.remove_min()
        ans.append(a[1])

    return ans


from collections import Counter
from math import sqrt, pow


class Triangle(object):
    """
    A triangle class that returns the kinds of triangles
    :cvar TYPES: The types of triangles to evaluate. it is a dictionary, therefore the key is the first letter
    of the type of triangle
        e stands for equilateral
        i stands for isosceles triangle
        s stands for scalene triangle
    """

    # the types of triangles
    TYPES = {"e": "equilateral", "s": "scalene", "i": "isosceles"}

    def __init__(self, s1, s2, s3):
        """
        initializes a Triangle object with the lengths of the triangle as parameters
        :param s1: side 1
        :param s2: side 2
        :param s3: side 3
        :raises: TriangleError
        """
        self.sides = (s1, s2, s3)

        # if the triangle sides are violated, raise an error early
        if self._invalid_lengths() or self._violates_inequality():
            raise TriangleError

    def _invalid_lengths(self):
        """
        Checks if any of the sides of the triangle have invalid lengths, an invalid length could be
        a side that is less than 0
        :return: True/False
        :rtype: bool
        """
        return any(side <= 0 for side in self.sides)

    def _violates_inequality(self):
        """
        Checks If any 2 sides sum of the triangle violate the triangle inequality.
        The inequality x + y >= z
        where x,y, and z are the lengths of the sides of a triangle. In other words, the
        sum of the lengths of any two sides of a triangle always exceeds or is equal to
        the length of the third side.

        # alternatively
        triangle=lambda a,b,c:all([a+b>c,a+c>b,b+c>a])
        triangle=lambda a,b,c:(a+b>c)&(a+c>b)&(b+c>a)
        triangle=lambda *x:sum(x)-max(x)>max(x)
        :return: True/False in regards to any violation
        :rtype: bool
        """
        x, y, z = self.sides
        return any([x + y <= z, x + z <= y, y + z <= x])

    def kind(self):
        """
        The kind of triangle this object is
        :return: The kind of triangle this is
        :rtype: str
        """

        # get the distinct sides of the triangle
        distinct = len(set(self.sides))

        # equilateral if all three sides are equal
        if distinct == 1:
            return self.TYPES["e"]
        # if 2 sides are equal
        elif distinct == 2:
            return self.TYPES["i"]
        # no sides are equal
        else:
            return self.TYPES["s"]

    def area(self):
        """
        Gets the area of the triangle from the given sides
        Area of a triangle is calculated as a = 1/2 * b *h

        Equilateral triangle area is calculated as:
            1/2 * b * h, where the base, b, is any of the sides
            height, h, is the height which is calculated as h = (sqrt(3) * s) / 2
            This equates to (sqrt(3) * s^2) / 4

        Isosceles triangle area is calculated as:
        1/2 a^2 * sqrt( (b^2) / (a^2) - 1/4), where the b is a side with an equal length in another side,
        while a is the base of the triangle, or the side that does not have an equal length.

        First start by finding the 2 sides that are similar in length, will be stored as b
        The remaining side will be a(which will be used as the base), which we can then use to calculate the height
        h = sqrt(b ^ 2 - (1/4 * (a^2)))

        Scalene Triangle area is calculated as:
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        Since all the sides are unequal

        :return: The area of the triangle as an integer
        :rtype: int
        """
        s1, s2, s3 = self.sides
        # if it is an equilateral triangle
        if self.kind() == self.TYPES["e"]:
            return (sqrt(3) * pow(s1, 2)) / 4

        # if the triangle is an isosceles triangle
        if self.kind() == self.TYPES["i"]:
            side_count = Counter(self.sides).most_common()
            highest_count = max(x[1] for x in side_count)
            lowest_count = min(x[1] for x in side_count)

            b, a = 0, 0

            for y in side_count:
                if y[1] == highest_count:
                    b = y[0]
                if y[1] == lowest_count:
                    a = y[0]

            return (0.5 * pow(a, 2)) * sqrt((pow(b, 2) / pow(a, 2)) - (1 / 4))

        # if the triangle is a scalene triangle
        if self.kind() == self.TYPES["s"]:
            s = sum(self.sides) / 2
            return sqrt(s * (s - s1) * (s - s2) * (s - s3))

    def perimeter(self):
        """
        Gets the perimeter of a triangle, perimeter is the sum of all 3 sides of a triangle
        :return: perimeter of a triangle as an int
        :rtype: int
        """
        return sum(self.sides)


class TriangleError(Exception):
    pass


def row_sum_odd_numbers(n):
    return n**3


from collections import Counter
from math import sqrt

from pymath.get_next_prime import get_next_prime


def is_triangle_number(number):
    """
    Checks if a number is a triangle number, Returns False fo any input that is not an integer

    An example
    >>> is_triangle_number(8)
    False

    Returns False for none integer inputs
    >>> is_triangle_number(None)
    False

    Returns True for 1
    >>> is_triangle_number(1)
    True

    :param number: Number
    :return: Boolean value, True if number is a triangle number, False otherwise
    :rtype: bool
    """
    if not isinstance(number, int):
        return False
    x = (sqrt(8 * number + 1) - 1) / 2
    if x - int(x) > 0:
        return False
    return True


def find_highly_divisible_triangle_number(no_of_divisors):
    """
    Finds the value of the first triangle number with over a certain number of divisors, in this case the no_of_divisors

    :param no_of_divisors: Number of divisors
    :return: Triangle number with over the given number of divisors
    :rtype: int
    """

    def prime_factorize(num):
        factors = []
        number = abs(num)
        while number > 1:
            factor = get_next_prime(number)
            factors.append(factor)
            number /= factor

        if num < -1:
            factors[0] = -factors[0]
        return factors

    highly_divisible_triangle_num = 1

    while True:
        triangle = (
            highly_divisible_triangle_num * (highly_divisible_triangle_num + 1) / 2
        )
        factors = prime_factorize(triangle)
        counts = Counter(factors)
        divisors = 1
        for k, v in counts.items():
            divisors *= v + 1
        if divisors >= no_of_divisors:
            highly_divisible_triangle_num = triangle
            break
        highly_divisible_triangle_num += 1

    return highly_divisible_triangle_num


if __name__ == "__main__":
    number_of_divisors = 500
    print(
        f"First triangular number to have over {number_of_divisors} divisors is "
        f"{find_highly_divisible_triangle_number(number_of_divisors)}"
    )
import math

ab = int(input())
bc = int(input())

# using SOHCAHTOA
angle = round(math.degrees(math.atan2(ab, bc)))
print(str(angle) + "°")


def compute_sum(n):
    return sum(int(c) for i in range(n + 1) for c in str(i))


def vampire_test(x, y):
    product = x * y
    if len(str(x) + str(y)) != len(str(product)):
        return False

    for i in str(x) + str(y):
        if i in str(product):
            return True
        else:
            return False


from __future__ import division

import math
from functools import reduce
from itertools import product
from operator import mul


def fac(n):
    """
    return the prime factors for n
    >>> fac(600)
    [5, 5, 3, 2, 2, 2]
    >>> fac(1000)
    [5, 5, 5, 2, 2, 2]
    >>>
    """
    step = lambda x: 1 + x * 4 - (x // 2) * 2
    maxq = int(math.floor(math.sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    res = []
    if q <= maxq:
        res.extend(fac(n // q))
        res.extend(fac(q))
    else:
        res = [n]
    return res


def fact(n):
    """\
    return the prime factors and their multiplicities for n
    >>> fact(600)
    [(2, 3), (3, 1), (5, 2)]
    >>> fact(1000)
    [(2, 3), (5, 3)]
    """
    res = fac(n)
    return [(c, res.count(c)) for c in set(res)]


def divisors(n):
    """Returns all the divisors of n"""
    factors = fact(n)  # [(primefactor, multiplicity), ...]
    primes, maxpowers = zip(*factors)
    powerranges = (range(m + 1) for m in maxpowers)
    powers = product(*powerranges)
    return (
        reduce(mul, (prime**power for prime, power in zip(primes, powergroup)), 1)
        for powergroup in powers
    )


def vampire(n):
    fangsets = set(
        frozenset([d, n // d])
        for d in divisors(n)
        if (
            len(str(d)) == len(str(n)) / 2.0
            and sorted(str(d) + str(n // d)) == sorted(str(n))
            and (str(d)[-1] == 0) + (str(n // d)[-1] == 0) <= 1
        )
    )
    return sorted(tuple(sorted(fangs)) for fangs in fangsets)


if __name__ == "__main__":
    print("First 25 vampire numbers")
    count = n = 0
    while count < 25:
        n += 1
        fangpairs = vampire(n)
        if fangpairs:
            count += 1
            print("%i: %r" % (n, fangpairs))
    print("\nSpecific checks for fangpairs")
    for n in (16758243290880, 24959017348650, 14593825548650):
        fangpairs = vampire(n)
        print("%i: %r" % (n, fangpairs))


class VisibleCubes:
    def __init__(self, n):
        self.n = n

    @classmethod
    def cubearea(cls, n):
        return cls(n)

    # method to calculate the area
    def calc_area(self):
        return str(pow(self.n, 3)) + " cm3"

    # check on the visible cubes
    @staticmethod
    def visible_cubes(n):
        return pow(n, 3) - VisibleCubes.not_visible_cubes(n)

    # check on how many cubes are not visible
    @staticmethod
    def not_visible_cubes(n):
        return 0 if n in range(0, 3) else (n - 2) ** 3


def wallpaper(l, w, h):
    wall_area = 2 * ((l * h) + (w * h))
    wall_paper_area = 0.52 * (10 * 1.15)
    papers = wall_area / wall_paper_area
    return papers


def productFib(prod):
    fib, res, indx = [0, 1], [], 0
    for _ in fib:
        if fib[indx] * fib[indx + 1] == prod:
            return [fib[indx], fib[indx + 1], True]
        if fib[indx] * fib[indx + 1] > prod:
            return [fib[indx], fib[indx + 1], False]
        fib.append(fib[indx] + fib[indx + 1])
        indx += 1


def productFib_v2(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]


"""
Finds the first fibonacci number with n digits
"""


def n_digit_fibonacci(n):
    """
    Finds the index of the first fibonacci number with n digits
    An example:

    >>> n_digit_fibonacci(3)
    12

    :param n: number of digits to find for a fibonacci number
    :type n int
    :return: index of first fibonacci number with n digits
    :rtype: int
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError(
            f"Expected n to be an integer and greater than 0, instead found {n}"
        )

    # starting fibonacci sequence
    fib_list = [1, 1]

    # c is the counter(pointer) that will be used to find the next fibonacci number,
    # no_of_digits is the number of digits of the current fibonacci number
    # term is the term of the next fibonacci number, i.e. the current index in the fibonacci sequence of the sum of the
    # previous 2 fibonacci number in the sequence
    c = 0
    no_of_digits = 1
    term = 2

    while no_of_digits < n:
        # get the next fibonacci number
        fn = fib_list[c] + fib_list[c + 1]

        # get the number of digits
        fn_digits = len(str(fn))

        # if the length of the fibonacci number is greater than current number of digits, re-assign
        if fn_digits > no_of_digits:
            no_of_digits = fn_digits

        # add the fibonacci number
        fib_list.append(fn)

        # increase the term and counter
        c += 1
        term += 1

    return term


if __name__ == "__main__":
    digits = 1000
    number = n_digit_fibonacci(digits)
    print(f"Index of the first fibonacci number with {digits} digits is {number}")
from pymath.xbonacci.fibonacci import fib


def even_fibonacci(a, b, limit):
    """
    Find the all the even numbers in a fibonacci sequence up to the given limit
    :param a Starting point of fibonacci sequence
    :param b second number of the sequence
    :param limit Limit of fibonacci sequence
    :return: list of all the even fibonacci numbers
    :rtype: list
    """
    return list(filter(lambda x: x % 2 == 0, fib(a, b, limit)))


if __name__ == "__main__":
    limit_ = 4_000_000
    print(f"Even fibonacci numbers up to {limit_} {even_fibonacci(0, 1, limit_)}")
    print(
        f"Sum of even fibonacci numbers up to {limit_} {sum(even_fibonacci(0, 1, limit_))}"
    )


def fib(a, b, end):
    c = 0
    fib_list = [a, b]
    if end == 0:
        return fib_list
    while c < end:
        nxt = fib_list[c] + fib_list[c + 1]
        fib_list.append(nxt)
        c += 1
        if nxt >= end:
            break
    return fib_list


def fib_memo(n):
    """
    uses memoization to reduce calculations by retrieving what has already been calculated
    :param n: number
    :return: resulting fibonacci
    """
    known = {0: 0, 1: 1}
    if n in known:
        return known[n]

    res = fib_memo(n - 1) + fib_memo(n - 2)
    known[n] = res
    return res


def nth_fibonacci(n):
    """
    Takes an integer n and returns the nth fibonacci
    :return: nth fibonacci
    """
    # edge cases
    if n < 0:
        raise Exception("Value in series can not be negative")
    elif n in [0, 1]:
        return n

    # we'll be building the fibonacci series from the bottom up
    # so we'll need to track the previous 2 numbers at each step
    prev_prev = 0  # 0th fibonacci
    prev = 1  # 1st fibonacci

    for _ in range(n - 1):
        # Iteration 1: current = 2nd fibonacci
        # Iteration 2: current = 3rd fibonacci
        # Iteration 3: current = 4th fibonacci
        # To get nth fibonacci ... do n-1 iterations.
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current


def tribonacci(sig, n):
    res = sig
    c = 0
    if n == 0:
        return []
    elif n in range(1, 4):
        return sig[0:n]
    while c <= n:
        next = res[c] + res[c + 1] + res[c + 2]
        res.append(next)
        c += 1
        if len(res) == n:
            break
    return res


def nth_tribonacci(n: int) -> int:
    sig = [0, 1, 1]

    if n in sig:
        return n

    first = sig[0]
    second = sig[1]
    third = sig[2]

    for _ in range(3, n + 1):
        fourth = first + second + third
        first = second
        second = third
        third = fourth

    return third
