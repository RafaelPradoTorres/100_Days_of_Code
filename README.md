# 100 Days of Code (Python) Projects
Hii! 👋
This is a little big portfolio that i'm making while i'm studying the course ministered by Angela Yu
https://www.udemy.com/course/100-days-of-code/

Well, in this document, I'll explain each af the projects, and what I've learned in them.

## 1st week

### Day 01 - Basic Functions, string manipulation and variables
Functions:
- print()
- len()
- input()

setting variable
- variable_name = <value>

String manipulation:
- new line: '\n'
- concatenation: <string> + <string>

### Day 02 - Data Types, errors and number manipulation
Function:
- type(<var>)

- str()
- int()
- float()
- bool()

- round()

String manipulation:
- str_var[index]  -> <char_in_index>
- str_var[-index] -> <char_negative_count>

- fstrings -> f"string content {<var>}"

Number mannipulation:
- 123_456_789 == 123456789, but it's easier to read

operations:
- x - y
- x + y
- x * y
- x / y
- x % y
- x // y
- x ** y
- (x + y) * z

Data types:
- integer
- string
- boolean
- string

### Day 03 - Logic
conditionals:
- if <condition1>:
-   ...
- elif <condition2>
-   ...
- elif <condition3>
-   ...
- else:
-   ...

Logical operators:
- x > y
- x < y
- x <= y
- x >= y
- x == y
- x != y

Multiline string:
- '''
- line 1 content
- line 2 content
- .
- .
- line n content
- '''

Atualizing variables:
- +=
- -=
- *=
- /=

### Day 04 - Import modules | Lists
- import <mudule name>
- from <module name> import <something>

Random module:
- randint(x, y) -> integer between (including) x and y
- random() -> float between 0 and 1
- uniform(x, y) -> float between (including) x and y
- choice(<list>) -> choose a value in a list
- shuffle(<list>) -> shuffle a list

List:
- Declaring -> list_name = [x, y, ..., z]
- Accessing -> list_name[i]
- Append method -> list_name.append(<value>)
- Extend method -> list_name.extend([ <value1>, <value2>, ... ])

### Day 05 - For loops
For (list)
- for item in list:
-   ...

For (range)
- for number in range(begin, end, step): #end is not inclusive
-   ...
    
Functions:
- range(x, y)
- max(<list>)
- min(<list>)
- sun(<list>)

### Day 06 - Defining functions
Define a function
- def function_name():
-   ...

Call the function
- function_name()

### Day 07 - Small Hangman project:
String methods
- .lower()
- .upper()
- .title()

<img width="149" height="248" alt="image" src="https://github.com/user-attachments/assets/91571884-049b-4f3e-b560-d8c3796158ad" />
  
## 2nd week
### Day 08 - Arguments in functions
Argument in a function
- def func_name(arg1, arg2, ...):
- ...

Calling the function with positional arguments:
- func_name(value1, value2, ...):

You can use keywords arguments:
- func_name(arg1= value1, arg2= value2)

Return the position of an item in a list:
- .index()

Comments:
- # the message ignored by the interpreter
- # TODO 1 : asdjasldjsalkdj

### Day 09 - Introduction do dictionaries | while loop
Defining a dictionary:
- dict_name = {
- 'key1' = value1
- ...
- 'keyN' = valueN
- }

Accessing a key:
- dict_name["keyN"]

Iterating through the dictionary:
- for key in dictionary_name
- | print(key)
- | print(dictionary_name[key])

While loop:
- while <condition>:
- |
- |

### Day 10 - Functions with outputs | Docstring
Returning a value from a function:
- def func_name():
- |
- |
- | return <something>

logic operators:
<x> or <y>
<x> and <y>

you can return inside a scope:
- def funct_name():
- |
- | if <something>
- | | return <x>
- |
- | return <z>

Well, to keep your functions well documented, you can use DOCSTRING
- def funct_name(<something>):
- | """ Receives something and return somethink
- | yeah
- | you are beaultiful """
- |
- | return <somethink>

well... the code of this day is cool, so... maybe I should review it sometime

### Day 11 - Blackjack project
<img width="535" height="716" alt="image" src="https://github.com/user-attachments/assets/41ff384d-08b4-42c1-9701-a5eb446390e7" />

### Day 12 - 









