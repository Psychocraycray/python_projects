"""# exercise found on poe for beginner python
# 1
name = input("please enter your name: ")
age = input("please enter your age: ")
print("hello ", name," you are age: ",  age , "years old")
print()
# 2
x = input("please enter the first number to be added: ")
y = input("please enter the second number to be added: ")
Sum=float(x)+float(y)
print("this is your sum: " + str(Sum))
numbers = [1,2,3,4,5]
sum = 0
for num in numbers:
    sum += num
print("the sum is: ",sum)
#3
string = input("enter a string: ")
vowels = "aeiou"
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print("there are",count,"vowels in the string.")
#string = input("please enter a statment: ")
#vowel = "aeiou"
#love = 0
#for char in string:
#      if char.lower() in vowel:
#        love+=1
#print(f"love is vowel and it is equal too {love}")
#4
even = [1,2,3,4,5]
even_num = []
for nums in even:
    if nums % 2 == 0:
        even_num.append(nums)
print("the even numbers:",even_num)
nuz = input("enter a list of numbers: ")
nuz_list = nuz.split(",")
even_nuz =[]
for numz in nuz_list:
    if int(numz)%2 ==0:
        even_nuz.append(int(numz))
print("the even numbers are: ",even_nuz)
#5
cout = input("enter a sentence: ")
word = cout.split()
word.reverse()
print(" ".join(word))"""
#6
tring = input("please enter a list of items: ")
tring_list = tring.split(",")
for trings in tring:
    if len(trings) >4:
        tring_list.append(trings)
print("the long trings are: ",tring_list)
