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

class TagCloud: 
    
