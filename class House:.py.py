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