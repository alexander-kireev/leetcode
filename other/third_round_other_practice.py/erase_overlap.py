def erase_overlap_intervals(intervals):
    intervals = sorted(intervals)

    last = intervals[0].copy()
    erased = 0
    i = 1
    START = 0
    END = 1

    while i < len(intervals):
        if last[END] > intervals[i][START]:
            last[START] = min(last[START], intervals[i][START])
            last[END] = min(last[END], intervals[i][END])
            erased += 1
        else:
            last = intervals[i]
        i += 1

    return erased



print(erase_overlap_intervals([[1,2], [2,3], [3,4], [1,3]]))
# expected: 1

print(erase_overlap_intervals([[1,2], [1,2], [1,2]]))
# expected: 2

print(erase_overlap_intervals([[1,2], [2,3]]))
# expected: 0

print(erase_overlap_intervals([[1,100], [11,22], [1,11], [2,12]]))
# expected: 2