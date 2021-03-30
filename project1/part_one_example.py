

# Original encrypted text
encrypted_text = "AB DMF GR YGI"

# Original known data
letter_switcher = {
    'M': 'A', 'Y': 'B', 'C': 'D',
    'A': 'M', 'T': 'F', 'I': 'G',
    'S': 'R', 'B': 'Y', 'G': 'I'
}

# Add the missing mappings of characters in 'letter_switcher' into a new dictionary
incremental = {}
for key, value in letter_switcher.items():
    if value not in letter_switcher:
        incremental.update({value: key})

# Merge the two dictionaries
print(f"This is the original dictionary:\n{letter_switcher}")
letter_switcher.update(incremental)
print(f"This is the merge dictionary:\n{letter_switcher}")

unencrypted_text = ""
for l in encrypted_text:
    if l == " ":
        unencrypted_text += " "
    elif l in letter_switcher:
        unencrypted_text += letter_switcher[l]
    else:
        unencrypted_text += ''

print(unencrypted_text)
print("#" * 40)
