def daily_temperatures(temperatures):
    stack = []
    days = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            days[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    
    return days
    



print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# expected: [1, 1, 4, 2, 1, 1, 0, 0]

print(daily_temperatures([30, 40, 50, 60]))
# expected: [1, 1, 1, 0]

print(daily_temperatures([30, 60, 90]))
# expected: [1, 1, 0]

print(daily_temperatures([90, 80, 70]))
# expected: [0, 0, 0]