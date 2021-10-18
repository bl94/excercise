from abc import ABC, abstractmethod


class Footballer():

    nationality="Norway"

    def __init__(self,name,number,position):
    #CLASS OBJECT ATTRIBUTE

        self.name=name
        self.number=number
        self.position=position
    
    def __str__(self) -> str:
        pass

    #Operations and methods
    def football_charasterics(self):
        print(self.name + " "+ self.number +" "+self.position +" "+ Footballer.nationality)   

new_footballer=Footballer(name="Erling",number="11",position="Forward")
new_footballer.football_charasterics()

class Square():

    def __init__(self,side_of_square=1):
        self.side_of_square = side_of_square
        self.area= side_of_square**2
        self.perimeter = 4*side_of_square
    
    def properties(self):
        print(f"side of square : {self.side_of_square}")
        print(f"Area : {self.area}")
        print(f"Perimeter : {self.perimeter}")
    
my_square=Square()
my_square.properties()

# abstract class
class Animal(ABC):
    def __init__(self,name,age,species):
        self.name=name
        self.age=age
        self.species=species

    def speak(self):
        print(f"I am {self.name}, my age is {self.age}. My species is {self.species}")
    
    @abstractmethod
    def how_look_like():
        pass

class Elephant(Animal):

    def __init__(self,name,age,species,weight):
        super().__init__(name,age,species)
        self.weight=weight

   #Super Methods 
    def __str__(self):
        return self.name
    
    def __len__(self):
        return len(self.name)
    
    def __del__(self):
       print(f"Deleted Elephant object {self.name}")

    def __add__(self):
        print(f"Add Elephant object {self.name}")
    
    def speak(self):
        super().speak()
        print(f"I am Elephant, my weight is {self.weight}")

    def how_look_like(self):
        print("I am big and gray")

class Paroot(Animal):
    def __init__(self,name,age,species,colour):
        super().__init__(name,age,species)
        self.colour=colour

    def speak(self):
        super().speak()
        print(f"I am Parrot, my colour is {self.colour}")

    def how_look_like(self):
        print(f"I am small and {self.colour}")

def main():
    my_elephant=Elephant("Bartek",27,"African Elephant",2000)
    my_elephant.speak()
    my_elephant.how_look_like()
    print(f"Bartek is instance : {isinstance(my_elephant,Elephant)}")
    print(len(my_elephant))
    print(my_elephant)
    my_parrot=Paroot("Bartek",27,"African Parrot","White")
    my_parrot.speak()
    my_parrot.how_look_like()
    print(f"Bartek is instance : {isinstance(my_parrot,Animal)}")

    print("\n")
    """
    zoo=[my_elephant,my_parrot]

    for x in zoo:
        x.speak()
    """
main()
