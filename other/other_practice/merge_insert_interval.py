




def merge_insert_interval(intervals, new_interval):
    output = []
    position = 0
    
    # append all preceeding intervals to output
    while position < len(intervals):
        cur = intervals[position]
        start = cur[0]
        end = cur[1]

        if end < new_interval[0]:
            output.append(cur)
            position += 1
        else:
            break
            


    while position < len(intervals) and intervals[position][0] <= new_interval[1]:
        start = min(new_interval[0], intervals[position][0])
        end = max(new_interval[1], intervals[position][1])
        new_interval = [start, end]
        position += 1     

    output.append(new_interval)

    while position < len(intervals):
        output.append(intervals[position])
        position += 1

    return output







intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]
print(merge_insert_interval(intervals, new_interval))
