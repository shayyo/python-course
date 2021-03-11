

print("#### Exercise 1 ####")
my_dict = {'fname': 'Shay', 'lname': 'Yosef', 'age': 40, 'phone': '0507774455'}
print(my_dict)

print("#### Exercise 2 ####")


def replace_char(lst):
    try:
        lst[4] = '@'
        return lst
    except IndexError:
        print("No such index")


lst1= ['a', 'b', 'c', 'd', 'e', 'f']
lst2 = ['a', 'b', 'c', 'd']
print(replace_char(lst1))
print(replace_char(lst2))


print("#### Exercise 3 ####")


def replace_char_assertion(lst):
    assert len(lst) >= 5, "Length of list is lower than 5"
    lst[4] = '@'
    return lst


lst1 = ['a', 'b', 'c', 'd', 'e', 'f']
print(replace_char_assertion(lst1))


print("#### Exercise 4 ####")


def update_dict(my_dict, key_value):
    my_dict.update(key_value)
    return my_dict


d = {'address': 'my address'}
print(update_dict(my_dict, d))


print("#### Exercise 5 ####")

num_dict = {}
addition = 3
for i in range(1, 6):
    current_dict_item = {i: (i + addition)}
    num_dict.update(current_dict_item)
    i += 1
print(num_dict)


print("#### Exercise 6 ####")

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {}
for i in dic1, dic2, dic3:
    new_dict.update(i)
print(new_dict)


print("#### Exercise 7 ####")


def count_characters(string):
    char_num_dict = {}
    already_counted = []
    for letter in string:
        if letter in already_counted:
            continue
        else:
            n = string.count(letter)
            char_num_dict.update({letter: n})
            already_counted.append(letter)
    return char_num_dict


print(count_characters("this is my string"))


print("#### Exercise 8 ####")