i = 1
while i<=5:
    print(i * "*")
    i+=1
name = ["berte","brook","fiker","booo","kooloo"]
name[1]="boy"
print(name[1:4])
numbers = [0,1,2,3,4,5]
numbers.insert(0,-1)
numbers.remove(3)
print(numbers)
print(len(numbers))
for item in numbers:
    print(item)
print("*******************************")
x=0
while x < len(numbers):
    print(x)
    x+=1
print("******************************")
for numb in range(5): #range syntax and understanding of use
    print(numb)
print("******************************")
# tuples they are imutable can not be changed
num = (1,2,3,3,5)
print(num.count(3))
print(num.index(2))