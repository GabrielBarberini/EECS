from datetime import datetime
from optimized_sel_sort import optm_sel_sort
from book_sel_sort import sel_sort

L = list(range(1,50))
L.reverse()

print("Book sel sort")
before = datetime.now()
print("Before sort:", before)
sel_sort(L)
print("Sorted list:", L)
after = datetime.now()
print("After sort:", after)
print("Diff:", after-before, "\n")

L.reverse()
print("Optimized sel sort")
before = datetime.now()
print("Before sort:", before)
optm_sel_sort(L)
print("Sorted list:", L)
after = datetime.now()
print("After sort:", after)
print("Diff:", after-before)
