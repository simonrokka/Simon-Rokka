#6
import random
num_points = int(input("Enter the number of random points to generate: "))
points_inside_circle = 0
for _ in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        points_inside_circle += 1
pi_approx = 4 * points_inside_circle / num_points
print(f"Approximation of pi using {num_points} random points: {pi_approx}")