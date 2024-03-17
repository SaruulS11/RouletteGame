class Revolver:
    def __init__(self, revolver):
        self.revolver = revolver

    def shoot(self, player):
        if self.revolver:
            self.revolver.pop()
            if 1 in self.revolver:
                print(f"{player.name} is ALIVE")
            else:
                player.health -= 1
                print(f"{player.name} You are dead GG {player.health}")
        else:
            print("No bullets left in the revolver.")