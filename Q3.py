def sum_of_cubes(N):
    if N < 0:
        return "Invalid input"
    sum = 0
    for i in range(1, N + 1):
        sum += i**3
    return sum

N = int(input("Enter N: "))
result = sum_of_cubes(N)
print(f"Sum of cubes of first {N} natural numbers is {result}")
