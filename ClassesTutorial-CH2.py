class Dog:


    breed="LabraDog"
    def bark(self,name): # self is important
        print("BARK!!!",' dear ',name)

    #Constructor - self is just a first parameter and a common practice , we can write any name
    # Providing default values
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color



#myDog=Dog() # Will not work as the constructor is defined
myDog=Dog("Buzo",2,"black")

print("Initial printing of Dog ->",myDog.name,myDog.age,myDog.color)


myDog.bark('tuzo')

## Basically on the fly we associated the properties with the dog
myDog.name="Check-Name"
myDog.Age=21
print(myDog.name,"-",myDog.breed,"-",myDog.Age)

print('Now I am overriding the calss values')
myDog.breed="Yeppi"
print("Breed is overriden to ",myDog.breed)
