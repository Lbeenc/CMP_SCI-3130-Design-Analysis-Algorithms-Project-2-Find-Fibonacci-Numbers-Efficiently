import time
from functools import lru_cache

# Recursive Method with Memoization
@lru_cache(maxsize=None)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def measure_recursive(max_n=40):

    n0 = 0
    elapsed = 0

    print("Finding n0 for recursive method...")
    while elapsed < 20 and n0 <= max_n:
        n0 += 1
        start_time = time.perf_counter()  # High-precision timer to count the microseconds
        fib_recursive(n0)
        elapsed = time.perf_counter() - start_time
        print(f"n = {n0}, Execution time: {elapsed:.6f} seconds")  # Show microseconds

    if elapsed < 20:
        print(f"n0 not found within limit of n <= {max_n}.")
        return n0

    print(f"n0 found: {n0} (Execution time: {elapsed:.2f} seconds)")
    return n0

# faster Dynamic Programming Method
def fib_dynamic(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

def measure_dynamic(n):
    start_time = time.perf_counter()
    result = fib_dynamic(n)
    elapsed_time = time.perf_counter() - start_time
    print(f"Dynamic Programming Method: F({n}) = {result}")
    print(f"Execution time: {elapsed_time:.6f} seconds")  # Microseconds tracking
    return elapsed_time

# Main logic
n0 = measure_recursive(max_n=30)  # Hard limit on recursive calculation so it doesnt use all of my RAM
if n0 > 0:
    measure_dynamic(n0)  # Compare with faster method

# Test for larger numbers
measure_dynamic(5000)
measure_dynamic(10000)
