
# Create a program that will print your identifications.
name = "Shay Yosef"
age = 40
print(f"My name is {name} and I am {age}")


# For a string that you created please check if:
print('#' * 50)
s = "this is a string"
if s[7] == 'a' and s[8] == 'b' and s[9] == 'c':
    print("True")
else:
    print("False")


# Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.
print('#' * 50)

text = "elephantsAreBig dogsAreSmall"
t1 = text.split()[0]
t2 = text.split()[1]

t1_two_first_char = t1[:2]
t1_new = t1_two_first_char[1]
t1_new += t1_two_first_char[0]
t1_new += t1[2:]

t2_two_first_char = t2[:2]
t2_new = t2_two_first_char[1]
t2_new += t2_two_first_char[0]
t2_new += t2[2:]

print(t1_new, t2_new)

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
print('#' * 50)

s = "Driving"
if len(s) >= 3:
    if s[len(s)-3:] == "ing":
        s = s[-len(s):len(s)-3] + "ly"
print(s)


# For a string (three characters and more) that you have created please create a new string that follows the next rules:
print('#' * 50)

orig_string = "this is the original string"
mid_char_of_orig_str = orig_string[int(len(orig_string) / 2)] # The first character of the new string is the middle character of the original string
last_char_of_orig_str = orig_string[-1] # The middle character of the new string is the last character of the original string
first_char_of_orig_str = orig_string[0] # The last character of the new string is the first character of the original string

new_string = f"{mid_char_of_orig_str}{last_char_of_orig_str}{first_char_of_orig_str}"
print("This is the new string:")
print(new_string)


# Write a Python function to insert a string in the space of the original string.
# You can assume that there is just one space in your string.
print('#' * 50)


def insert_text(string):
    fixed_string = "Python 3.0"
    combined_string = fixed_string.split()[0]
    combined_string += " " + string + " "
    combined_string += fixed_string.split()[1]
    print(combined_string)


insert_text("added_text")


