### BASIC PYTHON
# problem : How to write multiline program in python
multiline = "My Name is " + \
           "Md Sajjad hosen " + \
           "Noyon"
print(multiline)
# problem : Use of Quotation in python
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
# problem : Suppose this the year 2021. You have to input a number which is your birthdate and calculate your age.
birth_year = int(input('Enter your birthdate: '))
present_year = 2021
age = present_year - birth_year + 1
print(f"Your age is: {age}")
# problem : You are given a weight in pound(lbs) and you have to convert it in kilograms
weight_lbs = float(input('Weight (lbs): '))
weight_kg = weight_lbs * 0.45;
print(weight_kg)
# problem : calculate the expression x = (10 / 2 + 3) * 5 * 2 ^ 4 and print the result
x = (10 / 2 + 3) * 5 * 2 ** 4
print(x)



### STRING
str = 'Hello World!'
print(str)                  # Prints complete string
print(str[0])               # Prints first character of the string
print(str[2:5])             # Prints characters starting from 3rd to 5th
print(str[2:])              # Prints string starting from 3rd character
print(str * 5)              # Prints string five times
print(str + "TEST")         # Prints concatenated two strings
# problem : Some string related build in methods
course = 'Python for Begginer'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.find('r Begg'))
print(course.replace('Begginer', 'Absolute Begginer'))
print('python' in course)
isdecimal(), title(), swapcase(), strip([char]), split([char/string]),
max(str), min(str), islower(), isupper(), isdigit(), isalpha(), join(),



### NUMBERS & LIST & TUPLE
# Some build in function
abs(x), ceil(x)
cmp(x, y) => -1 if x < y, 0 if x == y, or 1 if x > y
exp(x), fabs(x), floor(x), log(x), log10(x)
max(x1, x2, x3, ....)
min(x1, x2, x3, ....)
pow(x, y) => x^y, round(x, n),  sqrt(x)

# LIST functions
cmp(list1, list2)
len(list1)
max(list1)
min(list2)
list(seq) => convert a tuple into list
# LIST methods
list.append(obj)
list.count(obj)
list.index(obj)
list.insert(index, obj)
list.pop(obj) => remove and returns
list.remove(obj)
list.reverse()
list.sort() / list.sort(cmp_function)
# TUPLE methods
cmp(tuple1, tuple2)
len(tuple)
max(tuple)
min(tuple)
tuple(sequence) => convert a lint into tuple

# You have a number of list. print the list such that every number appear in the list is distinct
numbers = [2, 2, 3, 4, 5, 6, 4, 6, 7]
uniques = []
for number in numbers:
    if uniques.count(number) == 0 or number not in uniques: # you can check with any one condition
        uniques.append(number)
print(uniques)



### UNPACKING
coordinate = (1, 2, 3)
x, y, z = coordinate
print(f"{x}, {y}, {z}")
List = [1, 2, 3]
x, y, z = List
print(f"{x}, {y}, {z}")
x, y, z = map(int, input().split())
print(f"{n} + {m} = {n + m}")
# you are given a number n and a list. You have to print the list in sorted order.
n = int(input())
List = list(map(int, input().split()))
List.sort()
for i in range(0, len(List)):
    print(List[i], end=', ')



### DICTONARY
# some methods
d.clear()
d.copy()
d.get(key, default=None) => returns value or default if key not in dictionary
d.has_key(key) => Returns true if key in dictionary dict, false otherwise
d.items() => Returns a list of dictionary d's (key, value) tuple pairs
d.update()
d.values() => Returns list of dictionary dict's values

# You are given a number and you have to print the spelling of each digit
# Input: 12345
# Output: One Two Three Four Five
# If you don't map any digit, then print exclamatory sign(!).

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
phone = input("Phone: ")
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
# given a string. You have to print the string with this emoji

message = input("> ")
words = message.split(' ')
emojis = {
    # keyboard shortcut for emoji: windows + .
    ":)": "😄",
    ":(": "😪"
}
output = ""
for word in words:
    output += emojis.get(word, word) + ' '
print(output)
# Use of get: If you don't get any word in the list, then after using get function with dictory gives extra facilities.



### FUNCTION




### FILTER FUNCTION




### FILE READ & WRITE

with open("plain_text.txt", mode="r") as read_file:
    words_all = []
    for line in read_file.readlines():
        words = line.strip().split(" ")
        words_all += words

    unique_words = set(words_all)
    print(len(words_all))
    print(len(unique_words))

    with open("unique_words.txt", mode="w") as write_file:
        for item in unique_words:
            write_file.write(item)
            write_file.write("\n")

print("finished")



