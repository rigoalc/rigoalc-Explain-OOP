# •	For each topic:
# o	Define it with one paragraph
# o	Show a small example of it in Python
# o	Explain how your python example shows the topic, with a paragraph
# o	You may assume the reader has Python knowledge of functions, but not classes


# TOPIC 1 Classes:

# Class is a collection of data and methods. It contains all the materials and procedures that we will use to create an object. 

# In the class, we will be able to build objects based on the materials and conditions included.

# We can see a class as parts and instructions or plans from an automobile. 

# In this toolbox or shelve we can find all the details for the different parts like chassis, parts, colors, from the car (in this case the object).

# In this example, we can see that a car is an object. This object is created in a class, under methods or functions, with the data or variables included. The object is also called “Instance of a class”; every time we create one object this will be called instantiation.




# Class declaration
class House:
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

class House:
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

class House:
    # Class variables
    object_type = 'house single family'
    # 'self' is always the first argument
    def __init__(self):
        self.color = "white"    
    # Custom methods   
    def white(self):
        # 'self' allows access the instace state
        print("The", self.object_type , "color is" , self.color)   
        
class Car:
    
    object_type = "car sedan" 
     
    def __init__(self):
        self.color = "blue"    
    # Custom methods   
    def white(self):
        # 'self' allows access the instace state
        print("The", self.object_type , "color is" , self.color)  
    
      
# Create an instance to use the class
object_type_instance = House()

object_type_instance.white()

object_type_instance = Car()

object_type_instance.white()

#In The example above, is shows two classes with the same object and same method name.The output will be different depending 
#on the object and attributes declared.



