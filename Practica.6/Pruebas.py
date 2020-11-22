problema1 = Problem()
problema1.addVariables(["A", "B", "C"], [1, 2, 3])
problema1.addConstraint(AllDifferentConstraint())
problema1.addConstraint(ExactSumConstraint(6))
x = problema1.getSolutions()
print(x)


problema = Problem()
problema.addVariables(range(0, 9), range(1, 9 + 1))
problema.addConstraint(AllDifferentConstraint(), range(0, 9))
problema.addConstraint(ExactSumConstraint(15), [0, 4, 8])
problema.addConstraint(ExactSumConstraint(15), [2, 4, 6])

for row in range(3):
    print(row)
    problema.addConstraint(ExactSumConstraint(15),
                              [row * 3 + i for i in range(3)])

for col in range(3):
    print(col)
    problema.addConstraint(ExactSumConstraint(15),
                              [col + 3 * i for i in range(3)])

solutions = problema.getSolution()
print(solutions)
