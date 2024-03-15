import random

def print_board(heap):
    # Function to print the current state of the heap
    print(f"Current heap: {'|' * heap}")

def get_user_move(heap):
    # Function to get the user's move
    while True:
        try:
            sticks_to_remove = int(input(f"Enter the number of sticks to remove: (minimum 1, maximum {min(heap, heap // 2)}) "))
            if 1 <= sticks_to_remove <= min(heap, heap // 2):
                break
            else:
                print(f"Invalid number. Please enter a number between 1 and {min(heap, heap // 2)}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return sticks_to_remove

def get_computer_move(heap):
    # Function to get the computer's move
    xor_sum = heap
    for i in range(heap):
        xor_sum ^= i
    
    # If the XOR sum is 0, make a random move
    if xor_sum == 0:
        max_sticks = min(heap, heap // 2)
        sticks_to_remove = random.randint(1, max_sticks)
    else:
        max_sticks = min(heap // 2, heap)
        sticks_to_remove = max(1, min(max_sticks, heap - xor_sum))
    return sticks_to_remove

def nim_game():
    # Function to play the Nim game
    heap = 16  # Initial number of sticks in the heap
    player_turn = 1  # Player 1 starts the game
    
    # Continue the game until there's only one stick left
    while heap > 1:
        print_board(heap)  # Print the current state of the heap
        player_name = "Player 1" if player_turn == 1 else "Computer"
        
        # Get the move based on the player's turn
        if player_turn == 1:
            sticks_to_remove = get_user_move(heap)
        else:
            sticks_to_remove = get_computer_move(heap)
        
        heap -= sticks_to_remove  # Update the heap after the move
        print(f"{player_name} removes {sticks_to_remove} sticks")
        player_turn = 3 - player_turn  # Switch player turn
        
    print_board(heap)  # Print the final state of the heap
    winner = "Player 1" if player_turn == 2 else "Computer"
    print(f"Player {player_turn} picks the last stick")
    print(f"{winner} wins!")

if __name__ == "__main__":
    nim_game()
