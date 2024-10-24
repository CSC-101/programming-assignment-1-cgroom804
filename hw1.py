import math
import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(vowels: str) -> int: #the argument "vowels" is expected to be a string, and the function should output an integer
    vowel_list = ["a", "e", "i", "o", "u"] #vowels
    vowels = vowels.lower() #makes entire string lowercase
    return sum(1 for char in vowels if char in vowel_list) #returns the number of characters in the list

# Part 2
def short_list(lst: list[list[int]]) -> list[list[int]]: #the argument "lst" is expected to be a list with a list with an integer, and the function should output a list with a list with an integer
    return [nested_list for nested_list in lst if len(nested_list) == 2] # add the nested_list in lst if it is equal to 2

# Part 3
def ascending_pairs(lst: list[list[int]]) -> list[list[int]]: #the argument "lst" is expected to be a list with a list with an integer, and the function should output a list with a list with an integer
    return [sorted(nested_list) if len(nested_list) == 2 else nested_list for nested_list in lst] #add the sorted nested_list in lst if it is equal to 2, otherwise add the nested_list as is

# Part 4
def add_prices(num1: data.Price, num2: data.Price): #The arguments num1 and num2 are expected to be an instance of the class Price from the data file
    cents = num1.cents + num2.cents #Adds total number of cents
    dollars = num1.dollars + num2.dollars + cents // 100 #calculates number of dollars with cents
    cents %= 100 # finds the remaining number of cents
    return data.Price(dollars, cents) # return the price using the Price class from file data

# Part 5
def rectangle_area(rectangle: data.Rectangle) -> float: # the argument rectangle is expected to be an instance of the class Rectangle from the data file
    width = rectangle.bottom_right.x - rectangle.top_left.x # Calculates the distance between the points' x co-ordinates
    height = rectangle.top_left.y - rectangle.bottom_right.y # Calculates the distance between the points' y co-ordinates
    return abs(width * height) # Returns the absolute value for the area of the square incase the points are swapped

# Part 6
def books_by_author(auth: str, books: list[data.Book]) -> list[data.Book]: # the arguments auth and books are expected to be a string and list with the instance Book respectively, and the function should output list with the instance Book
    return [book for book in books if auth in book.authors] # returns a list of books with the same author

# Part 7
def circle_bound(rectangle: data.Rectangle) -> data.Circle: #the argument rectangle is expected to be an instance of the class Rectangle from the data file, and the function is expected to output an Circle instance
    center_x = (rectangle.top_left.x + rectangle.bottom_right.x) / 2
    center_y = (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    radius = math.sqrt((rectangle.bottom_right.x - center_x) ** 2 + (rectangle.bottom_right.y - center_y) ** 2)
    return data.Circle(data.Point(center_x, center_y), radius)

# Part 8
def below_pay_average(pay_list: list[data.Employee]) -> list[str]: # the argument pay_list is expected to be a list consisting of instances of the class Employee, and the function will output a list of strings
    if len(pay_list) == 0: # return a blank list if there are no employees
        return []
    avg_pay = sum(employee.pay_rate for employee in pay_list)/len(pay_list) # adds together all the employees' pay and divides it by the total number of employees to find the average pay
    return [employee.name for employee in pay_list if employee.pay_rate < avg_pay] # returns the names of employees being paid below the average