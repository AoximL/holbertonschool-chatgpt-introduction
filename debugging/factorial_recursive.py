#!/usr/bin/python3
import random
import os

def clear_screen():
    """
    Function Description:
        Clears the terminal screen to provide a fresh view of the game board.
        It checks the operating system to determine the correct command ('cls' for Windows, 'clear' for Unix/Linux).

    Parameters:
        None

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        """
        Function Description:
            Initializes the Minesweeper game instance. It sets the board dimensions,
            randomly places mines, initializes the revealed state grid, and calculates
            the winning condition (total safe cells).

        Parameters:
            width (int): The width of the game board (default 10).
            height (int): The height of the game board (default 10).
            mines (int): The total number of mines to place on the board (default 10).

        Returns:
            None
        """
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        # Total cells minus mines equals the number of cells we need to reveal to win
        self.safe_cells_count = (width * height) - len(self.mines)

    def print_board(self, reveal=False):
        """
        Function Description:
            Renders the current state of the game board to the console.
            It displays column/row numbers, hidden cells (.), revealed safe cells (count),
            and mines (*) if the game is over.

        Parameters:
            reveal (bool): A flag indicating if all cells (including mines) should be revealed.
                           Defaults to False. Used primarily when the game ends.

        Returns:
            None
        """
        clear_screen()
        print('  ' + ' '.join(f"{i}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y}", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        """
        Function Description:
            Calculates the number of mines present in the 8 neighboring cells surrounding
            a specific coordinate (x, y).

        Parameters:
            x (int): The x-coordinate (column) of the target cell.
            y (int): The y-coordinate (row) of the target cell.

        Returns:
            int: The count of mines in the adjacent cells.
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        """
        Function Description:
            Attempts to reveal a cell at the given coordinates.
            If the cell contains a mine, it returns False.
            If the cell is empty (0 adjacent mines), it recursively reveals neighboring cells.

        Parameters:
            x (int): The x-coordinate (column) to reveal.
            y (int): The y-coordinate (row) to reveal.

        Returns:
            bool: True if the move was safe or the cell was already revealed.
                  False if the player hit a mine.
        """
        # Boundary check to prevent IndexError
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True # Invalid move, but not a game over

        if self.revealed[y][x]:
            return True # Already revealed

        if (y * self.width + x) in self.mines:
            return False # Hit a mine

        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        """
        Function Description:
            Checks if the victory condition has been met.
            It compares the total number of currently revealed cells against
            the total number of safe (non-mine) cells on the board.

        Parameters:
            None

        Returns:
            bool: True if all safe cells are revealed (win), False otherwise.
        """
        # Count how many cells are currently revealed
        revealed_count = sum(row.count(True) for row in self.revealed)
        # If revealed cells equal total safe cells, the player wins
        return revealed_count == self.safe_cells_count

    def play(self):
        """
        Function Description:
            The main game loop. It handles user input for coordinates, validates the input,
            calls the reveal logic, updates the board, and checks for win/loss conditions
            after every turn.

        Parameters:
            None

        Returns:
            None
        """
        while True:
            self.print_board()
            try:
                x_input = input("Enter x coordinate: ")
                y_input = input("Enter y coordinate: ")
                
                # Check for empty input or exit command
                if not x_input or not y_input: 
                    print("Please enter valid coordinates.")
                    continue

                x = int(x_input)
                y = int(y_input)

                # Validate range before calling reveal
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordinates out of bounds. Please enter x: 0-{self.width-1}, y: 0-{self.height-1}")
                    input("Press Enter to continue...")
                    continue

                # Attempt to reveal
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\nBOOM! Game Over! You hit a mine.")
                    break
                
                # Check for win condition
                if self.check_win():
                    self.print_board(reveal=True)
                    print("\nCongratulations! You have cleared all mines!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
