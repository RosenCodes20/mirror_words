import re

some_string = input()
found_mirror_words = r"@[a-zA-Z]{3,}@@[a-zA-Z]{3,}@|#[a-zA-z]{3,}##[a-zA-Z]{3,}#"
words_dict = {}
find_words = re.findall(found_mirror_words, some_string)
is_pared = False
mirror_words = []
for word in find_words:
    word_regex = r"\w+"
    found_words = re.findall(word_regex, word)
    if found_words:
        is_pared = True
        for words in found_words:
            if words not in words_dict:
                words_dict[words] = found_words[1]
            if words in words_dict.keys():
                break
if is_pared:
    print(f"{len(find_words)} word pairs found!")
else:
    print("No word pairs found!")
for k, v in words_dict.items():
    if k == v[::-1]:
        mirror_words.append(f"{k} <=> {v}")
if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")
