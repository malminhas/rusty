import time
import rusty

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)

def test_nonrusty(n):
    [factorial(n) for i in range(100000)]
    
def test_rusty(n):
    """ test function """
    [rusty.factorial(n) for i in range(100000)]
    
if __name__ == '__main__':
    n = 35
    start = time.time()
    test_rusty(n)
    end = time.time()
    print(f"time for rust code: {end-start}")
    start = time.time()
    test_nonrusty(n)
    end = time.time()
    print(f"time for python code: {end-start}")
