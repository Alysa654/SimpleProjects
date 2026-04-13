import random

def roll_dice():
    result = random.randint(1,6)
    return result

def turn(countA, countB, total):
    if(countA == total or countB == total):
        return countA, countB
    
    a_result = roll_dice()
    b_result = roll_dice()

    if(a_result < b_result):
        countA -= 1
        countB += 1
        return countA, countB
    elif (b_result < a_result):
        countA += 1
        countB -= 1
        return countA, countB
    else:
        resultA, resultB = turn(countA, countB, total)
        if (resultA < resultB):
            countA -= 1
            countB += 1
        else:
            countA += 1
            countB -= 1

        return countA, countB


def main():
    print("Enter # of Dice")
    count = input()
    count = int(count)
    if (count % 2 == 0):
        player_a = count//2
        player_b = count//2
    else:
        player_a = count//2
        player_b = count//2 + 1
    print(player_a,player_b)

    turn_count = 0
    while (player_a != 0 and player_b != 0):
        turn_count += 1
        player_a, player_b = turn(player_a,player_b, count)
        print(f"Turn: {turn_count}    Player 1 count: {player_a}    Player 2 count: {player_b}")
    
    if (player_a == 0):
        print("Player 2 won!")
    else:
        print("Player 1 won!")


main()