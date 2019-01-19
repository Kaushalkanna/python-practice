from random import randint
from timeit import timeit
import matplotlib.pyplot as plt

from sort_algos.insertion_sort import insertion_sort
from sort_algos.selection_sort import selection_sort
from sort_algos.shell_sort import shell_sort
from sort_algos.tim_sort import tim_sort
from sort_algos.bubble_sort import bubble_sort
from sort_algos.bucket_sort import bucket_sort
from sort_algos.cocktail_shaker_sort import cocktail_shaker_sort
from sort_algos.comb_sort import comb_sort
from sort_algos.counting_sort import counting_sort
from sort_algos.cycle_sort import cycle_sort
from sort_algos.heap_sort import heap_sort
from sort_algos.gnome_sort import gnome_sort
from sort_algos.merge_sort import merge_sort
from sort_algos.merge_sort_fastest import merge_sort as merge_sort_fastest
from sort_algos.pancake_sort import pancake_sort
from sort_algos.quick_sort import quick_sort
from sort_algos.bogo_sort import bogo_sort

LIST_SIZE = 800
TEST_DATA = []


def time_fn(to_call, unordered_list, *args, **kwargs):
    temp_unordered_list = unordered_list.copy()
    wrapped = wrapper(to_call, temp_unordered_list, *args, **kwargs)
    # print(f"running {to_call}")
    d_time = timeit(wrapped, number=1000)
    # print(f"Finished {to_call}")
    return d_time


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def run_test(to_test, test_with, *args, **kwargs):
    return time_fn(to_test, test_with, *args, **kwargs)


print("Testing with a ", LIST_SIZE, " element list...", sep="")
print("Generating and sorting test_sample values...")
test_sample = [randint(-100000, 100000) for i in range(LIST_SIZE)]

# The tests
print("RUNNING TESTS...")

result = {
    "Insertion sort": run_test(insertion_sort, test_sample),
    "Selection sort": run_test(selection_sort, test_sample),
    "Shell sort": run_test(shell_sort, test_sample),
    "Tim sort": run_test(tim_sort, test_sample),
    "Bubble sort": run_test(bubble_sort, test_sample),
    "Bucket sort": run_test(bucket_sort, test_sample),
    "Cocktail Shaker sort": run_test(cocktail_shaker_sort, test_sample),
    "Comb sort": run_test(comb_sort, test_sample),
    "Counting sort": run_test(counting_sort, test_sample),
    "Cycle sort": run_test(cycle_sort, test_sample),
    "Heap sort": run_test(heap_sort, test_sample),
    "Gnome sort": run_test(gnome_sort, test_sample),
    "Merge sort": run_test(merge_sort, test_sample),
    "Merge Fastest sort": run_test(merge_sort_fastest, test_sample),
    "pancake sort": run_test(pancake_sort, test_sample),
    "Quick sort": run_test(quick_sort, test_sample),
    "Bogo sort": run_test(bogo_sort, test_sample),
}

a, b = zip(*sorted(result.items()))
plt.plot(b, a)
plt.show()
