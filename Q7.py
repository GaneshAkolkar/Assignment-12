def count_digits(n):
    return len(str(n))

num = int(input("Enter a number: "))
result = count_digits(num)
print(f"Number of digits in {num} is {result}")
