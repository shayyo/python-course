

file_name = "encrypted.txt"
with open(file_name) as f:
    encrypted_text = f.read().lower()

letters_to_occurrences = {}
for i in encrypted_text:
    if not i.isalpha():
        continue
    letters_to_occurrences[i] = letters_to_occurrences.get(i, 0) + 1

letters_to_occurrences_sorted = dict(reversed(sorted(letters_to_occurrences.items(), key=lambda item: item[1])))
most_common_enc_str = list(letters_to_occurrences_sorted)[:4]
most_common_english = ['e', 't', 'o', 'f']
most_common = {}
for i in range(4):
    n = {most_common_english[i]: most_common_enc_str[i]}
    m = {most_common_enc_str[i]: most_common_english[i]}
    most_common.update(n)
    most_common.update(m)

################################################
unencrypted_text = ""
for i in encrypted_text:
    if i in most_common:
        unencrypted_text += most_common[i]
    else:
        unencrypted_text += i

print(unencrypted_text)
