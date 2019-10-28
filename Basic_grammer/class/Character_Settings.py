
import random

class Chapter:

    def __init__(self):

        self.sex = random.randrange(0, 1)
        self.hp = random.randrange(10, 20)
        self.mp = random.randrange(20, 30)
        self.atk = random.randrange(1, 3)

    def attacked(self, atk):
        self.hp = self.hp - atk
        return self.hp

    def attack(self):
        return self.atk

chapter_a = Chapter()
chapter_b = Chapter()

print("a의 HP:", chapter_a.hp)
print("b의 HP:", chapter_b.hp)
print("-----")

turn = "user"

while(chapter_a.hp <= 0 or chapter_b.hp <= 0):

    choice = int(input())

    if(choice == 1):
        if(turn == "user"):
            chapter_b.attacked(chapter_a.attack())
            print("a의 HP:", chapter_a.hp)
            print("b의 HP:", chapter_b.hp)
            print("-----")

            turn = "com"

        if(turn == "com"):
            chapter_a.attacked(chapter_b.attack())
            print("a의 HP:", chapter_a.hp)
            print("b의 HP:", chapter_b.hp)

            turn = "user"