# Function to check and print if the given sides of a triangle are of a right angled triangle.
def right_angled_triangle_check(a, b, c):
    x = min(a,b,c)
    z = max(a,b,c)
    y = (a+b+c) - (x+z)
    if z**2 == x**2 + y**2:
        print("Right angled triangle")
    else:
        print("Not a right angled triangle")


# Function to find radius of a circle given the circumference.
def find_radius_from_cicumference(circumference):
    return circumference/(2*3.14)


# Function to find radius of circle given area of the circle.
def find_radius_from_area(area):
    return (area/3.14)**0.5


# Program to central angle given the radius and arc length
arc_length = 22
radius = 7
central_angle = arc_length/radius
print("Central angle :", central_angle)


# Function to print the area of the maximum possible square inside a circle of given radius
def find_area_of_square(radius):
    print("Area of maximum possible square: ", (2 * radius**2))


# Function to calculate the perimeter of an equilateral triangle given one side.
def perimeter_equilateral_triangle(side):
    return 3*side


# Function to calculate area of an equilateral triangle given one side.
def area_equilateral_triangle(side):
    return (3**0.5 * side**2)/4


# Program to calculate and print area of square given one side of the square
square_side_length = 10
area_of_square = square_side_length * square_side_length
print(f'Area of the square= {area_of_square}')


# Program to calculate and print area of rectangle given 2 adjacent sides of the rectangle
side_a = 5
side_b = 10
area_of_rectangle = side_a * side_b
print(f'Area of the rectangle = {area_of_rectangle}') 


# Program to calculate and print perimeter of square given one side of the square
square_side_length = 10
perimeter_of_square = square_side_length * 4
print(f'Perimeter of the square= {perimeter_of_square}')


# Program to calculate and print perimeter of rectangle given 2 adjacent sides of the rectangle
side_a = 5
side_b = 10
perimeter_of_rectangle = 2 * (side_a + side_b)
print(f'Perimeter of the rectangle = {perimeter_of_rectangle}') 


# Program to print the perimeter of a triangle given 3 sides of the triangle
side_a = 3
side_b = 4
side_c = 5
perimeter_of_triangle = side_a + side_b + side_c
print(f'Perimeter of the triangle = {perimeter_of_triangle}')


# Function to find area of the biggest circle that can be drawn inside a square given the length of the square's side.
def big_circle_area(side):
    return ((22/7) * (side/2)**2)


# Function to find if two lines are parallel given their slopes.
def line_parallel_check(m1, m2):
    if m1 == m2:
        return "Lines are parallel"
    else:
        return "Lines are not parallel"


# Function to find if two lines are perpendicular given their slopes.
def line_perpendicular_check(m1, m2):
    if m1 * m2 == -1:
        return "Lines are perpendicular"
    else:
        return "Lines are not perpendicular"


# Calculate simple interest for given principle amount, rate and time
principal_amount = 10000
rate = 10
time = 5
simple_interest = (principal_amount * time * rate)/100


# Function to calculate standard deviation of a list of numbers
def calculate_standard_deviation(test_list):
    mean = sum(test_list) / len(test_list) 
    variance = sum([((x - mean) ** 2) for x in test_list]) / len(test_list) 
    res = variance ** 0.5
    return res

# Function to calculate mean of a list of numbers
def calculate_mean(test_list):
    mean = sum(test_list) / len(test_list)
    return mean


# Function to calculate number of minutes in duration given in seconds
def calculate_mins(duration):
    minutes = duration // 60
    seconds = duration - (60 * minutes)
    return minutes, seconds


# Function to calculate number of rupees in given amount in paise
def calculate_rupees(amount):
    rupees = amount // 100
    paise = amount - (100 * rupees)
    return rupees, paise


# Function to calculate your weight in moon
def weight_in_moon(weight):
    return weight * 0.165


# Function to find if a number is a Fibonacci number or not.
import math
def find_fibo_2(n):
    return math.sqrt(5*n**2+4).is_integer() or math.sqrt(5*n**2-4).is_integer()


# Program to strip vowels from a string
vowel_stripper = [x for x in filter(lambda x: x not in ['a','e','i','o','u'],'veritaserum')]


# Program to add every 3rd number in the list.
from functools import reduce
num_list = [x for x in range(1,20)]
sum_every_3 = reduce(lambda x,y : x+y, [num_list[i] for i in range(len(num_list)) if (i+1)%3==0])


# Function to generate a number between 1 and 6 like a dice.
import random
def roll_dice():
    return random.randint(1,6)


# Function to find if a number is divisible by 3.
def divisibility_by_3(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number//10
    return True if sum % 3 == 0 else False


# Function to find if a number is divisible by 4
def divisibility_by_4(number):
    last_two_digits = number % 100
    return True if last_two_digits % 4 == 0 else False


# Function to find if the given number is divisible by 5
def divisibility_by_5(number):
    last_digit = number % 10
    return True if last_digit in (0,5) else False


# Function to find if the given number is divisible by 9
def divisibility_by_9(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number//10
    return True if sum % 9 == 0 else False


# Function to find if the number is divisible by 10
def divisibility_by_10(number):
    last_digit = number % 10
    return True if last_digit == 0 else False


# Function to find squares of a list of integers.
def square_of_list(a):
    square_list = []
    for i in a:
        square_list.append(i**2)
    return square_list


# Function to find the cube of a list of integers.
def cube_of_list(a):
    cube_list = []
    for i in a:
        cube_list.append(i**3)
    return cube_list


# Program to print the reverse of a list.
a_list = [1,2,3,'and','the']
print(f'Reverse of the list is {a_list[::-1]}')


# Function to convert a list to a string
def convert_list_to_string(list_b):
    return ' '.join([word for word in list_b])


# Function to convert a string to a list
def convert_string_to_list(string_sequence):
    list_c =string_sequence.split()
    return list_c


# function to return the characters of a string.
def string_to_char(string_sequence):
    char_list = list(string_sequence)
    return char_list


# Program to swap two variables without temporary variable
x = 'guten'
y = 'morgen'
x, y = y, x
print('New value of x', x)
print('New value of y', y)


# Function to count the occurence of each vowel in a word.
def count_vowels(word):
    vowel_dict = {}.fromkeys(['a', 'e', 'i', 'o', 'u'], 0)
    for char in word:
        if char in vowel_dict:
            vowel_dict[char] += 1
    return vowel_dict


# Program to find if string is a palindrome
string_sequence = 'rorberto'
rev_sequence = reversed(string_sequence)

if list(string_sequence) == list(rev_sequence):
    print(f"{string_sequence} is a palindrome")
else:
    print("Its not a palindrome")


# Function to find the sum of numbers at even indices and odd indices.
def sum_odd_even_indices(sequence):
    odd_indice_sum = 0
    even_indice_sum = 0
    for i in range(len(sequence)):
        if i%2 == 0:
            even_indice_sum += sequence[i]
        else:
            odd_indice_sum += sequence[i]
    return odd_indice_sum, even_indice_sum


# Function to raise the power of a number by any exponent
def number_exponent(number, exponent):
    return number ** exponent


# Function to strip the first and the last character in a string.
def strip_first_last(sequence):
    return seq[1:-1]


# Function to print the number of occurences of a substring within a string
def substring_occurence_count(sequence, substring):
    print(sequence.count(substring))


# Function to replace a string within another string once in a sentence and print result.
def replace_substring_string(sequence, substring1, substring2):
    print(sequence.replace(substring1, substring2,1))


# Function to find the indices where a given character is present in a string.
def find_indice_char(sequence, ch):
    indice_location = []
    for i in range(len(sequence)):
        if sequence[i] == ch:
            indice_location.append(i)
    return indice_location


# Function to get a substring from a string based on the slice indices.
def get_substring_from_slice(sequence, start_index, end_index):
    return sequence[start_index: end_index]


# Function to invert a boolean value
def boolean_invert(boolean_value):
    return not boolean_value


# Function to find the factorial of a number
def number_factorial(number):
    factorial = 1
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        for i in range(1, number+1):
            factorial = i*factorial
    return factorial


# Function to remove punctuations from a sentence
def remove_punctuation(sequence):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in sequence:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


# Function to repeat a sequence n number of times.
def repeat_sequence(sequence, repeat_number):
    return sequence*repeat_number


# Function to write the numbers in words
def numbers_in_words(number):
    numbers_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = [int(x) for x in str(number)]
    words = [numbers_words[digit] for digit in digits]
    return " ".join(n for n in words)


# Function to write digits of numbers written in words
def words_to_numbers(words):
    numbers_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = []
    words = list(words.split())
    for i in range(len(words)):
        numbers.append(numbers_words.index(words[i]))
    return numbers



