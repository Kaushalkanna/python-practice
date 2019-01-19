import random


def bogo_sort(unsorted):
    def is_sorted(collection):
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not is_sorted(unsorted):
        random.shuffle(unsorted)
    return unsorted
