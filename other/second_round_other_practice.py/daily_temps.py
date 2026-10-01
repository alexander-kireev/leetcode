
def daily_temps(temps):
    output = [0] * len(temps)
    stack = []

    for i, temp in enumerate(temps):

        while stack and temp > temps[stack[-1]]:
            output[stack[-1]] = i - stack[-1]
            stack.pop()
            
        stack.append(i)

    return output



temperatures = [73,74,75,71,69,72,76,73]
# Output:      [1,  1, 4, 2, 1, 1, 0, 0]

print(daily_temps(temperatures))