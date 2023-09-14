def sum_of_even_numbers(N):
    if N < 0:
        return "Invalid input"
    sum = 0
    for i in range(2, 2 * N + 1, 2):
        sum += i
    return sum

N = int(input("Enter N: "))
result = sum_of_even_numbers(N)
print(f"Sum of first {N} even natural numbers is {result}")
