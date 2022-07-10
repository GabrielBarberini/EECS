from datetime import datetime
from tabular import tabu_make_change
from memoization import memo_make_change

print("Memoization")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", memo_make_change(list(range(1,50)), 250))
print("coin_val = [1], change = 250: ", memo_make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")

print("Tabular")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", tabu_make_change(list(range(1,50)), 250))
print("coin_val = [1], change = 250: ", tabu_make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")
