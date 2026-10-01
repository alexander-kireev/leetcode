




def erase_overlap_intervals(intervals):
    START = 0
    END = 1

    if not intervals:
        return 0

    min_remove = 0
    intervals.sort()

    kept = intervals[0]

    for i in range(1, len(intervals)):
        cur = intervals[i]

        if kept[END] > cur[START]:
            min_remove += 1
            
            if cur[END] < kept[END]:
                kept = [cur[START], cur[END]]
        else:
            kept = cur
    
    return min_remove






    














def run_tests():
    tests = [
        # 1. Basic overlap
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),

        # 2. All overlapping
        ([[1, 2], [1, 2], [1, 2]], 2),

        # 3. No overlaps
        ([[1, 2], [2, 3]], 0),

        # 4. One huge interval blocks many smaller ones
        ([[1, 100], [2, 3], [4, 5], [6, 7]], 1),

        # 5. Touching endpoints are allowed
        ([[1, 3], [3, 5], [5, 7]], 0),

        # 6. Nested intervals
        ([[1, 10], [2, 3], [3, 4], [4, 5]], 1),

        # 7. Unsorted input
        ([[3, 4], [1, 2], [2, 3], [1, 3]], 1),

        # 8. Mixed overlaps
        ([[1, 4], [2, 3], [3, 5], [6, 8]], 1),

        # 9. Single interval
        ([[1, 2]], 0),

        # 10. Empty input
        ([], 0),
    ]

    for i, (intervals, expected) in enumerate(tests, 1):
        result = erase_overlap_intervals(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        print(f"  Input:    {intervals}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()


run_tests()