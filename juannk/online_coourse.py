name = 'hee said he "loved me and yet i did not believe him" '
print(name[5:10])
done = True #any number except 0 is true any sting is true unless it is left empty
if done:
    print("yes")
else:
    print("no")
killmanga = True
killmanga1 = False
movie_out = all([killmanga, killmanga1])
print(movie_out)
comple = 2+3j
num = complex(2,3)
print(num.real, num.imag)
print(round(4.9527385543545475))
from enum import Enum
class state(Enum):
    inactive = 0
    active = 1
print(list(state))
# user input
# control statment

condition = True

if condition == True:
    print("the condition")
    print("was true")

# list
dogs = ["Roger", "simba", "brook"]
dogs.append("dogs")
dogs.extend(["cats"])
dogs+= ["gabe"]
dogs+="12d"
dogs.remove("Roger")
print(dogs.pop())
print(len(dogs))
dogs.insert(2,"lverman")
dogs[0:1]=["loverboy","lovergirl"]
dogs.sort()
sorted(dogs,key=str.lower)
print(dogs)
# Tuples
nam = ("Roger", "brook")
nam[0]
nam.index("Roger")
print("brook" in nam)
print(sorted(nam, key=str.lower))
newt_up = nam + ("broooo", "winier")
print(sorted(newt_up, key=str.lower))
# dictionaries
dog= {"name": "berte"}
print(dog["name"])
dog["name"]= "levithen"
print(dog["name"])
print(dog.get("friend","brook"))
print(list(dog.items()))
# sets
niga = {"killer", "winnneerru","berte"}
niga2 = {"berte"}
intresct = niga & niga2
print(intresct)
# function
def hi(namer= "killer"): #paramter
    print("hi "+ namer)

hi("berte") # argument
hi("lover")
hi()
def ikk():
    print("lover boy")

ikk()
