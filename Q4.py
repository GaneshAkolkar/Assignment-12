def sum_of_odd_numbers(N):
    if N < 0:
        return "Invalid input"
    sum = 0
    for i in range(1, 2 * N, 2):
        sum += i
    return sum

N = int(input("Enter N: "))
result = sum_of_odd_numbers(N)
print(f"Sum of first {N} odd natural numbers is {result}")
