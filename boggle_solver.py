"""
Name: Jayson Kiggundu
SID: 003107096

Boggle Solver:
Implements a Boggle word search game solver.
"""

import re

class Boggle:
    def __init__(self, grid, dictionary):
        """Initialize the Boggle grid and dictionary."""
        self.grid = grid
        self.dictionary = set(word.lower() for word in dictionary)
        self.prefix_set = self.build_prefix_set(dictionary)
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0]) if self.grid else 0
        self.solutions = set()  # Store found words

    def build_prefix_set(self, dictionary):
        """Build a set of all valid prefixes from the dictionary."""
        prefix_set = set()
        for word in dictionary:
            for i in range(1, len(word) + 1):
                prefix_set.add(word[:i].lower())  # Add all prefixes
        return prefix_set

    def validate_grid(self, grid):
        """Validate that the grid is square and contains valid characters."""
        if not grid or len(grid) != len(grid[0]):
            return False
        regex = r'^(st|qu|[a-prt-z]+)$'
        for row in grid:
            for cell in row:
                if not re.match(regex, cell.lower()):  # Reject invalid cells
                    return False
        return True

    def setGrid(self, grid):
        """Set a new grid and update dimensions."""
        self.grid = grid
        self.num_rows = len(grid)
        self.num_cols = len(grid[0]) if grid else 0

    def setDictionary(self, dictionary):
        """Set a new dictionary and rebuild prefix set."""
        self.dictionary = set(word.lower() for word in dictionary)
        self.prefix_set = self.build_prefix_set(dictionary)

    def dfs(self, r, c, current_word, visited):
        """Perform DFS to explore possible words starting from a cell."""
        if r < 0 or c < 0 or r >= self.num_rows or c >= self.num_cols or visited[r][c]:
            return

        current_word += self.grid[r][c].lower()

        if current_word not in self.prefix_set:  # Stop if not a valid prefix
            return

        if len(current_word) >= 3 and current_word in self.dictionary:
            self.solutions.add(current_word)  # Add valid word

        visited[r][c] = True
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            self.dfs(r + dr, c + dc, current_word, visited)

        visited[r][c] = False  # Backtrack

    def find_solutions(self):
        """Find all valid words on the board using DFS search."""
        self.solutions.clear()
        visited = [[False] * self.num_cols for _ in range(self.num_rows)]
        for r in range(self.num_rows):
            for c in range(self.num_cols):
                self.dfs(r, c, "", visited)
        return list(self.solutions)

    def getSolution(self):
        """Return a sorted list of valid solutions in uppercase."""
        if not self.validate_grid(self.grid):
            return []
        solutions = self.find_solutions()
        return sorted([word.upper() for word in solutions])


def main():
    """Main function: create a Boggle instance and solve it."""
    grid = [["A", "B", "C", "D"],
            ["E", "F", "G", "H"], 
            ["I", "J", "K", "L"], 
            ["A", "B", "C", "D"]]

    dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())  # Print the game results


if __name__ == "__main__":
    main()