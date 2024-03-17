import pygame, sys
import random
from button import Button

pygame.init()

# Player class
class Player:
    def __init__(self, name, health, turn):
        self.name = name
        self.health = health
        self.turn = turn

# Revolver class
class Revolver:
    def __init__(self, revolver):
        self.revolver = revolver

    def shoot(self, player):
        bullet_slot = random.randint(0, 5)
        if self.revolver[bullet_slot] == 1:
            while True:
                PLAY_MOUSE_POS = pygame.mouse.get_pos()

                SCREEN.fill("black")

                PLAY_TEXT = get_font(45).render(player.name + " is dead!", True, "White")
                PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
                SCREEN.blit(PLAY_TEXT, PLAY_RECT)

                PLAY_AGAIN = Button(image=None, pos=(640, 460), 
                text_input="PLAY AGAIN", font=get_font(75), base_color="White", hovering_color="Green")

                PLAY_AGAIN.changeColor(PLAY_MOUSE_POS)
                PLAY_AGAIN.update(SCREEN)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_AGAIN.checkForInput(PLAY_MOUSE_POS):
                            main_menu()

                pygame.display.update()
        else:
            print(f"Click! {player.name} survived. 😅")

player_health = 1
player1_turn = random.choice([True, False])
player2_turn = not player1_turn
player1 = Player("Burnee", player_health, player1_turn)
player2 = Player("Beck", player_health, player2_turn)
revolver = [0, 0, 0, 0, 0, 0]
bullet_slot = random.randint(0, 5)
revolver[bullet_slot] = 1
gun = Revolver(revolver)

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Roulette Game/assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Roulette Game/assets/font.ttf", size)

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAYER1_NAME = get_font(50).render(player1.name, True, "#b68f40")
        P1_RECT = PLAYER1_NAME.get_rect(center=(640, 100))
        PLAYER2_NAME = get_font(50).render(player2.name, True, "#b68f40")
        P2_RECT = PLAYER2_NAME.get_rect(center=(640, 500))
        BULLETS = get_font(20).render(str(revolver), True, "#b68f40")
        BULLET_REVEAL = BULLETS.get_rect(center=(1100, 360))

        PLAY_BUTTON = Button(image=pygame.image.load("Roulette Game/assets/Play Rect.png"), pos=(400, 650), 
                            text_input="YOURSELF", font=get_font(40), base_color="#d7fcd4", hovering_color="Red")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Roulette Game/assets/Play Rect.png"), pos=(880, 650), 
                            text_input="OPPONENT", font=get_font(40), base_color="#d7fcd4", hovering_color="Red")
        QUIT_BUTTON = Button(image=pygame.image.load("Roulette Game/assets/Quit Rect.png"), pos=(100, 100), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(PLAYER1_NAME, P1_RECT)
        SCREEN.blit(PLAYER2_NAME, P2_RECT)
        SCREEN.blit(BULLETS, BULLET_REVEAL)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    gun.shoot(player1)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()