class TimeMap:
    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key, timestamp):
        largest = ""
        
        values = self.time_map.get(key)
        if not values or values[0][0] > timestamp:
            return largest

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if timestamp == values[mid][0]:
                return values[mid][1]
            elif timestamp < values[mid][0]:
                right = mid - 1
            else:
                left = mid + 1

        return values[left - 1][1]

time_map = {
    "foo": {
        "value": "bar",
        "timestamp": 1
    }
}

tm = TimeMap()

tm.set("foo", "bar", 1)



print(tm.get("foo", 1))  # expected "bar"
print(tm.get("foo", 3))  # expected "bar"

tm.set("foo", "bar2", 4)



print(tm.get("foo", 4))  # expected "bar2"
print(tm.get("foo", 5))  # expected "bar2"
print(tm.get("foo", 0))  # expected ""

tm.set("user", "active", 2)
tm.set("user", "inactive", 10)

print(tm.get("user", 1))   # expected ""
print(tm.get("user", 2))   # expected "active"
print(tm.get("user", 9))   # expected "active"
print(tm.get("user", 10))  # expected "inactive"

print(tm.get("missing", 5))  # expected ""