
def main():
    # Read the encrypted file
    file_name = "encrypted.txt"
    with open(file_name) as f:
        encrypted_text = f.read().lower()

    # Get only alphabetic characters from encrypted text into dictionary and count their occurances
    letters_to_occurrences = {}
    for i in encrypted_text:
        if not i.isalpha():
            continue
        letters_to_occurrences[i] = letters_to_occurrences.get(i, 0) + 1

    # Get the dict sorted in a descending sort order.
    letters_to_occurrences_sorted = dict(reversed(sorted(letters_to_occurrences.items(), key=lambda item: item[1])))
    # Read the first 4 characters (which are the 4 most common) from the sorted dict (as a list)
    most_common_enc_str = list(letters_to_occurrences_sorted)[:4]
    # Define the well-known most common characters in English (descending sort order)
    most_common_english = ['e', 't', 'o', 'f']

    # Merged both most common characters to use in deciphering
    most_common = {}
    for i in range(4):
        n = {most_common_english[i]: most_common_enc_str[i]}
        m = {most_common_enc_str[i]: most_common_english[i]}
        most_common.update(n)
        most_common.update(m)

    # Build the unencrypted text based on the most common dictionary
    unencrypted_text = ""
    for i in encrypted_text:
        if i in most_common:
            unencrypted_text += most_common[i]
        else:
            unencrypted_text += i

    print(f"Unencrypted text is:\n{unencrypted_text}\n")

    print("#### PART 2 ####")
#################################################
    my_dict = {'a': 'e', 'c': 'o', 'b': 't', 'e': 'a', 'd': 'r', 'o': 'c', 'r': 'd', 't': 'b'}

    def decrypt_text(txt):
        txt = txt.lower()
        new_txt = ""
        for l in txt:
            if l in my_dict:
                new_txt += my_dict[l]
            else:
                new_txt += l
        print(f"Unencrypted text is:\n {new_txt}")

    enc_text = "///bha Taa3add, bha Tdaer, enr b7ha Fdcccccbbb..."
    decrypt_text(enc_text)


if __name__ == '__main__':
    main()
