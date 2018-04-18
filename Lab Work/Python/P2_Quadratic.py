import cmath
print('Solve the quadratic equation:')
a = float(input('Please enter a : '))
b = float(input('Please enter b : '))
c = float(input('Please enter c : '))
dell = (b**2) - (4*a*c)
sol_1 = (-b-cmath.sqrt(dell))/(2*a)
sol_2 = (-b+cmath.sqrt(dell))/(2*a)

print('The solutions are {0} and {1}'.format(sol_1,sol_2))