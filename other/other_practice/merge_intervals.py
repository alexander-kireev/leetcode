




def merge_intervals(intervals):
    
    intervals = sorted(intervals)
    output = [intervals[0]]
    

    # FIX INFINITE LOOP
    for start, end in intervals[1:]:
        last = output[-1]

        if start <= last[1]:
            last[1] = max(last[1], end)
        else:
            output.append([start, end])

    return output

intervals = [[1,3], [15,18], [2,6], [8,10]]

intervals = sorted(intervals)
print(merge_intervals(intervals))