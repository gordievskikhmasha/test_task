import textwrap

text = input("Введите текст: ")

formatted_text = textwrap.fill(text, width=70, break_long_words=False)

print(formatted_text)