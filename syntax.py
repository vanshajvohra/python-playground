from collections import deque
from array import array

print("Hello World")
print("chomu" in "Hackathon")
print('chomu'.find('c'))
is_hot = True
name = "yippee"
if is_hot: print(name)
print('e' in name)
print(name.find('p'))
print(len(name))
# inputted_name = input("enter new name - ")
# print(inputted_name)
# if inputted_name == "chomucho": print("abc")
for num in range(4):
    print(num)

def functionOne():
    print("You are inside functionOne. ")
functionOne()

def functionTwo(*digits):
    total = 0
    for number in digits:
        total = total + number
    print(total)

functionTwo(19, 18, 3, 22, 45)

def functionThree(*numeros):
    prod = 1
    for numero in numeros:
        prod *= numero
    print(prod)

functionThree(45, 25, 40, 75)

# Lists
listOne = [8, 0, 5]
matrixOne = [[1, 2], [3, 4], [4, 5]]
print(matrixOne[2][1])

# Stack
emptyStackOne = []
emptyStackOne.append(234)
print(emptyStackOne)
emptyStackOne.pop()
print(emptyStackOne)

# Double Ended Queues
emptyQueueOne = deque([])
emptyQueueOne.append(79)
emptyQueueOne.append(89)
print(emptyQueueOne)
emptyQueueOne.popleft()
print(emptyQueueOne)

# Arrays
# we already did from array import array
arrayOne = array("i", [1, 2, 3])
print(arrayOne)
arrayOne.append(4)
print(arrayOne)
arrayOne.pop()
print(arrayOne)

# Strings
planet = 'Pluto'
print(planet[0])
print(len(planet))

# Dictionaries
numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])
numbers['eleven'] = 11
print(numbers)

# List Comprehensions
# to loop through characters in a string - for char in s:
squares = [n**2 for n in range(7)]
print(squares)
names = ['Fighter', 'and', 'the', 'Warriors']
proper_nouns = [name for name in names if len(name) > 3]
print(proper_nouns)

# Classes
class Point:
   def __init__(self, x, y):
       self.x = x
       self.y = y

   @classmethod
   def zero(cls):
       cls(0, 0)
    
   def draw(self):
       print(f"The point is ({self.x}), ({self.y})")
       
myPoint = Point(1, 2)
myPoint.draw() # point is an object of class Point
myPoint.y
myPoint.x
myPointTwo = Point(3, 4)
myPointTwo.y = 7
myPointTwo.draw()

# Properties in Python
class Product:
    def __init__(self, price):
        self.price = price # This is how we set an attribute price
    
    @property # decorator
    def price(self):
        return self.__price
    
    @price.setter # decorator
    def price(self, value):
        if value < 0: raise ValueError("Price cannot be negative")
        self.__price = value

product = Product(10)
print(product.price)


 # Simple Inheiritance
class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("Eats food")

class Mammal(Animal):
    def heloo(self):
        print('hello')

m = Mammal()
print(m.age)

# Lists again
individual_chars = list("Hello World")
print(individual_chars)
clean_chars = [s for s in individual_chars if s.isalnum()]
print(clean_chars)
print(clean_chars[4])
nums = list(range(20))
print(nums[::2]) # to print alternate numbers

# List unpacking
numbers = [1, 2, 3, 4]
first, second, *third = numbers
print(first)
print(second)
print(third)
list_unpacking_example_list = ["a", 1, 3, 5, 7, 9, "z"]
lu_first, *others, lu_last = list_unpacking_example_list
print(lu_first)
print(*others)
print(lu_last)

# Looping in lists
loop_list_example = ["abcd", 32, "z", True]
for l in loop_list_example:
    print(l)

# to get indices and their corresponding elements
# we use enumerate() function to convert our list into a tuple
for index, letter in enumerate(loop_list_example):
    print(index, letter)

# Sorting through a tuple
example_for_sorting = [("Product 1", 10), ("product 7", 3)]

list_comprehension_even = [x*2 for x in range(5)]
print(list_comprehension_even)

set_comprehension_even = {x * 2 for x in range(5)}
print(set_comprehension_even)

# Dictionary comrehensions
dict_comprehension_eg = {x: x*2 for x in range(5)}
print(dict_comprehension_eg)

# Exercise
# Find the most repeated character in some text
sentence = "This is a common interview question."
character_count = {} # [] is a list, () is a tuple\
for char in character_count:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1
        
# Hash Map/Dictionary Implementation in Python
empty_dict = {}
not_empty_dict = {1: 1, 2: 4, 3: 9, 4: 16}
# Checking for existence using the key
print(3 in not_empty_dict)
