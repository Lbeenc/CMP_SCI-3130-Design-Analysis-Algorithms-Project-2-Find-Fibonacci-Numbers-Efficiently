import time

def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def measure_recursive(n):
    start_time = time.time()
    result = fib_recursive(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Recursive Method: F({n}) = {result}")
    print(f"Execution time: {elapsed_time:.2f} seconds")
    return elapsed_time

# Find n0 such that the execution time is between 20 and 30 seconds
n0 = 0
elapsed = 0
while elapsed < 20:
    n0 += 1
    elapsed = measure_recursive(n0)

print(f"n0 found: {n0} (Execution time: {elapsed:.2f} seconds)")
