course = "python for beginners"
print(course)
print(course.upper())
print(course.find('y'))
print(course.find("for"))
print(course.find("python"))
print(course.replace('for','4'))
print(course.replace('beginners','noobs'))
print(course.replace('python','weird snake'))
print('python' in course)
print(10 ** 3)
x = 10
x **= 3
print(x)
y = 3
print(not y>5 and y <10) # and,or,not
temp= input("enter temperature: ")
if int(temp) > 30:
    print("it is a hot day")
    print("stop fucking")
elif int(temp) < 5:
    print("wayyyyyy too cold mate")
else:
    print("go die")
wight = int(input("please enter your wight: "))
x = input("kg or bs: ")
if x=="K" or x=="k":
    print("this is your wight in bs: " + str(wight*2))
elif x=="L"or x=="l":
    print("this is your wight in kg: " + str(wight/2))
else:
    print("Error: please try again later")