import sys

f_name = "my_id.txt"
print("#### Exercise 1 ####")

try:
    with open(f_name, 'w') as fh:
        fh.write("Name: Shay Yosef\nAge: 40\nAge: 40\nPhone_number: 05077733377\n")
        print("File successfully created")
except:
    print("Error creating file")
    sys.exit(1)


print("#### Exercise 2 ####")


def count_word_occurrences(file):
    with open(file, 'r') as fh:
        text = fh.read()
    text_list = text.split()
    already_counted = []
    word_dict = {}
    for w in text_list:
        if w not in already_counted:
            count = text_list.count(w)
            word_dict.update({w: count})
            already_counted.append(w)
    return word_dict


print(count_word_occurrences(f_name))
