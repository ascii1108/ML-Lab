a = [2,7,4,1,3,6]
def sumisten(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 10:
                count += 1
    return count

count = sumisten(a)
print(count)




