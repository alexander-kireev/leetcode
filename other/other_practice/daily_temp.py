







def daily_temp(temperatures):
    days = [0] * len(temperatures)
    stack = []
    
    

    for i, temp in enumerate(temperatures):

        while stack and temp > temperatures[stack[-1]]:
            old_i = stack.pop()
            days[old_i] = i - old_i
        
        stack.append(i)

    return days

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temp(temperatures))