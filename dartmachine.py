#!/usr/bin/python3

import random
from time import sleep

"""
Count the scores of darts
"""

class Game:
    """
    takes the score of the player and count down the score till 0
    """

    def turn(score):
        """
        count scores of darts during one turn
        """
        s,c = 0,0
        for d in range(1,4):
            #sleep(.1)
            print(score-s)
            ui = input(f"Enter score of dart {d}: ").lower().strip()
            #ui = random.randint(1,60)
            if ui == 'q': break
            try:
                s += int(ui)
                c += 1
                if s > score: 
                    print("Too much...")
                    return score
                elif score - s == 1:
                    print("Foul!")
                    return score
                elif score == s:
                    return 0
                else: pass
            except: pass
        return score - s

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
