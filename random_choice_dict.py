import random

my_dict = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange",
}

# Choose a random key-value pair
key, value = random.choice(list(my_dict.items()))

print(f"Key: {key}, Value: {value}")
