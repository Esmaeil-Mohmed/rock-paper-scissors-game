# start the game
# ask the player to choose a move (r, p, s)
# pc makes a random move
# if player == pc => tie
# if player == r, pc == s or player == p, pc == r or if player == s, pc == p => player win!
# else => player lost!

import random

print("game statred!")

player = input("choose your move, 'r' for rock or 'p' for paper or 's' scissors\n")
pc = random.choice(['r', 'p', 's'])

print(f"user played: {player}")
print(f"pc played: {pc}")

if player == pc:
    print("It\'s tie")
elif (player == 'r' and pc == 's') or (player == 'p' and pc == 'r') or (player == 's' and pc == 'p'):
    print("you won!")
else:
    print("you lost!")
