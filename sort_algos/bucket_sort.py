from sort_algos.insertion_sort import insertion_sort
import math

DEFAULT_BUCKET_SIZE = 5


def bucket_sort(unsorted, bucket_size=DEFAULT_BUCKET_SIZE):
    if len(unsorted) == 0:
        print('You don\'t have any elements in array!')

    min_value = unsorted[0]
    max_value = unsorted[0]

    # For finding minimum and maximum values
    for i in range(0, len(unsorted)):
        if unsorted[i] < min_value:
            min_value = unsorted[i]
        elif unsorted[i] > max_value:
            max_value = unsorted[i]

    # Initialize buckets
    bucket_count = math.floor((max_value - min_value) / bucket_size) + 1
    buckets = []
    for i in range(0, bucket_count):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(unsorted)):
        buckets[math.floor((unsorted[i] - min_value) / bucket_size)].append(unsorted[i])

    # Sort buckets and place back into input array
    sorted_array = []
    for i in range(0, len(buckets)):
        insertion_sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sorted_array.append(buckets[i][j])

    return sorted_array
