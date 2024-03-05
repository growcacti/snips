class OrderedDictionary:
    def __init__(self):
        self._keys = []
        self._values = []

    def __len__(self):
        return len(self._keys)

    def __getitem__(self, key):
        if self.has_key(key):
            return self._values[self._keys.index(key)]
        else:
            return None

    def __setitem__(self, key, value):
        if self.has_key(key):
            self._values[self._keys.index(key)] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __delitem__(self, key):
        val = self[key]
        self._keys.remove(key)
        self._values.remove(val)

    def has_key(self, aKey):
        return aKey in self._keys

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        return zip(self._keys, self._values)


docstr = """The provided code defines a class called OrderedDictionary, which implements a dictionary-like data structure with ordered keys. This class can be used to store key-value pairs, similar to a regular dictionary, but it preserves the order of the keys as they are inserted.

Here's how you can use this program:

    Creating an instance of the OrderedDictionary class:

python

my_dict = OrderedDictionary()

    Adding key-value pairs to the dictionary:

python

my_dict['key1'] = 'value1'
my_dict['key2'] = 'value2'

    Accessing values by key:

python

value1 = my_dict['key1']  # Returns 'value1'

    Modifying values by key:

python

my_dict['key2'] = 'new_value'

    Deleting a key-value pair:

python

del my_dict['key1']

    Checking if a key exists in the dictionary:

python

if my_dict.has_key('key2'):
    print("Key 'key2' exists in the dictionary")

    Getting a list of keys:

python

key_list = my_dict.keys()  # Returns a list of keys

    Getting a list of values:

python

value_list = my_dict.values()  # Returns a list of values

    Getting a list of key-value pairs:

python

item_list = my_dict.items()  # Returns a list of tuples [(key1, value1), (key2, value2)]

Note that the code you provided has a couple of typos:

    In the __len__ method, sef.keys should be self._keys.
    In the items method, map(None, self._keys, self._values) should be zip(self._keys, self._values).

Once these typos are fixed, you can use the OrderedDictionary class as described above."""
