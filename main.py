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

listOne = [8, 0, 5]
matrixOne = [[1, 2], [3, 4], [4, 5]]
print(matrixOne[2][1])