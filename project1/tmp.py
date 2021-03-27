

# Original encrypted text
encrypted_text = "AB DMF GR YGI"

# Original known data
letter_switcher = {
    'M': 'A', 'Y': 'B', 'C': 'D',
    'A': 'M', 'T': 'F', 'I': 'G',
    'S': 'R', 'B': 'Y', 'G': 'I'
}

# Init a new dict to add key => value pairs which are missing from 'letter_switcher'
incremental = {}
for key, value in letter_switcher.items():
    if value not in letter_switcher:
        incremental.update({value: key})

# Merge the two dictionaries
letter_switcher.update(incremental)

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
