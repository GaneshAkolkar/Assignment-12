def decimal_to_octal(n):
    if n < 0:
        return "Invalid input"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n //= 8
    return octal

num = int(input("Enter a decimal number: "))
result = decimal_to_octal(num)
print(f"Octal equivalent of {num} is {result}")
