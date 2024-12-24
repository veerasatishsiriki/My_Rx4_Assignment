def find_minimum_platforms(arr, dep):
    # Convert time to minutes past midnight for comparison
    def convert_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes

    arr = sorted([convert_to_minutes(time) for time in arr])
    dep = sorted([convert_to_minutes(time) for time in dep])
    
    n = len(arr)
    i, j = 0, 0
    platforms_needed = 0
    max_platforms = 0

    # Traverse the arrival and departure arrays
    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1

    return max_platforms

# Examples
arr1 = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep1 = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(find_minimum_platforms(arr1, dep1))  # Output: 3
