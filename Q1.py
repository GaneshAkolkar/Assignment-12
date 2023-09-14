
def sum_of_natural_numbers(N):
    if N < 0:
        return "Invalid input"
    sum = 0
    for i in range(1, N + 1):
        sum += i
    return sum

N = int(input("Enter N: "))
result = sum_of_natural_numbers(N)
print(f"Sum of first {N} natural numbers is {result}")
