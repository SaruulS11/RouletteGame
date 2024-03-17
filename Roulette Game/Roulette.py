import random
from Player import Player
from Revolver import Revolver
player_health = 1
revolver = [0, 0, 0, 0, 0, 0]
bullet_slot = random.randint(0 , 5)
revolver[bullet_slot] = 1
player1_turn = random.choice([True, False])
player2_turn = not player1_turn
print("Enter your name first player: ")
player1 = Player("Burnee", player_health, player1_turn)
print("Enter your name second player: ")
player2 = Player("Bek", player_health, player2_turn)
gun = Revolver(revolver)

print("GAME STARTED")
show_case = ['b', 'b', 'b', 'b', 'b', 'b']
while player1.health > 0 and player2.health > 0:
    print("Remaining bullets ",show_case)
    print(revolver)
    show_case.pop()
    if player1_turn:
        print(f"{player1.name}'s turn Shoot yourself or your opponent! Y: yourself O: opponent")
        choice = input()
        player1_turn = False
        player2_turn = True
        if choice == "y":
            gun.shoot(player1)
        else:
            gun.shoot(player2)
    else:
        print(f"{player2.name}'s turn Shoot yourself or your opponent! Y: yourself O: opponent")
        choice = input()
        player2_turn = False
        player1_turn = True
        if choice == "y":
            gun.shoot(player2)
        else:
            gun.shoot(player1)
    
    









# #Ээлж ээлжээр буудах тест
# while player1.health > 0 and player2.health > 0:
#     if player1.turn:
#         gun.shoot(player1)
#         player1.turn = False
#         player2.turn = True
#     else:
#         gun.shoot(player2)
#         player1.turn = True
#         player2.turn = False