from datetime import datetime
from with_memoization import make_change 
from without_memoization import wo_make_change 

print("With memoization")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", make_change(list(range(1,50)), 250))
print("coin_val = [1], change = 250: ", make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")

print("Without memoization")
before = datetime.now()
print("coin_val = range(1,50), change = 250: ", wo_make_change(list(range(1,50)), 250))
print("coin_val = [1], change = 250: ", wo_make_change([1], 250))
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")
