# Second session

# 1
print("#### Exercise 1 ####")
my_list = ['Alex', 'Python Instructor', 'DevOps Expert', 'my phone number']
print(my_list[0])
for i in my_list:
    print(i)

# 2
print('#' * 50)
print("#### Exercise 2 ####")

new_list = []
lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 4, 3, 2, 1]

if len(lst1) != len(lst2):
    print("Lists must be of the same length")
else:
    for i in range(0, 5):
        x = lst1[i]
        y = lst2[i]
        if x > y:
            new_list.append(x)
        if x < y:
            new_list.append(y)
        if x == y:
            new_list.append(x)

print(new_list)

# 3
print('#' * 50)
print("#### Exercise 3 ####")

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list = [1, 2, 3, 4, 5, 6, 's', 7, 8, 9] # Uncomment this line to test what happens when the list contains a string
odd = 0
even = 0
for i in my_list:
    if isinstance(i, str):
        print(f"It's a string!!!")
        even = 0
        odd = 0
        break
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"The of even numbers: {even}")
print(f"The number of odd numbers: {odd}")


# 4
print('#' * 50)
print("#### Exercise 4 ####")


def sum_list(list1):
    l_sum = 0
    for n in list1:
        l_sum += n
    return l_sum


list_of_numbers = [44, 33, 99, 110]
sum_of_list_of_numbers = sum_list(list_of_numbers)
print(f"The addition of numbers is: {sum_of_list_of_numbers}")


# 5
print('#' * 50)
print("#### Exercise 5 ####")


def multiply_list(list1):
    l_mul = list1[0]
    for n in list1[1:]:
        l_mul = l_mul * n
    return l_mul


list_of_numbers = [9, 9, 9, 10]
mul_of_list_of_numbers = multiply_list(list_of_numbers)
print(f"The multiplication of all numbers is: {mul_of_list_of_numbers}")


# 6
print('#' * 50)
print("#### Exercise 6 ####")


def find_min_number(list1):
    return min(list1)


list_of_numbers = [55, 77, 88, 11]
print(find_min_number(list_of_numbers))


# 7
print('#' * 50)
print("#### Exercise 7 ####")

upper_letters = 0
lower_letters = 0


def count_upper_lower_cases(string):
    for letter in string:
        if letter.isupper():
            global upper_letters
            upper_letters += 1
        if letter.islower():
            global lower_letters
            lower_letters += 1


my_str = "This IS a sTrinG comPOSeD of UppeR aNd 1232323 lOWeR cAseS"
count_upper_lower_cases(my_str)
print(f"Number of lower case characters: {lower_letters}")
print(f"Number of upper case characters: {upper_letters}")
