# Algorithmic Methods of Data Mining (Sapienza, 2026-2027) - Homework 1, Problem 1
# %% [Introduction] Say "Hello, World!" With Python  (https://www.hackerrank.com/challenges/py-hello-world)
if __name__ == '__main__':
    print("Hello, World!")

# %% [Introduction] Python If-Else  (https://www.hackerrank.com/challenges/py-if-else)
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

# %% [Introduction] Python: Arithmetic Operators  (https://www.hackerrank.com/challenges/python-arithmetic-operators)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

# %% [Introduction] Python Division  (https://www.hackerrank.com/challenges/python-division)
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

# %% [Introduction] Python Loops  (https://www.hackerrank.com/challenges/python-loops)
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)

# %% [Introduction] Write a function  (https://www.hackerrank.com/challenges/write-a-function)
def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0 and year % 100 != 0:
        leap = True

    return leap


# %% [Introduction] Python Print  (https://www.hackerrank.com/challenges/python-print)
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")

# %% [Data Types] Lists  (https://www.hackerrank.com/challenges/python-lists)
if __name__ == '__main__':
    N = int(input())
    numbers = []
    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            numbers.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(numbers)
        elif command[0] == "remove":
            numbers.remove(int(command[1]))
        elif command[0] == "append":
            numbers.append(int(command[1]))
        elif command[0] == "sort":
            numbers.sort()
        elif command[0] == "pop":
            numbers.pop()
        elif command[0] == "reverse":
            numbers.reverse()

# %% [Data Types] Tuples  (https://www.hackerrank.com/challenges/python-tuples)
def old_hash(t):
    mask = (1 << 64) - 1
    x = 0x345678
    mult = 1000003
    for i, item in enumerate(t):
        x = ((x ^ hash(item)) * mult) & mask
        mult += 82520 + 2 * (len(t) - i - 1)
    x = (x + 97531) & mask
    if x >= (1 << 63):
        x -= (1 << 64)
    return x
if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(old_hash(t))

# %% [Data Types] List Comprehensions  (https://www.hackerrank.com/challenges/list-comprehensions)
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    coordinates = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    print(coordinates)

# %% [Data Types] Finding the percentage  (https://www.hackerrank.com/challenges/finding-the-percentage)
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    average = sum(marks) / len(marks)
    print(f"{average:.2f}")

# %% [Data Types] Nested Lists  (https://www.hackerrank.com/challenges/nested-list)
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    grades = sorted(set(student[1] for student in students))
    second_lowest = grades[1]
    names = sorted(
        student[0] for student in students
        if student[1] == second_lowest
    )
    for name in names:
        print(name)

# %% [Data Types] Find the Runner-Up Score!  (https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(set(arr))
    scores.sort(reverse=True)
    print(scores[1])

# %% [Strings] Text Alignment  (https://www.hackerrank.com/challenges/text-alignment)
thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c +
           (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# %% [Strings] Text Wrap  (https://www.hackerrank.com/challenges/text-wrap)


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


# %% [Strings] Designer Door Mat  (https://www.hackerrank.com/challenges/designer-door-mat)
N, M = map(int, input().split())
# Parte superiore
for i in range(N // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))
# Parte centrale
print("WELCOME".center(M, "-"))
# Parte inferiore
for i in range(N // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))

# %% [Strings] String Formatting  (https://www.hackerrank.com/challenges/python-string-formatting)
def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(width),
              octal.rjust(width),
              hexadecimal.rjust(width),
              binary.rjust(width))


# %% [Strings] Alphabet Rangoli  (https://www.hackerrank.com/challenges/alphabet-rangoli)
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    lines = []

    for i in range(size):
        letters = alphabet[size-1:i:-1] + alphabet[i:size]
        row = "-".join(letters)
        lines.append(row.center(width, "-"))

    print("\n".join(lines[::-1] + lines[1:]))


# %% [Strings] Capitalize!  (https://www.hackerrank.com/challenges/capitalize)


# Complete the solve function below.

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))


# %% [Strings] The Minion Game  (https://www.hackerrank.com/challenges/the-minion-game)
def minion_game(string):
    kevin = 0
    stuart = 0
    n = len(string)
    for i in range(n):
        if string[i] in "AEIOU":
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


# %% [Strings] Merge the Tools!  (https://www.hackerrank.com/challenges/merge-the-tools)
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        result = ""

        for char in substring:
            if char not in result:
                result += char

        print(result)


# %% [Strings] String Split and Join  (https://www.hackerrank.com/challenges/python-string-split-and-join)
def split_and_join(line):
    words = line.split(" ")
    result = "-".join(words)
    return result


# %% [Strings] What's Your Name?  (https://www.hackerrank.com/challenges/whats-your-name)
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


# %% [Strings] Swap Case  (https://www.hackerrank.com/challenges/swap-case)
def swap_case(s):
    return s.swapcase()


# %% [Strings] Mutations  (https://www.hackerrank.com/challenges/python-mutations)
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


# %% [Strings] Find a string  (https://www.hackerrank.com/challenges/find-a-string)
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count


# %% [Strings] String Validators  (https://www.hackerrank.com/challenges/string-validators)
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

# %% [Sets] Introduction to Sets  (https://www.hackerrank.com/challenges/py-introduction-to-sets)
def average(array):
    unique = set(array)
    return round(sum(unique) / len(unique), 3)


# %% [Sets] Symmetric Difference  (https://www.hackerrank.com/challenges/symmetric-difference)
m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

result = sorted(a.symmetric_difference(b))

for x in result:
    print(x)

# %% [Sets] No Idea!  (https://www.hackerrank.com/challenges/no-idea)
n, m = map(int, input().split())

arr = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

print(happiness)

# %% [Sets] .add()  (https://www.hackerrank.com/challenges/py-set-add)
n = int(input())

countries = set()

for i in range(n):
    country = input()
    countries.add(country)

print(len(countries))

# %% [Sets] .discard(), .remove() & .pop()  (https://www.hackerrank.com/challenges/py-set-discard-remove-pop)
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))

# %% [Sets] .union() Operation  (https://www.hackerrank.com/challenges/py-set-union)
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
print(len(english.union(french)))

# %% [Sets] .intersection() Operation  (https://www.hackerrank.com/challenges/py-set-intersection-operation)
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
print(len(english.intersection(french)))

# %% [Sets] .difference() Operation  (https://www.hackerrank.com/challenges/py-set-difference-operation)
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
print(len(english.difference(french)))

# %% [Sets] .symmetric_difference() Operation  (https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation)
n = int(input())
english = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
print(len(english.symmetric_difference(french)))

# %% [Sets] Set Mutations  (https://www.hackerrank.com/challenges/py-set-mutations)
n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    operation, length = input().split()
    B = set(map(int, input().split()))
    if operation == "update":
        A.update(B)
    elif operation == "intersection_update":
        A.intersection_update(B)
    elif operation == "difference_update":
        A.difference_update(B)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(B)

print(sum(A))

# %% [Sets] The Captain's Room  (https://www.hackerrank.com/challenges/py-the-captains-room)
K = int(input())
rooms = list(map(int, input().split()))
unique_rooms = set(rooms)
captain = (K * sum(unique_rooms) - sum(rooms)) // (K - 1)

print(captain)

# %% [Sets] Check Subset  (https://www.hackerrank.com/challenges/py-check-subset)
T = int(input())
for _ in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))

# %% [Sets] Check Strict Superset  (https://www.hackerrank.com/challenges/py-check-strict-superset)
A = set(map(int, input().split()))
N = int(input())
result = True
for _ in range(N):
    B = set(map(int, input().split()))
    if not A > B:
        result = False

print(result)

# %% [Collections] Company Logo  (https://www.hackerrank.com/challenges/most-commons)
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    result = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for char, count in result[:3]:
        print(char, count)

# %% [Collections] collections.Counter()  (https://www.hackerrank.com/challenges/collections-counter)
from collections import Counter
X = int(input())
shoes = Counter(map(int, input().split()))
N = int(input())
total = 0
for _ in range(N):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        total += price
        shoes[size] -= 1

print(total)

# %% [Collections] collections.deque()  (https://www.hackerrank.com/challenges/py-collections-deque)
from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "append":
        d.append(int(command[1]))
    elif command[0] == "appendleft":
        d.appendleft(int(command[1]))
    elif command[0] == "pop":
        d.pop()
    elif command[0] == "popleft":
        d.popleft()

print(*d)

# %% [Collections] DefaultDict Tutorial  (https://www.hackerrank.com/challenges/defaultdict-tutorial)
from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n + 1):
    word = input()
    d[word].append(i)
for _ in range(m):
    word = input()
    if word in d:
        print(*d[word])
    else:
        print(-1)

# %% [Collections] Collections.namedtuple()  (https://www.hackerrank.com/challenges/py-collections-namedtuple)
from collections import namedtuple
N = int(input())
Student = namedtuple('Student', input().split())
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(N)) / N:.2f}")

# %% [Collections] Collections.OrderedDict()  (https://www.hackerrank.com/challenges/py-collections-ordereddict)
from collections import OrderedDict
n = int(input())
items = OrderedDict()
for _ in range(n):
    *name, price = input().split()
    name = " ".join(name)
    items[name] = items.get(name, 0) + int(price)

for name, total in items.items():
    print(name, total)

# %% [Collections] Word Order  (https://www.hackerrank.com/challenges/word-order)
from collections import OrderedDict
n = int(input())
words = OrderedDict()
for _ in range(n):
    word = input().strip()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(*words.values())

# %% [Collections] Piling Up!  (https://www.hackerrank.com/challenges/piling-up)
from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))
    top = float('inf')
    possible = True
    while cubes:
        if cubes[0] >= cubes[-1]:
            cube = cubes.popleft()
        else:
            cube = cubes.pop()
        if cube > top:
            possible = False
            break
        top = cube

    print("Yes" if possible else "No")

# %% [Date and Time] Calendar Module  (https://www.hackerrank.com/challenges/calendar-module)
import calendar
month, day, year = map(int, input().split())
day_number = calendar.weekday(year, month, day)

print(calendar.day_name[day_number].upper())

# %% [Date and Time] Time Delta  (https://www.hackerrank.com/challenges/python-time-delta)

#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    formato = "%a %d %b %Y %H:%M:%S %z"
    data1 = datetime.strptime(t1, formato)
    data2 = datetime.strptime(t2, formato)

    differenza = abs((data1 - data2).total_seconds())

    return str(int(differenza))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()


# %% [Exceptions] Exceptions  (https://www.hackerrank.com/challenges/exceptions)
T = int(input())
for _ in range(T):
    a, b = input().split()
    try:
        a = int(a)
        b = int(b)
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# %% [Built-ins] Zipped!  (https://www.hackerrank.com/challenges/zipped)
N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(list(map(float, input().split())))
for student in zip(*scores):
    print(f"{sum(student) / X:.1f}")

# %% [Built-ins] Python Sort-Sort  (https://www.hackerrank.com/challenges/python-sort-sort)
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key=lambda x: x[k])
    for row in arr:
        print(*row)


# %% [Built-ins] Ginorts  (https://www.hackerrank.com/challenges/ginorts)
s = input()
lower = sorted(c for c in s if c.islower())
upper = sorted(c for c in s if c.isupper())
odd = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)

print(''.join(lower + upper + odd + even))

# %% [Functionals] Map and Lambda Function  (https://www.hackerrank.com/challenges/map-and-lambda-expression)
cube = lambda x: x ** 3

def fibonacci(n):
    result = []
    a, b = 0, 1

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    return result




# %% [Regex and Parsing] Introduction to Regex  (https://www.hackerrank.com/challenges/introduction-to-regex)
import re

T = int(input())

for _ in range(T):
    s = input()
    pattern = r'^[+-]?[0-9]*\.[0-9]+$'
    print(bool(re.fullmatch(pattern, s)))

# %% [Regex and Parsing] Re.split()  (https://www.hackerrank.com/challenges/re-split)
regex_pattern = r"[,.]"

# %% [Regex and Parsing] Group(), Groups() & Groupdict()  (https://www.hackerrank.com/challenges/re-group-groups)
import re
s = input()

match = re.search(r'([a-zA-Z0-9])\1', s)

if match:
    print(match.group(1))
else:
    print(-1)

# %% [Regex and Parsing] Re.findall() & Re.finditer()  (https://www.hackerrank.com/challenges/re-findall-re-finditer)
import re
s = input()
pattern = r'(?<=[^aeiouAEIOU\W\d_])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU\W\d_])'

matches = re.findall(pattern, s)

if matches:
    print('\n'.join(matches))
else:
    print(-1)

# %% [Regex and Parsing] Re.start() & Re.end()  (https://www.hackerrank.com/challenges/re-start-re-end)
import re
s = input()
k = input()
matches = list(re.finditer(r'(?={})'.format(re.escape(k)), s))

if matches:
    for match in matches:
        print((match.start(), match.start() + len(k) - 1))
else:
    print((-1, -1))

# %% [Regex and Parsing] Regex Substitution  (https://www.hackerrank.com/challenges/re-sub-regex-substitution)
import re
n = int(input())
for _ in range(n):
    s = input()
    s = re.sub(r'(?<= )&&(?= )', 'and', s)
    s = re.sub(r'(?<= )\|\|(?= )', 'or', s)
    print(s)

# %% [Regex and Parsing] Validating Phone Numbers  (https://www.hackerrank.com/challenges/validating-the-phone-number)
import re
N = int(input())
for _ in range(N):
    number = input()

    if re.fullmatch(r'[789][0-9]{9}', number):
        print("YES")
    else:
        print("NO")

# %% [Regex and Parsing] Validating and Parsing Email Addresses  (https://www.hackerrank.com/challenges/validating-named-email-addresses)
import re
import email.utils
n = int(input())
pattern = r'[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}'
for _ in range(n):
    line = input()
    name, address = email.utils.parseaddr(line)

    if re.fullmatch(pattern, address):
        print(email.utils.formataddr((name, address)))

# %% [Regex and Parsing] Validating Roman Numerals  (https://www.hackerrank.com/challenges/validate-a-roman-number)
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"



# %% [Regex and Parsing] Validating Postal Codes  (https://www.hackerrank.com/challenges/validating-postalcode)

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"


# %% [Regex and Parsing] Incorrect Regex  (https://www.hackerrank.com/challenges/incorrect-regex)
import re
T = int(input())
for _ in range(T):
    s = input()
    try:
        if re.search(r'(?<!\\)[*+?]{2,}', s):
            print(False)
        else:
            re.compile(s)
            print(True)
    except re.error:
        print(False)

# %% [Regex and Parsing] Hex Color Code  (https://www.hackerrank.com/challenges/hex-color-code)
import re
n = int(input())
css = '\n'.join(input() for _ in range(n))

pattern = r'(?<![\w#])#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![\w])'

blocks = re.findall(r'\{([^{}]*)\}', css, re.DOTALL)

for block in blocks:
    for color in re.findall(pattern, block):
        print(color)

# %% [Regex and Parsing] HTML Parser - Part 1  (https://www.hackerrank.com/challenges/html-parser-part-1)
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for name, value in attrs:
            print("->", name, ">", value)
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for name, value in attrs:
            print("->", name, ">", value)

n = int(input())
html = "\n".join(input() for _ in range(n))
parser = MyHTMLParser()
parser.feed(html)

# %% [Regex and Parsing] HTML Parser - Part 2  (https://www.hackerrank.com/challenges/html-parser-part-2)
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# %% [Regex and Parsing] Detect HTML Tags, Attributes and Attribute Values  (https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values)
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for name, value in attrs:
            print("->", name, ">", value)
parser = MyHTMLParser()
N = int(input())
for _ in range(N):
    parser.feed(input())
parser.close()

# %% [Regex and Parsing] Validating UID  (https://www.hackerrank.com/challenges/validating-uid)
T = int(input())
for _ in range(T):
    uid = input().strip()

    valid = (
        len(uid) == 10
        and uid.isascii()
        and uid.isalnum()
        and len(set(uid)) == 10
        and sum(c.isupper() for c in uid) >= 2
        and sum(c.isdigit() for c in uid) >= 3
    )

    print("Valid" if valid else "Invalid")

# %% [Regex and Parsing] Validating Credit Card Numbers  (https://www.hackerrank.com/challenges/validating-credit-card-number)
import re
N = int(input())
for _ in range(N):
    card = input()

    pattern = r'^[456]\d{3}(-?\d{4}){3}$'

    if re.fullmatch(pattern, card):
        digits = card.replace('-', '')

        if re.search(r'(\d)\1{3}', digits):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")

# %% [Regex and Parsing] Matrix Script  (https://www.hackerrank.com/challenges/matrix-script)
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ""

for col in range(m):
    for row in range(n):
        decoded += matrix[row][col]

decoded = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded)

print(decoded)


# %% [XML] XML 1 - Find the Score  (https://www.hackerrank.com/challenges/xml-1-find-the-score)

def get_attr_number(node):
    return sum(len(element.attrib) for element in node.iter())

# %% [XML] XML2 - Find the Maximum Depth  (https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth)


maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth = max(maxdepth, level + 1)

    for child in elem:
        depth(child, level + 1)


# %% [Closures and Decorators] Decorators 2 - Name Directory  (https://www.hackerrank.com/challenges/decorators-2-name-directory)


def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return [f(person) for person in people]
    return inner


# %% [Closures and Decorators] Standardize Mobile Number Using Decorators  (https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators)
def wrapper(f):
    def fun(l):
        numbers = []
        for number in l:
            number = number[-10:]
            number = "+91 " + number[:5] + " " + number[5:]
            numbers.append(number)
        f(numbers)
    return fun

# %% [NumPy] Arrays  (https://www.hackerrank.com/challenges/np-arrays)

def arrays(arr):
    return numpy.array(arr, dtype=float)[::-1]


# %% [NumPy] Shape and Reshape  (https://www.hackerrank.com/challenges/np-shape-reshape)
import numpy
arr = list(map(int, input().split()))
result = numpy.array(arr).reshape(3, 3)
print(result)

# %% [NumPy] Transpose and Flatten  (https://www.hackerrank.com/challenges/np-transpose-and-flatten)
import numpy
n, m = map(int, input().split())
arr = numpy.array([list(map(int, input().split())) for _ in range(n)])
print(numpy.transpose(arr))
print(arr.flatten())

# %% [NumPy] Concatenate  (https://www.hackerrank.com/challenges/np-concatenate)
import numpy
n, m, p = map(int, input().split())
arr1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
arr2 = numpy.array([list(map(int, input().split())) for _ in range(m)])
print(numpy.concatenate((arr1, arr2), axis=0))

# %% [NumPy] Zeros and Ones  (https://www.hackerrank.com/challenges/np-zeros-and-ones)
import numpy
shape = tuple(map(int, input().split()))
print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))

# %% [NumPy] Eye and Identity  (https://www.hackerrank.com/challenges/np-eye-and-identity)
import numpy
numpy.set_printoptions(legacy='1.13')
N, M = map(int, input().split())
print(numpy.eye(N, M))

# %% [NumPy] Floor, Ceil and Rint  (https://www.hackerrank.com/challenges/floor-ceil-and-rint)
import numpy
numpy.set_printoptions(legacy='1.13')
A = numpy.array(list(map(float, input().split())))
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

# %% [NumPy] Array Mathematics  (https://www.hackerrank.com/challenges/np-array-mathematics)
import numpy
N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(numpy.floor_divide(A, B))
print(numpy.mod(A, B))
print(numpy.power(A, B))

# %% [NumPy] Sum and Prod  (https://www.hackerrank.com/challenges/np-sum-and-prod)
import numpy
N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.prod(numpy.sum(A, axis=0)))

# %% [NumPy] Min and Max  (https://www.hackerrank.com/challenges/np-min-and-max)
import numpy
N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.max(numpy.min(A, axis=1)))

# %% [NumPy] Mean, Var, and Std  (https://www.hackerrank.com/challenges/np-mean-var-and-std)
import numpy
N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(round(numpy.std(A), 11))

# %% [NumPy] Dot and Cross  (https://www.hackerrank.com/challenges/np-dot-and-cross)
import numpy
N = int(input())
A = numpy.array([list(map(int, input().split())) for _ in range(N)])
B = numpy.array([list(map(int, input().split())) for _ in range(N)])
print(numpy.dot(A, B))

# %% [NumPy] Inner and Outer  (https://www.hackerrank.com/challenges/np-inner-and-outer)
import numpy
A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))
print(numpy.inner(A, B))
print(numpy.outer(A, B))

# %% [NumPy] Polynomials  (https://www.hackerrank.com/challenges/np-polynomials)
import numpy
P = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(P, x))

# %% [NumPy] Linear Algebra  (https://www.hackerrank.com/challenges/np-linear-algebra)
import numpy
N = int(input())
A = numpy.array([list(map(float, input().split())) for _ in range(N)])
print(round(numpy.linalg.det(A), 2))

# ---------------------------------------------------------------------------
# Problem 2
# ---------------------------------------------------------------------------

# %% [Problem 2] Birthday Cake Candles  (https://www.hackerrank.com/challenges/birthday-cake-candles)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    massimo = max(candles)
    return candles.count(massimo)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# %% [Problem 2] Kangaroo  (https://www.hackerrank.com/challenges/kangaroo)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#


def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# %% [Problem 2] Strange Advertising  (https://www.hackerrank.com/challenges/strange-advertising)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def viralAdvertising(n):
    shared = 5
    total = 0

    for day in range(n):
        liked = shared // 2
        total += liked
        shared = liked * 3

    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# %% [Problem 2] Recursive Digit Sum  (https://www.hackerrank.com/challenges/recursive-digit-sum)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k

def superDigit(n, k):
    total = sum(int(digit) for digit in n) * k

    while total >= 10:
        total = sum(int(digit) for digit in str(total))

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

# %% [Problem 2] Insertion Sort - Part 1  (https://www.hackerrank.com/challenges/insertionsort1)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr

def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2

    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1

    arr[i + 1] = value
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

# %% [Problem 2] Insertion Sort - Part 2  (https://www.hackerrank.com/challenges/insertionsort2)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr

def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
