"""

Estimated Time: 20 mins
"""

text = input("Text: ")

words = text.split()


word_counts = {}
for word in words:
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts)
# print(word_counts)

for word in sorted_words:
    print(f"{word} : {word_counts[word]}")