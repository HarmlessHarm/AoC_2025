from time import time

def timeit(func):
    """Decorator to time a function's execution."""

    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.6f} seconds")
        return result

    return wrapper