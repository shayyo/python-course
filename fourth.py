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


print("\n#### Exercise 2 ####")


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

print("\n#### Exercise 3 ####")

with open(f_name) as fh:
    for i in range(2):  # read first two lines
        print(fh.readline())


print("\n#### Exercise 4 ####")

t = "this is a text to be checked for the longest word in it"
text = t.split()
longest = 0
for w in text:
    if len(w) > longest:
        longest = len(w)

print(f"The longest word in text is {longest} character long")


print("\n#### Exercise 5 ####")

t = "This is a text to be reversed"

print(t[::-1])


print("\n#### Exercise 6 ####")


class MyClass:

    def get_string(self, string):
        self.print_string(string)

    def print_string(self, string):
        print(string.upper())


obj = MyClass()
obj.get_string('A class object')


print("\n#### Exercise 7 ####")


class Rectangle:

    def calc_rectangle(self, length, width):
        print(f"Results is: {length * width}")


obj = Rectangle()
obj.calc_rectangle(5, 55)