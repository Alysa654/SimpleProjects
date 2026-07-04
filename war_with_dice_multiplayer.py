import random


class Player():
    def __init__(self, num, name):
        self.dice_count = num
        self.name = name
        pass

    def set_dice(self, num):
        self.dice_count = num
    def get_dice(self):
        return self.dice_count
    def increment_dice(self, num):
        self.dice_count += num
    def get_name(self):
        return self.name
    
    def __str__(self):
        return f"{self.name} has {self.dice_count} dice"
    def __repr__(self):
        return f"{self.name} has {self.dice_count} dice"
    def __eq__(self, other):
        return (self.dice_count, self.name) == (other.dice_count, other.name)
    def __hash__(self):
        return hash(self.name)








#rolls the dice per person
def roll_dice():
    result = random.randint(1,6)
    return result

def get_winners(dice_results: list[int], player_list : list[Player]):
    winners = []
    try:
        winning_value = max(dice_results)
    except ValueError:
        print("players", player_list)
        print("dice results",dice_results)
    for i in range(len(dice_results)):
        if dice_results[i] == winning_value:
            winners.append(i)
    return winners

def turn_helper(player_list : list[Player], total:int, losers : list[Player], winning_pool):
    # print(player_list[0])
    for index in range(len(player_list)):
        if player_list[index].get_dice() >= total:
            winner = player_list.pop(index)
            return winner, player_list
    dice_results = [roll_dice() for _ in range(len(player_list))]
    winners_list = get_winners(dice_results, player_list)
    winning_pool = winning_pool + len(player_list)

    if(len(winners_list) <= 1):
        winning_player = []
        for i in range(len(player_list)):
            player_list[i].increment_dice(-1)
        winning_player = player_list.pop(winners_list[0])
        winning_player.increment_dice(winning_pool)
        return winning_player, player_list
    else:
        wining_players = []
        for i in range(len(player_list)):
            player_list[i].increment_dice(-1)
        for index in winners_list:
            wining_players.append(player_list[index])
            pass
        winner, loser_list = turn_helper(wining_players, total, losers, winning_pool)
        loser_list = list(set(loser_list))
        return winner, loser_list

# logic for an individual turn in game
def turn(player_list : list[Player], total:int):
    winner, list_of_players = turn_helper(player_list, total, [], 0)
    list_of_players.append(winner)
    return list_of_players


def get_dice_count():
    while True:
        count = input("Enter # of Dice: ")
        try:
            count = int(count)
            return count
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_player_count():
    while True:
        count = input("Enter # of Players: ")
        try:
            count = int(count)
            return count
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# runs the program
def main():

    count = get_dice_count()
    num_players = get_player_count()

    if(num_players == 1):
        print("You cannot play by yourself")
        return None
    else:
        names = [input("Enter Name: ") for _ in range(num_players)]


    list_of_players = [Player(0, names[i]) for i in range(num_players)]

    # divides total count of dice evenly.
    for i in range(num_players):
        list_of_players[i].set_dice(count//num_players)
    remainder = count % num_players
    index = 0
    while remainder != 0:
        list_of_players[index].increment_dice(1)
        remainder -=1
        index +=1

    # print("Line 116: ", list_of_players)

    # displays turn number as well as who has what dice on the table. 
    turn_count = 0
    game_over = False
    while (not game_over):
        # logic for ending the game
        list_of_players = list(set(list_of_players))
        for player in list_of_players:
            if player.get_dice() >= count:
                game_over = True
        # if len(list_of_players) >= 4:
        #     game_over = True
        #     print("length went over")
        turn_count += 1
        list_of_players = turn(list_of_players, count)
        print(f"Turn: {turn_count} " + str(list_of_players))
    
    #reveals who won
    for player in list_of_players:
        if player.get_dice() == count:
            print(player.get_name() + " won!")

# get_winners([],[])
random.seed(5)
# print(Player(1,"Furcorn"))
main()