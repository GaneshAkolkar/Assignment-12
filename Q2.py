def sum_of_squares(N):
    if N < 0:
        return "Invalid input"
    sum = 0
    for i in range(1, N + 1):
        sum += i**2
    return sum

N = int(input("Enter N: "))
result = sum_of_squares(N)
print(f"Sum of squares of first {N} natural numbers is {result}")
