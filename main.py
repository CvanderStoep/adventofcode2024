from sympy import symbols, Eq, solve

# Define the symbols
A, B = symbols('A B')

# Define the equations
eq1 = Eq(26*A + 67*B, 10000000012748)
eq2 = Eq(66*A + 21*B, 10000000012176)

# Solve the system of equations
solution = solve((eq1, eq2), (A, B))

# Extract the solutions
A_value = solution[A]
B_value = solution[B]

print(solution)

# Check if the solutions are integers
if A_value.is_integer and B_value.is_integer:
    print(f'Integer Solutions: A = {int(A_value)}, B = {int(B_value)}')
else:
    print('No integer solutions found.')
