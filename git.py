print("hello world") # Salam Qerdesh
print("Salam de salam") 
class Animal:
    def __init__(self,animalName) -> None:
        self.animalName =animalName
class Mammal(Animal):
    def __init__(self, animalName) -> None:
        super().__init__(animalName)
        print(animalName," a warm blood animal")
