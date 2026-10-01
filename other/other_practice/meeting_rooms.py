



def meeting_rooms(intervals):
    intervals.sort()

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
        
    return True






def run_tests():
    tests = [
        ([[0, 30], [5, 10], [15, 20]], False),
        ([[7, 10], [2, 4]], True),
        ([[1, 3], [3, 5]], True),
        ([[1, 10], [2, 3]], False),
        ([[1, 4], [1, 2]], False),
        ([[5, 8]], True),
        ([], True),
        ([[10, 12], [1, 5], [4, 8], [8, 10]], False),
        ([[1, 2], [2, 3], [3, 4]], True),
        ([[3, 6], [6, 9], [2, 3]], True),
    ]

    for i, (intervals, expected) in enumerate(tests, 1):
        result = meeting_rooms(intervals)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        print(f"  Input:    {intervals}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()


run_tests()

