def merge(intervals):
    output = []
    if not intervals:
        return output
    intervals.sort()

    output.append(intervals[0])
    
    START = 0
    END = 1

    for i in range(1, len(intervals)):
        last = output[-1]
        cur = intervals[i]

        if cur[START] <= last[END]:
            output[-1][END] = max(last[END], cur[END])
        else:
            output.append(cur)

    return output






print(merge([[1,3], [2,6], [8,10], [15,18]]))
# expected: [[1,6], [8,10], [15,18]]

print(merge([[1,4], [4,5]]))
# expected: [[1,5]]

print(merge([[1,4], [0,4]]))
# expected: [[0,4]]

print(merge([[1,4], [2,3]]))
# expected: [[1,4]]

print(merge([]))
# expected: []