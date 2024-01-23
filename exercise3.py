def print_even_indexed_chars():

    str1 = input("Enter a string: ")

    even_chars = [str1[i] for i in range(len(str1)) if i % 2 == 0]

    for char in even_chars:
        print(char)

print_even_indexed_chars()