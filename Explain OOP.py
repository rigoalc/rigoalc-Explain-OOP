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
    house_type = 'Single family'
    
    # 'self' is always the first argument
    def _init_(self):
        self.color = 'white'
        
    # Custom methods   
    def color(self):
        # 'self' alows acces the instace state
        print("The", house_type, "House, is color", self.color)
        
# Create an instance to use the class
my_house_instance = House()
# Call the methods
my_house_instance.color()
