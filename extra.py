# #NOTE: question 1
# You run charity competitions in which people must guess how many lollies are in a jar. Everybody who guesses to within 100 of the actual number wins a prize. For example, if there are 1000 lollies in the jar a guess of 950 will win a prize. Write a function close_to(guesses,lollies) that filters a list of guesses to those that are within 100 of the actual number of lollies. The function should return the filtered list.

# def close_to(guesses, lollies):
#   result = []
#   for i in guesses:
#     if i <= lollies + 100 and i >= lollies - 100:
#       result.append(i)
#   return result

# def close_to(guesses, lollies):
#     filtered_guesses = [guess for guess in guesses if abs(guess - lollies) <= 100]
#     return filtered_guesses

# guesses = [800, 950, 1005, 1100, 1200]
# lollies = 1000
# print(close_to(guesses, lollies))

#NOTE: question 2
# Write a function find_key(input_dict, value) that takes as a parameter a dictionary and a value and returns the key in the dictionary that maps to the given value or None if no such key exists. In other words, the function finds the key such that input_dict[key] == value. You may assume that there is at most one such key in the dictionary.

# def find_key(input_dict, value):
#   return [key for key in input_dict if input_dict[key] == value]

# def find_key(input_dict, value):
#     for key, val in input_dict.items():
#         if val == value:
#             return key 
#     return None  

# input_dict = {'a': 1, 'b': 2, 'c': 3}
# print(find_key(input_dict, 5))  


#NOTE: question 3
# Write a function calculate_cartons(eggs) for a small local farm that takes a number of eggs and returns the number of egg cartons that will be needed to pack these eggs, assuming 12 eggs fit into a carton. Don't worry about any left over eggs (they will be eaten by the owner for breakfast). See the examples below for expected output.

# def calculate_cartons(eggs):
#   return eggs//12

# print(calculate_cartons(24))
    


#NOTE: question 4
# Create a function dinner_calculator(meal_cost, drinks_cost) that calculates and returns the total cost of the meal for a small restaurant during happy hour (drinks only are discounted).
# • The function takes two values, the cost of the meals and drinks before GST.
# • Before GST is applied, a 30% discount needs to be applied to the drinks cost.
# • Goods and services tax (GST) needs to be added to the meal and drinks cost, GST is set to 15%.
# • The function should return the total cost.
# • Do not worry about formatting the number of decimal places; this will be taught in a later lab.

# def dinner_calculator(meal_cost, drinks_cost):
#     discounted_drinks = drinks_cost * (1 - 0.3) 
#     total_before_gst = meal_cost + discounted_drinks
#     gst = total_before_gst * 0.15
#     total_cost = total_before_gst + gst
#     return total_cost


# print(dinner_calculator(50, 20))


#NOTE: question 5
# Write a function bmi_risk(bmi, age) that takes two positive numeric arguments into parameters bmi and age and returns a string Low, Medium, or High according to the following table:
# Under 45
# 45 or over
# BMI less than 22
# Low
# Medium
# BMI 22 or more
# Medium
# High

# def bmi_risk(bmi, age):
#   if bmi < 22 and age < 45:
#     return "low"
#   elif bmi < 22 and age >= 45:
#     return "medium"
#   elif bmi >= 22 and age < 45:
#     return "medium"
#   else:
#     return "high"

# print(bmi_risk(21, 44))


#NOTE: question 6

# A Magic Square is an n x n grid of numbers containing all the integers from 1 up to n2 inclusive, with the property that the sums of the elements in each row and each column and each diagonal are all equal. For example,
# 2
# 7
# 6
# 9
# 5
# 1
# 4
# 3
# 8
# is a 3 x 3 magic square, where all rows, columns, and diagonals sum to 15.
# Such a grid of numbers can be represented in Python as a nested list, in the above case it would be
# square = [
# [2, 7, 6],
# [9, 5, 1],
# [4, 3, 8]
# ]
# Write a function row_sums(square) that takes such a (possibly magic) square as a parameter and returns a list of the row sums. For example, with the above square it would return the list [15, 15, 15]. To give you practice with nested loops, you're not allowed to use the built-in sum function.

# def rows_sum(square):
#   return [sum(row) for row in square]


# def rows_sum(square):
#   result = []

#   for row in square:
#     sum_row = 0

#     for item in row:
#       sum_row += item
  
#     result.append(sum_row)

#   return result


# square = [
# [2, 7, 6],
# [9, 5, 1],
# [4, 3, 8]
# ]

# print(rows_sum(square))


#NOTE: question 7

# Write a function make_index(words_on_page) that takes a dictionary mapping from page number to a list of the unique words on that page and returns a dictionary that maps from a word to an ordered list of pages on which that word appears. All words are lower case.
# For example, if a 3 page book contains just the sentence "hi there fred" on page 1, the sentence "there we go go go" on page 2 and "fred was there was there" on page 3, the input dictionary words_on_page would be

# def make_index(words_on_page):
#   index = {}

#   for page, words in words_on_page.items():
#     for word in words:
#       if word not in index:
#         index[word] = [page]
#       else:
#         if page not in index[word]:
#           index[word].append(page)

#   print(index)


# data = {1: ['hi', 'there', 'fred'], 2: ['there', 'we', 'go'], 3: ['fred', 'was', 'there']}

# make_index(data)