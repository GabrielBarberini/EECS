from datetime import datetime
from with_memoization import make_change 
from without_memoization import wo_make_change 

print("With memoization")
before = datetime.now()
make_change(range(50), 250)
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")

print("Without memoization")
before = datetime.now()
wo_make_change(range(50), 250)
after = datetime.now()
print("Before call:", before)
print("After call:", after)
print("Diff:", after-before, "\n")
