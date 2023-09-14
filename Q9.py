num = int(input("Enter a decimal number: "))
def decimal_to_binary(n):
    if n < 0:
        return "Invalid input"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

result = decimal_to_binary(num)
print(f"Binary equivalent of {num} is {result}")
