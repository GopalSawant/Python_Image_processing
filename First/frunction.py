#parameters
def greet(name="Darth vader", emoji="Angry"):
    print(f"Hello {name}, {emoji} !!!")

#arguments
greet("sawant", "smile")

#keyword argument
greet(emoji="smile",name="Gopal")
    
#will call default parameter
greet()
greet("Yoda")
 
