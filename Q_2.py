def calculate_range(numbers):
    if len(numbers) < 3:
        return "Range determination not possible"
    min_value = min(numbers)
    max_value = max(numbers)
    return max_value - min_value

arr = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    arr.append(ele)
result = calculate_range(arr)
print(result)