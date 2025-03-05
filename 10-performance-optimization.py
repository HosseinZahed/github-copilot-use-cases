# The function below calculates the sum of squares of numbers from 1 to n.
def sum_of_squares_not_optimized(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

# Example usage:
print(sum_of_squares_not_optimized(1000000))  # Output: 333332833333500000

# What's the big-O complexity of the above function?

# Optimized the above function

