def insert(intervals, newInterval):

    # handle if no newInternval
    if not newInterval:
        return intervals
    
    index = 0
    output = []
    START = 0
    END = 1

    # append all preceeding intervals to output
    while index < len(intervals) and intervals[index][END] < newInterval[START]:
        output.append(intervals[index])
        index += 1
    
    # merge new interval
    while index < len(intervals) and intervals[index][START] <= newInterval[END]:
        newInterval[START] = min(newInterval[START], intervals[index][START])
        newInterval[END] = max(newInterval[END], intervals[index][END])
        index += 1

    output.append(newInterval)

    # append remaining intervals to output
    while index < len(intervals):
        output.append(intervals[index])
        index += 1

    
    return output



print(insert([[1,3], [6,9]], [2,5]))
# expected: [[1,5], [6,9]]

print(insert([[1,2], [3,5], [6,7], [8,10], [12,16]], [4,8]))
# expected: [[1,2], [3,10], [12,16]]

print(insert([], [5,7]))
# expected: [[5,7]]

print(insert([[1,5]], [2,3]))
# expected: [[1,5]]

print(insert([[1,5]], [6,8]))
# expected: [[1,5], [6,8]]