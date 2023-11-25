import random

# Start the game
print("Game started!")

# Ask the player to choose a move (r, p, s)
player = input("Choose your move, 'r' for rock, 'p' for paper, or 's' for scissors\n")

# Input validation
valid_moves = ['r', 'p', 's']
while player not in valid_moves:
    print("Invalid move. Please enter 'r', 'p', or 's'.")
    player = input("Choose your move, 'r' for rock, 'p' for paper, or 's' for scissors\n")

# PC makes a random move
pc = random.choice(valid_moves)

# Display player and PC moves
print(f"User played: {player}")
print(f"PC played: {pc}")

# Determine the winner
if player == pc:
    print("It's a tie!")
elif (player == 'r' and pc == 's') or (player == 'p' and pc == 'r') or (player == 's' and pc == 'p'):
    print("You won!")
else:
    print("You lost!")
