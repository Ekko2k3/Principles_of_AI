import random

class Crossword:
    def __init__(self, height, width):
        # Initialize the crossword grid with specified height and width
        self.height = height
        self.width = width
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]  # Create an empty grid
        self.words = []  # Initialize an empty list to store words

    def add_word(self, word):
        # Method to add a word to the crossword
        word = word.upper()  # Convert word to uppercase
        # Check if the word is too long to fit in the grid
        if len(word) > max(self.height, self.width):
            print(f"Word '{word}' is too long to fit in the grid.")
            return
        
        # Add the word to the list of words
        self.words.append(word)
        placed = False
        
        # Keep trying until the word is successfully placed in the crossword
        while not placed:
            direction = random.choice(['across', 'down'])  # Randomly choose a direction (across or down)
            if direction == 'across':
                # Randomly select starting position for an across word
                x = random.randint(0, self.width - len(word))
                y = random.randint(0, self.height - 1)
                # Check if the word fits in the chosen position
                if self.check_fit(word, x, y, 1, 0):
                    # If it fits, place the word in the crossword
                    self.place_word(word, x, y, 1, 0)
                    placed = True
            else:
                # Randomly select starting position for a down word
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - len(word))
                # Check if the word fits in the chosen position
                if self.check_fit(word, x, y, 0, 1):
                    # If it fits, place the word in the crossword
                    self.place_word(word, x, y, 0, 1)
                    placed = True

    def check_fit(self, word, x, y, dx, dy):
        # Method to check if a word fits in a given position and direction
        for i in range(len(word)):
            # Check if the current cell is empty or contains the same letter as the word
            if self.grid[y][x] not in [' ', word[i]]:
                return False
            x += dx  # Move to the next cell in the specified direction
            y += dy
        return True

    def place_word(self, word, x, y, dx, dy):
        # Method to place a word in the crossword grid
        for i in range(len(word)):
            # Place each letter of the word in the corresponding cell
            self.grid[y][x] = word[i]
            x += dx  # Move to the next cell in the specified direction
            y += dy

    def display(self):
        # Method to display the crossword grid
        for row in self.grid:
            print(' '.join(row))  # Print each row of the grid with spaces between cells


def main():
    # Create a crossword puzzle and add words to it
    crossword = Crossword(12, 12)  # Create a 12x12 crossword grid
    words = ["PYTHON", "ALGORITHM", "PROGRAMMING", "COMPUTER", "LANGUAGE"]  # List of words to add
    for word in words:
        crossword.add_word(word)  # Add each word to the crossword puzzle
    crossword.display()  # Display the completed crossword puzzle

if __name__ == "__main__":
    main()
