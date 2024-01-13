text_with_brackets = "(Paul O'Neill)"
text_without_brackets = text_with_brackets.strip('(')
text_without_brackets = text_without_brackets.strip(')')
print(text_without_brackets)
