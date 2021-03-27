

file_name = "encrypted.txt"
with open(file_name) as f:
    encrypted_text = f.read().lower()

letters_to_occurrences = {}
counted_letter = []

for i in encrypted_text:
    if not i.isalpha():
        continue
    if i == " ":
        continue
    if i not in counted_letter:
        num = encrypted_text.count(i)
        n = {i: num}
        letters_to_occurrences.update(n)
        counted_letter.append(i)

print(letters_to_occurrences)


