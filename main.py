import random

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.hamsters = []
        self.order = 0
    
    def add_animal(self, name, kind):
        kind = kind.lower()
        self.order += 1
        
        animal = {"name": name, 
                  "type": kind, 
                  "order": self.order}
        
        if kind == "cat":
            self.cats.append(animal)
        elif kind == "dog":
            self.dogs.append(animal)
        elif kind == "hamster":
            self.hamsters.append(animal)
        else:
            print('Такого вида нет!')
    
    def adopt_any(self):
        orders = []
        if self.cats:
            orders.append(self.cats[0]['order'])
        if self.dogs:
            orders.append(self.dogs[0]['order'])
        if self.hamsters:
            orders.append(self.hamsters[0]['order'])
        minOrder = min(orders)
        
        if minOrder == self.cats[0]['order']:
            return self.adopt_cat()  
        if minOrder == self.dogs[0]['order']:
            return self.adopt_dog()
        if minOrder == self.hamsters[0]['order']:
            return self.adopt_hamster()
                   
    def __adopt_animal__(self, animal_list):
        if len(animal_list) == 0:
            return print("Закончились!")
        else:
            print("Вы забрали: ", animal_list[0]['name'], animal_list[0]['type'])
            return animal_list.pop(0)
   
    def adopt_cat(self):
        return self.__adopt_animal__(self.cats)
    
    def adopt_dog(self):
        return self.__adopt_animal__(self.dogs)
    
    def adopt_hamster(self):
        return self.__adopt_animal__(self.hamsters)
    
    def show_animals(self):
        for i in range(len(self.cats)):
            print("Вид: ", self.cats[i]["type"])
            print("Имя: ", self.cats[i]["name"])
            print("Очередь: ", self.cats[i]["order"])
            
        for i in range(len(self.dogs)):
            print("Вид: ", self.dogs[i]["type"])
            print("Имя: ", self.dogs[i]["name"])
            print("Очередь: ", self.dogs[i]["order"])
            
        for i in range(len(self.hamsters)):
            print("Вид: ", self.hamsters[i]["type"])
            print("Имя: ", self.hamsters[i]["name"])
            print("Очередь: ", self.hamsters[i]["order"])

animalShelter = AnimalShelter()

names = ["beta", 'alpha', 'fenomen', 'eric', 'admin', 'boba', 'sharick', 'kek', 'poop']
kind = [ "cat", "dog", "hamster" ]

for i in range(0, 10):
    animalShelter.add_animal(names[random.randrange(len(names))], kind[random.randrange(len(kind))])

while True:
    print("1. Отобразить животных")
    print("2. Забрать любого")
    print("3. Забрать определенный вид")
    print("4. Отдать в приют")
    print("0. выйти из программы")
    
    cmd = input("Выберите пункт: ")
    
    if cmd == "1":
        animalShelter.show_animals()
    elif cmd == "2":
        animalShelter.adopt_any()
    elif cmd == "3":
        print("Виды: ", kind)
        x = input("Напишите вид: ").lower()
        if x == 'cat':
            animalShelter.adopt_cat()
        if x == 'dog':
            animalShelter.adopt_dog()
        if x == 'hamster':
            animalShelter.adopt_hamster()
    elif cmd == "4":
        print("Виды: ", kind)
        x = input("Напишите вид: ")
        y = input("Напишите имя: ")
        animalShelter.add_animal(y, x)
    elif cmd == "0":
        exit()
    else:
        print("Вы ввели не правильное значение")