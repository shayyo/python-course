
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

