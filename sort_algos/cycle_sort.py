def cycle_sort(unsorted):
    ans = 0

    # Pass through the unsorted to find cycles to rotate.
    for cycleStart in range(0, len(unsorted) - 1):
        item = unsorted[cycleStart]

        # finding the position for putting the item.
        pos = cycleStart
        for i in range(cycleStart + 1, len(unsorted)):
            if unsorted[i] < item:
                pos += 1

        # If the item is already present-not a cycle.
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == unsorted[pos]:
            pos += 1
        unsorted[pos], item = item, unsorted[pos]
        ans += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:

            # Find where to put the item.
            pos = cycleStart
            for i in range(cycleStart + 1, len(unsorted)):
                if unsorted[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates.
            while item == unsorted[pos]:
                pos += 1
            unsorted[pos], item = item, unsorted[pos]
            ans += 1

    return unsorted
