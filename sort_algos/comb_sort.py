def comb_sort(unsorted):
    shrink_factor = 1.3
    gap = len(unsorted)
    swapped = True

    while gap > 1 or swapped:
        # Update the gap value for a next comb
        gap = int(float(gap) / shrink_factor)

        swapped = False
        i = 0

        while gap + i < len(unsorted):
            if unsorted[i] > unsorted[i + gap]:
                # Swap values
                unsorted[i], unsorted[i + gap] = unsorted[i + gap], unsorted[i]
                swapped = True
            i += 1

    return unsorted
