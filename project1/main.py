
# Read the encrypted file
file_name = "encrypted.txt"
with open(file_name) as f:
    encrypted_text = f.read().lower()

# Get alphabetic characters of encrypted text into dictionary
letters_to_occurrences = {}
for i in encrypted_text:
    if not i.isalpha():
        continue
    letters_to_occurrences[i] = letters_to_occurrences.get(i, 0) + 1

# Get the dict sorted in a descending sort order.
letters_to_occurrences_sorted = dict(reversed(sorted(letters_to_occurrences.items(), key=lambda item: item[1])))
# Read the first 4 most common characters from the sorted dict (as a list)
most_common_enc_str = list(letters_to_occurrences_sorted)[:4]
# Define the well-known most common characters in English (descending sort order)
most_common_english = ['e', 't', 'o', 'f']

# Build a new merged dict with most common characters to use in deciphering
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
