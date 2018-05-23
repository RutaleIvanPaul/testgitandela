print("Stuff")
import math
print(math.sqrt(16))

print("""This Should
Appear Like this
on the console""")

print("here is a string"+"\t here is more")

print("single quote' double quote \"")
''' name=input("Input Name:")
print(name) '''
print("Input Name:\n")
#name=input()
print(r"This would skip \n but the r stops it.")
print("This string five times\n"*5)
#Slicing strings
stringer="this new string"
print(stringer[3])
print(stringer[3:6])
print(len(stringer))
#Lists
listone=[12,33,4,22,4,32,23]
print(listone[2])
listone[2]=444
listone.append(404)
print(listone)
listone[:3]=[]
print(listone)
#elif
name="Ivan"
if name is "Rutale":
    print("Hey Rutax")
#else if(name is "Bucky"):
 #   print("Hey Bucky")
elif name is "Ivan":
    print("Hey Ivan")
else:
    print("None")

#Looping
listtwo=['food','is','life']
for c in listtwo:
    print(c)
#double indexing
print(listtwo[0][1])
for x in range(10):
    print(x)

for y in range(2,12,2):
    print(y)

#MEssing around
print("Concat")
nmbr=9
print(99,'String: ')
''' for x in range(10):
    if x is 4:
        print(4,"has reached.")
        break
 '''
 #Functions now
def firstfunction (x,y):
     return x*y
print(firstfunction(5,4))