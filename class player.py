class Player () :
    def __init__(self, name, age, rank):
        self.name = name
        self.age = age
        self.rank = rank
player1 = Player("messi", 36, 1)
player2 = Player("mbappe", 24, 2)
print("The player name is {}  he's {} and his rank is {}".format(player1.name,player1.age,player1.rank))
print("The player name is {}  he's {} and his rank is {}".format(player2.name,player2.age,player2.rank))