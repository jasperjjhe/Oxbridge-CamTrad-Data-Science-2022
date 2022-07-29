## Variables
number = 3
decimal_number = 3.5
some_text = "Hello!"

### Everything is Python is an object
type_number = type(number)
print(type_number, type(decimal_number), type(some_text))

### Arithmetics
res_sum = 2*(3 + 10.5 - 9.5) / 2 + .7
print("Result Sum:", res_sum, "Type Result Sum:", type(res_sum))

# Convert between types; type casting
# We must use the int, float, str
integer_res_sum = int(res_sum)
print("Converted Sum Type", type(integer_res_sum))
print("Converted to Integer Sum", integer_res_sum)

## Round numbers
rounded_res_sum = round(res_sum)
print("Rounded number", rounded_res_sum)

print("The number of the day is " + str(number))

## Format-strings
print(f"The Number of the days is {number}")

## Import the number of Pi
from math import pi
print(f"Pi number equals {pi}")

def get_area_circle(radius):
    return pi*radius**2

print("Area of the circle with radius 1 is", get_area_circle(1))

print("Area of the circle with radius 2 is:", get_area_circle(2))