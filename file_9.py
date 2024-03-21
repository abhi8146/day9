'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

FibArray = [0, 1]
 
def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib
 
# Driver Program
 
print(fibonacci(8))


# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

s1 = "Hello how are you"
s2 = "Hello how is"

s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

# 3.)Wrire a code print the 8th fibanochi number

num = 5
n1 = 0
n2 = 1
ans= 0+1

n1 = 1
n2 = 1
ans = 1+1

n1 = 1
n2 = 2
ans = 2+3

num = 5
n1 = 0
n2 = 1

for val in range(5):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)

# ! constructors

class profile:
    def _init_(self):
        print("hello world")

obj = profile()
obj_init_()


# ? Eg:2

# !parametarised constructors
class profile:
    def _init_(self,id,name,age):
        print(id,name,age)

obj = profile(1,"Abhi",12)

# ! Eg:3
class c1:
    email = "abhinaik@gmail.com"
    
    name = "Abhi"
    place = "cbe"
    def m1(self):
        name = "Abhi"
        place = "cbe"
        print(name,place)
        print(self.email)
        
object = c1()
object.m1()


# ? Eg:4

class c1:
    def m1(self):
        name = "Abhi"
        age = 21
        return name,age

    def display(self):
        print(name,age)
        print(self,name,self,age)
        print(self.m1())
        
object = c1()
object.display()


# ? Eg:5
class class1:
    email = "Abhi@gmail.com"  #static variable
    def _init_(self):
        self.name = "Abhi"    #instance variable
        self.email = "abhi@gmail.com"
        return name, email # error --> cannot use return with constructor
    def display(self):     #instance method
        print(self.name,self.email)

c1 = class1()
c1.display()

# ! -----> Intheritance
# The process of utilising the methods and attributes of parent
# Throught the object of child class it is called as inheritance

# 5 types of inheritance
   --> single inheritance
   --> multilevel inheritance
   --> multiple inheritance
   --> hybrid inheritance
   --> heirarichal inheritance

# * single inheritance
It has only one parent class and only one child class

# Eg:1
class parent:
    def m1(self):
        print("Iam child class")

class child(parent):
    def m2(self):
        print("Iam child class")

obj = child()
obj.m1()


# ! Eg:2
class c1:
    def _init_(self):
        print("Iam constructor from parent class")

class child1(c1):
    pass
obj = child1()

# ! Eg:3
class parent:
    name = 'Abhi"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()




# ! multilevel inheritance:

# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("brak")

class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def cat_voice(self):
        print("speak")


all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()

# ! Eg:2

class honda_city:
    def engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
        print(self, cc, hp, torque, fuel_type, num_of_piston)

        def body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class amaze:
        def amaze_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def amaze_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class civic(amaze):
        def civic_engine_specs(self, cc, hp, torque, fuel_type, num_of_piston):
            print(self, cc, hp, torque, fuel_type, num_of_piston)

        def civic_body_specs(self,  color, weight, height, lenght, vehicle_type):
            print(color, weight, height, lenght, vehicle_type)

class honda:
    pass

honda= Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")
        


# ! multiple inheritance:
# ? It has multiple parent and 1 child
# ! Eg;1

class while_petrol:
    def function1(self):
        print("used to Airplans")

class organic_petrol:
    def function_o(self):
        print("used for bike, cars")

class premium_petrol:
    def function_p(self):
        print("sports car, bikes")

class petrol(white_petrol, organic_petrol, premium_petrol):
    def defanition(self):
        print("petrols type")

p=petrol()
p.defanition()

# ! Eg:2
# MRO --> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
        
    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
        
calc = division() 
# calc.add(3, 4)
calc.mul(4, 2)


# ! Hybrid inheritance:
The one parent class will asct as parent for all the child classes

  def weight(self,weight):
        print("weight")
    def display(self,color,taste):
        print(color,taste)
class Tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste= "neutral taste"
        self.display(color,taste)
class carrot(catagory):
    def carrot_specs (self):
        color="green"
        taste= "sweet"
        self.display(color,taste)


                    
        
# ! Hybrid inheritance:
# ? The combination of above 4 inheritanceis called hybrid inheritance
class c1:
    def m1(self):
        print("class1")
class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class3")

class c4(c2):
    def m4(self):
        print("class4")

class c5:
    def m5(self):
        print("class4")

class c6(c5,c4,c3,c2,c1):
    def m6(self):
        print("class4")
obj = c6()
obj.m3()

# ! --------> polymorphism
# Poly - many, morph---> form
# A function which has the ability to perform more than 1 functionality
# Then it is considered to be as plioymorphism

# * plioymorphism in builtion functions
# len()---> which is used to find the length of list,tuple,dict etc..
# Index()
# Max()
# Min()
# Count()
# Pop()
# and more..

# * plioymorphism in operators
# *
# print(8+8)
# print("K"+"1")
# print([1,2,3]+[5,6])
'''

# *
print(6*7)
l1 = {12,3,4,5,6}
print(*l1)
def f1(*args)

l1 = [1,2,3,4,5,6]
print(l1*10)








