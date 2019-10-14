# 1 Function Basics

###Challenge Activity 1###
    # print_pattern() prints 5 characters. Call print_pattern() twice to print
    # 10 characters. Example output:
    #*****
    #*****

def print_pattern():
   print('*****')

print_pattern()
print_pattern()

###Challenge Activity 2###
    # Define print_shape() to print the below shape. Example output:
    # ***
    # ***
    # ***

def print_shape():
   print('***')
   print('***')
   print('***')

print_shape()


# 2 Parameters

###Challenge Activity 1###

    # Complete the function definition to output the hours given minutes.

    # Sample output with input: 210.0
    # 3.5

def output_minutes_as_hours(orig_minutes):
    print(str(orig_minutes) + ' minutes is ' + str(orig_minutes / 60) + \
          ' hours.')

minutes = float(input('Enter minutes: '))
output_minutes_as_hours(minutes)

###Challenge Activity 2###

    # Define a function print_total_inches, with parameters num_feet and
    # num_inches, that prints the total number of inches.
    # Note: There are 12 inches in a foot.

    # Sample output with inputs: 5 8
    # Total inches: 68


def print_total_inches(num_feet, num_inches):
    total_inches = (num_feet * 12) + num_inches
    print('Total inches: ' + str(total_inches))

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))
print_total_inches(feet, inches)


# 3 Return

###Challenge Activity 1###

    # Complete the program by writing and calling a function that converts a
    # temperature from Celsius into Fahrenheit.
    # Use the formula F = C x 9/5 + 32. Test your program knowing that 50
    # Celsius
    # is 122 Fahrenheit.

def c_to_f(celsius):
    """Converts celsius to fahrenheit"""
    f = celsius * 9/5 + 32
    return  f

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None


temp_f = c_to_f(temp_c)


print('Fahrenheit:' , temp_f)

###Challenge Activity 2###

    # Assign max_sum with the greater of num_a and num_b, PLUS the greater of
    # num_y and num_z. Use just one statement.
    # Hint: Call find_max() twice in an expression.

    # Sample output with inputs: 5.0 10.0 3.0 7.0
    # max_sum is: 17.0

def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input('Enter first number: '))
num_b = float(input('Enter second number: '))
num_y = float(input('Enter third number: '))
num_z = float(input('Enter fourth number: '))

max_sum = float(find_max(num_a, num_b) + find_max(num_y, num_z))

print('max_sum is:', max_sum)

###Challenge Activity 3 - Volume of a Pyramid###

    # Define a function pyramid_volume with parameters base_length, base_width,
    # and pyramid_height, that returns the volume of a pyramid with a
    # rectangular base.

    # Sample output with inputs: 4.5 2.1 3.0
    # Volume for 4.5, 2.1, 3.0 is: 9.45
    # Relevant geometry equations:
    # Volume = base area x height x 1/3
    # Base area = base length x base width.

def pyramid_volume(base_length, base_width, pyramid_height):
    vol = base_length * base_width * pyramid_height * 1/3
    return vol

length = float(input('Enter 4.5 for length: '))
width = float(input('Enter 2.1 for width: '))
height = float(input('Enter 3.0 for height: '))
volume = round(pyramid_volume(length, width, height), 2)
print('Volume for 4.5, 2.1, 3.0 is:', volume)


# 4 Dynamic

def add(x, y):
    return x + y
	
print('add(7, 7) is', add(7, 7))
print("add('light', 'house') is", add('light', 'house'))


# 5 Why functions

# ###Challenge Activity 1###

# #Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles().
# #Original main program:

# miles_per_hour = float(input())
# minutes_traveled = float(input())
# hours_traveled = minutes_traveled / 60.0
# miles_traveled = hours_traveled * miles_per_hour

# print('Miles: %f' % miles_traveled)

#Sample output with inputs: 70.0 100.0
#Miles: 116.666667

def mph_and_minutes_to_miles(mph, minutes):
    hours_traveled = minutes / 60.0
    miles_traveled = hours_traveled * mph
    return miles_traveled

miles_per_hour = float(input('Enter mph: '))
minutes_traveled = float(input('Enter minutes travled: '))

print('Miles: %f' % mph_and_minutes_to_miles(miles_per_hour, minutes_traveled))
