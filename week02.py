import math

# Question 1:

def greet(name):
    return f"Hello {name}. How are you?"
    print(greet("Alex"))

# Question 2:

my_friends = ["Nicole","Aryn","Obi"]

def greet_friends(my_friends):
    for friend in my_friends:
        print(greet(friend))
        
greet_friends(my_friends)

# Question 3:

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("No real solutions")
    else:
        x1 = (-b - math.sqrt(discriminant)) / (2*a)
        x2 = (-b + math.sqrt(discriminant)) / (2*a)
        print(f"The solutions are: x1 = {x1}, x2 = {x2}")

solve_quadratic(1,-3,2)
solve_quadratic(1,2,5)
