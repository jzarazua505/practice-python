# phrase = "My_name_Jeff"
# words = []
# new_word = ""
# for c in phrase:
#     if c != " ":
#         new_word += c
#     else:
#         words.append(new_word)
#         new_word = ""
# words.append(new_word)

# rev_words = words[::-1]
# rev_phrase = ""
# for i in range(len(rev_words)):
#     if i > 0:
#         rev_phrase += " "
#     rev_phrase += rev_words[i]
# print(rev_phrase)

phrase2 = "My name Jeff"
words = phrase2.split()  # <- ["My", "name", "Jeff"]
words.reverse()
rev_phrase = " ".join(words)
print(rev_phrase)
