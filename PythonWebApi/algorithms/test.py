from utility import GenerateRandomArray
from maximumsubarrayproblem import find_max_crossing_subarray
from maximumsubarrayproblem import find_maximum_subarray
from heap import heap


Array=GenerateRandomArray(10)
print(Array)

h=heap(Array)

print(h.array)

h.heap_increase_key(5,400)

print(h.array)

h.max_heap_insert(300)

print(h.array)

