import time
from functools import lru_cache

@lru_cache(maxsize=2)
def some_work(n):
    time.sleep(n)
    return n
# if __name__ == '__main__':
print("NOW running some work")
some_work(3)
print("CALLING...WAIT")
some_work(3)
print("called successfully")
