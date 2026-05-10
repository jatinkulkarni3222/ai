class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

        # Sets for Branch and Bound
        self.cols = set()
        self.diag1 = set()   # row - col
        self.diag2 = set()   # row + col

    def solve(self, row=0, board=None):

        if board is None:
            board = []

        # All queens placed successfully
        if row == self.n:
            self.solutions.append(board[:])
            return

        # Try placing queen in each column
        for col in range(self.n):

            # Check if position is safe
            if (col in self.cols or
                (row - col) in self.diag1 or
                (row + col) in self.diag2):
                continue

            # Place queen
            self.cols.add(col)
            self.diag1.add(row - col)
            self.diag2.add(row + col)
            board.append(col)

            # Recursive call
            self.solve(row + 1, board)

            # Backtracking
            board.pop()
            self.cols.remove(col)
            self.diag1.remove(row - col)
            self.diag2.remove(row + col)

    def print_board(self, solution):

        for r in range(self.n):
            for c in range(self.n):
                if solution[r] == c:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()


# Take input from user
n = int(input("Enter value of N: "))

# Create object
solver = NQueens(n)

# Solve the problem
solver.solve()

# Print total solutions
print(f"\nTotal solutions for {n}-Queens: {len(solver.solutions)}")

# Print first solution
if solver.solutions:
    print("\nFirst Solution:\n")
    solver.print_board(solver.solutions[0])
else:
    print("No solution exists.")

