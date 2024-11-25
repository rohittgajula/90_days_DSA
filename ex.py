
def generate_numbers():
    for i in range(5):
        yield i

# Using the generator
for num in generate_numbers():
    print(num)
# Output: 0, 1, 2, 3, 4 (one at a time)
