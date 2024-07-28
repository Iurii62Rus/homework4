my_string = input("Введите произвольный текст: ")
print("Количество символов в введённом тексте:", len(my_string))
print('Uppercase text', my_string.upper())
print('Uppercase text', my_string.lower())
my_string_no_spaces = my_string.replace(" ", "")
print("Text without spaces:", my_string_no_spaces)
print("First character of line:", my_string[0])
print("Last character of the line:", my_string[-1])

