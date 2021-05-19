phrase = "My name is Julian"
words = []
new_word = ""
for c in phrase:
    if c != " ":
        new_word += c
    else:
        words.append(new_word)
        new_word = ""
words.append(new_word)

rev_words = words[::-1]
rev_phrase = ""
for i in range(len(rev_words)):
    if i > 0:
        rev_phrase += " "
    rev_phrase += rev_words[i]
print(rev_phrase)

