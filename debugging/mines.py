#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        # Total cells minus mines equals the number of cells we need to reveal to win
        self.safe_cells_count = (width * height) - len(self.mines)

    def print_board(self, reveal=False):
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
        # Count how many cells are currently revealed
        revealed_count = sum(row.count(True) for row in self.revealed)
        # If revealed cells equal total safe cells, the player wins
        return revealed_count == self.safe_cells_count

    def play(self):
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
