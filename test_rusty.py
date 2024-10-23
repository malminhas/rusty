import time
import rusty

K=2000000

def test_nonrusty(n):
    """ test function for Python implementation """
    def factorial(n):
        if n <= 1:
            return n
        return n * factorial(n - 1)
    [factorial(n) for i in range(K)]
    
def test_rusty(n):
    """ test function for Rust implementation """
    [rusty.factorial(n) for i in range(K)]
    
if __name__ == '__main__':
    n = 34
    start = time.time()
    test_rusty(n)
    end = time.time()
    rust_time = end-start
    print(f"time for rust code: {round(rust_time,2)} sec")
    start = time.time()
    test_nonrusty(n)
    end = time.time()
    python_time = end-start
    print(f"time for python code: {round(python_time,2)} sec")
    print(f"Rust implementation is {round(python_time/rust_time,2)} times faster than Python one")