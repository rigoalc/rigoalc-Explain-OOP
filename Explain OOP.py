# •	For each topic:
# o	Define it with one paragraph
# o	Show a small example of it in Python
# o	Explain how your python example shows the topic, with a paragraph
# o	You may assume the reader has Python knowledge of functions, but not classes


# TOPIC 1 Classes:

# Class is a collection of data and methods. It contains all the materials and procedures that we will use to create an object. 

# In the class, we will be able to build objects based on the materials and conditions included.



# Class declaration
class House():
    # Class variables
    house_type = 'single family'
    # 'self' is always the first argument
    def __init__(self):
        self.color = "white"    
    # Custom methods   
    def white(self):
        # 'self' allows access the instace state
        print("The", self.house_type , "house color is" , self.color)        
# Create an instance to use the class
my_house_instance = House()
# Call the methods
my_house_instance.white()




# In the example we have a class house as an object.

# Inside the class is were with the variables and functions is created a new object. 

# In this case printing the type and color of the House.





# TOPIC 2 Instance:

# Instance in an object included in a class. Every time that object variates is an instance of its class. 

# A Instance it is part of the given class, that has specified values. Instance can be called class instance or class object. 

# #Instantiation can be seen as a construction.  
# 
# An object that belongs to a class Rectangle is an instance of the class.

class House():
    # Class variables
    house_type = 'single family'
    # 'self' is always the first argument
    def __init__(self):
        self.color = "white"    
    # Custom methods   
    def white(self):
        # 'self' allows access the instace state
        print("The", self.house_type , "house color is" , self.color)   
             
# Create an instance to use the class
my_house_instance = House()
# Call the methods
my_house_instance.white()

#In the code example above, we can see the instance my_house_instance included in the class House created at the end of the class.


# •	For each topic:
# o	Define it with one paragraph
# o	Show a small example of it in Python
# o	Explain how your python example shows the topic, with a paragraph
# o	You may assume the reader has Python knowledge of functions, but not classes


# TOPIC 3 Polymorphism:

# Polymorphism is the ability of any data to be processed in more than one form. 
# Poly means many and morphism means types.
# It lets us have methods in the child class with the same name as the methods in the parent class.


class House():
    def apartment(self):
        print("The master room is small")
        
    def color(self):
        print("the apartment color is grey")
    
class ranch(House):
    def color(self): 
        print("The master room is brown")
        
obj_house = House()
obj_ranch = ranch()

obj_house.apartment()
obj_house.color()

obj_ranch.apartment()
obj_ranch.color()


#In the example above we can see polymorphism with Inheritance (We will talk more in the next topic about Inheritance) 
#This is a very useful because it is possible to change a method in the child class that was inherited from the parent class.add()
#The process of re-implementing a method is called Method Overriding.


# TOPIC 4 Inheritance:

#Is the option of a class to inherit all the  properties form other class
#Inheritance represents a real_world relationship well.
#It offer reusability code. Is not necessary to write the same code again and again.


class House():
    
   
    def __init__(self):
        self.color = "white" 
           
    # Custom methods   
    def white(self):
        # 'self' allows access the instace state
        print("The Bungalow color is" , self.color)   
        
class Bungalow(House):
    
    pass

x = House()
y = Bungalow()

my_house_instance = House()
# Call the methods
my_house_instance.white()


#In the example we can see that the properties from the parent class House and inherited by the child class bungalow. 
# The child class bungalow is naming and taking the properties naming the parent class House in his definition.


#Topic 5 Private vs Public variables

# In Python there is no anything that can be called a private private for itself. 
# To create a private member we must place two underscores ( __ ) at the beginning of any variable or method.
# The function of this private member function is that can only be accessed in the class.
# The public variables are created outside of the function called Global Variables, can be used by anyone, inside or inside functions.

class House():  
    def __init__(self):
        self.color = "The house color is Public-White"
        self.__color = "The house color is Private-White"        
    def residences(self):
        print(self.__color)
x = House()
print(x.color)
my_house_instance = House()
# Call the methods
my_house_instance.residences()




# In the example above we can see color as a public being used outside the class House.
# Under that we run the child class residences and print the private variable __color.
# If we want to make the child class residences private, it is possible to add the underscores at the start __residences.
# This could be usefoul for protect values, functions or data stored.

# Topic 6 Multiple Inheritance

#As we say in the Topic 4 Inheritance is the way to re-use code creating a child class.
#Multiple inheritance is when a class derived from multiple classes.
#In other words, the derived class inherit everythong from the base class.

class House():
    def color(self):
        print("The house is white grey")
class Ranch():
    def color(self): 
        print("The ranch is brown")
class Apartment(House,Ranch):
    def color(self):
        House.color(self)
        Ranch.color(self)
        print("The apartment colors are grey and brown")       

c = Apartment()
c.color()

#In the code example we have 2 Base Classes called House and Ranch. The class Apartment derived from the base classes.
#All the features From House and Ranch and passed to Apartment.


#Topic 7 Interfaces / Duck Typing

# An interface can be seen as a blueprint for designing classes. 
# Compared with classes the interfaces define methods but the methods are abstract.
# The interface don't implement the method, the method is implemented by the class, giving a meaning to the interfaces abstract methods.








# In Duck Typing we check for the presence of a given method or attribute.
# The type or the class of an object is less important than the method it defines.
# Duck-typing emphasis what the object can really do, rather than what the object is.






    
 
    
      



