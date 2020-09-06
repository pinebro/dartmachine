#!/usr/bin/python3

"""
Count the scores of darts
"""

class Game:
    """
    takes the score of the player and count down the score till 0
    """

    def turn(target):
        """
        count scores of darts during one turn
        """
        score = 0
        for d in range(1,4):
            print(target-s)
            ui = input(f"Enter score of dart {d}: ").lower().strip()
            if ui == 'q': break
            try:
                score += int(ui)
                c += 1
                if score > target: 
                    print("Too much...")
                    return target
                elif target - score == 1:
                    print("Foul!")
                    return target
                elif target == score:
                    return 0
                else: pass
            except: pass
        return sum(target, -abs(score))

    def gameloop(players):
        """
        loop the turn-function till score equals 0
        """
        while True:
            for p in players:
                print(f"{p.name} ", end='')
                p.score = Game.turn(p.score)
                print(p.score)
                if p.score == 0:
                    print(f"Game finished!\nThe winner is {p.name}!")
                    return 0

class Player:
    """
    creates players
    """

    players = []

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Player.players.append(self)
        pass

Player1 = Player('Foo', 501)
Player2 = Player('Bar', 501)

if __name__ == '__main__':

    def testing():
        for i in Player.players:
            i.score = 501
        Game.gameloop(Player.players)

    testing()
