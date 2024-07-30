def count_highest_occurrence(input_string):
    char_count = {}

    for char in input_string:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]

    return max_char, max_count


input_string = input("Enter a string: ")
char, count = count_highest_occurrence(input_string)
print(f"The character which occurs the maximum number of times is '{char}' & occurrence count is {count}.")