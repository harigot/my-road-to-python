'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, 
Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso 
tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a 
qualquer momento.
'''



class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.health = 100
        self.age = 0

    def feed(self):
        if 0 < self.hunger:
            self.hunger -= 5
            self.health += 5
            print('yum yum yum!')
        elif self.hunger <= 0:
            print('Im not hungry >.<')

    def play(self):
            self.hunger += 5
            print('so much fun!!')
    
    def get_old(self):
        self.age += 1
        self.hunger += 10
        self.health -= 10

    def humor(self):
        if self.hunger > self.health:
            print('im not happy!, I am hungry')
        elif self.hunger <= self.health:
            print('I am happy')
    
    def display(self):
        print(f'Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}\nHealth: {self.health}')


srisumbhajee = Tamagotchi('srisumbhajee')
srisumbhajee.display()
srisumbhajee.get_old()
srisumbhajee.play()
srisumbhajee.feed()
srisumbhajee.get_old()
srisumbhajee.humor()
srisumbhajee.display()

