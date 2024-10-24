import math

import data
import hw1
from hw1 import vowel_count, short_list, ascending_pairs, add_prices, rectangle_area, books_by_author, circle_bound, \
    below_pay_average
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1

    def test_vowel_count1(self):
        quote = "How many vowels are in this quote?"
        result = hw1.vowel_count(quote)
        expected = 11
        self.assertEqual(result,expected)

    def test_vowel_count2(self):
        quote = "What about this quote?"
        result = vowel_count(quote)
        expected = 8
        self.assertEqual(result, expected)

    # Part 2
    def test_short_list1(self):
        test = [[1, 2], [3, 4, 5], [5, 6]]
        result = short_list(test)
        expected = [[1, 2], [5, 6]]
        self.assertEqual(result, expected)

    def test_short_list2(self):
        test = [[7], [8, 9, 10], [11, 12]]
        result = short_list(test)
        expected = [[11,12]]
        self.assertEqual(result, expected)

    # Part 3
    def test_ascending_pairs1(self):
        test = [[7, 6], [5, 4, 3], [2, 1]]
        result = ascending_pairs(test)
        expected = [[6,7], [5, 4, 3], [1, 2]]
        self.assertEqual(result, expected)

    def test_ascending_pairs2(self):
        test = [[5,2,8], [8, 4], [9, 2]]
        result = ascending_pairs(test)
        expected = [[5,2,8], [4, 8], [2, 9]]
        self.assertEqual(result, expected)

    # Part 4
    def test_add_prices1(self):
        price1 = data.Price(5, 20)
        price2 = data.Price(4, 82)
        result = add_prices(price1, price2)
        expected = data.Price(10,2)
        self.assertEqual(result, expected)

    def test_add_price2(self):
        price1 = data.Price(3, 65)
        price2 = data.Price(9, 22)
        result = add_prices(price1, price2)
        expected = data.Price(12,87)
        self.assertEqual(result, expected)

    # Part 5
    def test_rectangle_area1(self):
        top_left = data.Point(0,6)
        bottom_right = data.Point(4, 3)
        result = rectangle_area(data.Rectangle(top_left, bottom_right))
        expected = 12
        self.assertEqual(result, expected)

    def test_rectangle_area2(self):
        top_left = data.Point(2, 7)
        bottom_right = data.Point(4, 3)
        result = rectangle_area(data.Rectangle(top_left, bottom_right))
        expected = 8
        self.assertEqual(result, expected)

    # Part 6
    def test_books_by_author1(self):
        book_list = [data.Book(['Ibi Zoboi'], 'American Street'),
                    data.Book(['Ibi Zoboi', 'Yusef Salaam'],'Punching the Air')]
        result = books_by_author("Ibi Zoboi", book_list)
        expected = book_list
        self.assertEqual(result,expected)

    def test_books_by_author2(self):
        book_list = [data.Book(['American Street'], 'Ibi Zoboi'),
                    data.Book(['Ibi Zoboi', 'Yusef Salaam'],'Punching the Air')]
        result = books_by_author("Yusef Salaam", book_list)
        expected = [book_list[1]]
        self.assertEqual(result,expected)

    # Part 7
    def test_circle_bound1(self):
        top_left = data.Point(0, 6)
        bottom_right = data.Point(4, 3)
        result = circle_bound(data.Rectangle(top_left, bottom_right))
        expected = data.Circle(data.Point(2.0, 4.5), 2.5)
        self.assertEqual(result, expected)

    def test_circle_bound2(self):
        top_left = data.Point(2, 7)
        bottom_right = data.Point(4, 3)
        result = circle_bound(data.Rectangle(top_left, bottom_right))
        expected = data.Circle(data.Point(3.0, 5.0), 2.23606797749979)
        self.assertEqual(result, expected)

    # Part 8
    def test_below_pay_average1(self):
        employee_list = [data.Employee("James", 25000), data.Employee("Cole", 80000),
                         data.Employee("Alex", 40000)]
        result = below_pay_average(employee_list)
        expected = ["James", "Alex"]
        self.assertEqual(result, expected)

    def test_below_pay_average2(self):
        employee_list = []
        result = below_pay_average(employee_list)
        expected = []
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
