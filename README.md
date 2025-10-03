# 100 Days of Code (Python) Projects - First Month
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
- choices(<list>, k=<number of itens to return>) -> return a random list (you can set the weight)
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

### Day 12 - Scopes
Scopes:
- Python does not have local scope in loops, conditionals, etc
- Function Scope
- Global Scope

- You can define a function inside another function

Modifying a global variable inside a function:
- def func_name():
- |
- | global <var>
- | ...

Defining a global constant:
- ALL_IN_CAPS = "value"

### Day 13 - Error handling
Catching Exceptions
- try:
- | <somethin to try>
- except ValueError:
- | <something do do>

Debugger:
- You can set a stop point and use a debugging function in your IDE

### Day 14 - Higher or lower project
<img width="454" height="376" alt="image" src="https://github.com/user-attachments/assets/3c49fbab-865b-4c52-a704-4ad4a26d9ee5" />

## 3rd Week
### Day 15 - Coffee machine
<img width="383" height="501" alt="image" src="https://github.com/user-attachments/assets/bd062169-af89-4b06-91fa-e4b8f96a134e" />

### Day 16 - Intruduction to OOP
Creating an object:
- obj_name = ClassName()
Calling a method:
- obj_name.method()

creating an object and init method :
- class ClassName:
- | def __init__(self, ...)
- | | self.att1 = x
- | | self.att2 = y
- |
- | def method(self, ...):
- | |...


turtle module:
- (GUI module to move a turtle)

Turtle methods:
- .shape()
- .color()
- .foward()

Screen methods:
- .canvheight()
- .exitonclick()

preetyTable:
- (you can make formatted tables)

PreetyTable methods:
- .add_column()

PreetyTable attributes:
- .align

### Day 17 - Quizz game project
<img width="564" height="232" alt="image" src="https://github.com/user-attachments/assets/9643b5c8-7d6d-476d-8699-32e6feab87c6" />

### Day 18 - Exploring Turtle module
Turtle methods:
- .speed()
- .circle()
- .heading()
- .setheading()
- .pencolor()
- .penup()
- .pendown()
- .fd() -> foward
- .lt() -> left
- .right()
- .goto()

heroes library:
- (well, dont worry about it)

Colorgram library:
- you can extract predominant collors from an image

### Day 19
- Event listeners
turtle Screen methods:
- .listen()
- .onkey()
- .setup()
- .textinput()
- .tracer()
- .update()

### Day 20-21 - Snake project
time module:
- .sleep()

<img width="601" height="631" alt="image" src="https://github.com/user-attachments/assets/52ee845e-7576-417a-a81d-55312fa8b88a" />




