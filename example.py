def reverse_binary(num):

    binary_str = format(num, '032b')
    
    reversed_binary_str = binary_str[::-1]

    reversed_decimal = int(reversed_binary_str, 2)
    return reversed_decimal

# Example usage
number = 12
result = reverse_binary(number)
print(f"Decimal of reversed binary: {result}")
