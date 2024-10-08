# quiz 1
#     *
#    ***
#   *****
#  *******
# *********

# def print_triangle(n):
#     for i in range(1, n+1):
#         print(" "*(n-i) + "*"*(2*i-1))

# print_triangle(5)

# def print_mixed_types(a,b,c):
#     sum_ab = a + b
 
#     print(str(sum_ab) + " " + c)
#     # print(f"{a+b} {c}")


# print_mixed_types(2,3.4,"hello")

# def is_even(number):
#   if number%2==0:
#     return True
#   else:
#     return False


# def validate_even(numbers):
#     # result = []
#     # for number in numbers:
#     #   result.append(is_even(number))
#     # return result
#     return [is_even(number) for number in numbers]

# print(validate_even([1,2,3,4,5,6,7,8,9,10]))

# def multiplication_table(n):
#     for i in range(1, n+1):
#         print(f"{i} {n}")

# multiplication_table(5)

# def multiplication_table(n):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(i * j, end=" ")
#         print()

# multiplication_table(5)


# def swap_elements(lst, n):
#     # temp = lst[n]
#     # lst[n] = lst[-n]
#     # lst[-n] = temp
#     lst[n], lst[-(n+1)] = lst[-(n+1)], lst[n]
#     return lst

# print(swap_elements([1,2,3,4,5], 1))




# def classify_grade(score):
#   if score >= 90:
#     print("Excellent")
#   elif score >= 80 and score <= 89:
#     print("Good")
#   elif score >= 70 and score <= 79:
#     print("Average")
#   elif score >= 60 and score <= 69:
#     print("Poor")
#   else:
#     print("Fail")

# classify_grade(95)

# quiz 2

# def ticket_price(age, is_member):
#   if is_member:
#     return 7
#   elif age < 12 and not is_member:
#     return 5
#   elif age >= 60 and not is_member:
#     return 6
#   else:
#     return 10

# print(ticket_price(10, True))
# print(ticket_price(10, False))
# print(ticket_price(60, True))
# print(ticket_price(60, False))
# print(ticket_price(20, True))
# print(ticket_price(20, False))
# print(ticket_price(70, True))
# print(ticket_price(70, False))


# def process_transactions(transactions):
#   return [transaction ** 2 for transaction in transactions if transaction >= 100 or transaction <= -100]


# print(process_transactions([100, 200, 300, -100, -200, -300, 50, -50]))


# def extract_acronyms(product_name):
#     words = product_name.split()
#     acronyms = ""
#     for word in words:
#       acronyms += word[0].upper()
#     return acronyms

#     # return ''.join([word[0].upper() for word in product_name.split()])

# print(extract_acronyms("Hello World of Warcraft"))
# print(extract_acronyms("Hello"))


# def multiply_vectors(row_vector, col_vector):
#   if len(row_vector) != len(col_vector):
#     print("Vectors must be of the same length.")
#     return
#   result = 0
#   for i in range(len(row_vector)):
#     result += row_vector[i] * col_vector[i]
#   print(result)

# row_vector = [1, 2, 3]
# col_vector = [4, 5, 6]
# multiply_vectors(row_vector, col_vector)  # Output: 32


# quiz 3

# def movie_details(movie):
#   title = movie["Title"]
#   year = movie["Year"]
#   plot = movie["Plot"]

#   print(f"{title} ({year}) - {plot}")

# movie = {
#     'Title': 'Gremlins',
#     'Year': '1984',
#     'Rated': 'PG',
#     'Runtime': '106 min',
#     'Genre': 'Comedy, Fantasy, Horror',
#     'Director': 'Joe Dante',
#     'Actors': 'Zach Galligan, Phoebe Cates, Hoyt Axton',
#     'Plot': 'A young man inadvertently breaks three important rules concerning his new pet '
#             'and unleashes a horde of malevolently mischievous monsters on a small town.',
#     'Language': 'English, Spanish',
#     'Awards': '8 wins & 7 nominations',
#     'Rotten Tomatoes Rating': '86%',
#     'BoxOffice': '$153,642,180'
# }

# movie_details(movie)


# def display_movie_info(movie):
#     # Check if 'Title' exists in the dictionary and print it if available
#     if 'Title' in movie:
#         title = movie['Title']
#         # print(f"Title: {movie['Title']}")
    
#     # Check if 'Year' exists in the dictionary and print it if available
#     if 'Year' in movie:
#         year = movie['Year']
#         # print(f"Year: {movie['Year']}")
    
#     # Check if 'Plot' exists in the dictionary and print it if available
#     if 'Plot' in movie:
#         plot = movie['Plot']
#         # print(f"Plot: {movie['Plot']}")
    
#     print(f"{title} ({year}) - {plot}")

# # Example usage
# movie_temp = {
#     'Title': 'Gremlins',
#     'Year': '1984',
#     'Rated': 'PG',
#     'Runtime': '106 min',
#     'Genre': 'Comedy, Fantasy, Horror',
#     'Director': 'Joe Dante',
#     'Actors': 'Zach Galligan, Phoebe Cates, Hoyt Axton',
#     'Plot': 'A young man inadvertently breaks three important rules concerning his new pet '
#             'and unleashes a horde of malevolently mischievous monsters on a small town.',
#     'Language': 'English, Spanish',
#     'Awards': '8 wins & 7 nominations',
#     'Rotten Tomatoes Rating': '86%',
#     'BoxOffice': '$153,642,180'
# }

# display_movie_info(movie_temp)



# def movie_details(movie):
#     # Iterate through all key-value pairs in the movie dictionary using items()
#     for key, value in movie.items():
#         print(f"{key}: {value}")

# # Example usage
# movie = {
#     'Title': 'Gremlins',
#     'Year': '1984',
#     'Rated': 'PG',
#     'Runtime': '106 min',
#     'Genre': 'Comedy, Fantasy, Horror',
#     'Director': 'Joe Dante',
#     'Actors': 'Zach Galligan, Phoebe Cates, Hoyt Axton',
#     'Plot': 'A young man inadvertently breaks three important rules concerning his new pet '
#             'and unleashes a horde of malevolently mischievous monsters on a small town.',
#     'Language': 'English, Spanish',
#     'Awards': '8 wins & 7 nominations',
#     'Rotten Tomatoes Rating': '86%',
#     'BoxOffice': '$153,642,180'
# }

# movie_details(movie)


# def place(queue, name):
#     print(queue)
#     return queue.index(name)

# # Example usage
# queue = ['John', 'Venu', 'Alice', 'Bob']
# name = 'Bob'
# print(place(queue, name))  # Output: 2


# def dequeue(queue):
#     return queue.pop(0)

# queue = ['John', 'Venu', 'Alice', 'Bob']
# print(dequeue(queue))  # Output: John


# import math

# Function to calculate the speed rounded up
# def calculate_speed(distance, time):
#     speed = distance / time
#     return math.ceil(speed)

# # Function to calculate speeds for all journeys
# def journey_speeds(journeys):
#     # Create a new dictionary to store the results
#     speeds = {}
    
#     # Iterate through the journeys dictionary using items()
#     for journey_name, data in journeys.items():
#         # data[0] is the distance, data[1] is the time
#         distance, time = data
#         # Calculate the speed using the calculate_speed function
#         speeds[journey_name] = calculate_speed(distance, time)
    
#     return speeds

# # Example usage
# journeys = {
#     "Trip1": [100, 2],
#     "Trip2": [150, 3],
#     "Trip3": [200, 4]
# }

# result = journey_speeds(journeys)
# print(result)  # Output: {'Trip1': 50, 'Trip2': 50, 'Trip3': 50}



# quiz 4

# def calculate_salary(salary, years):
#   if salary < 500 and years >= 10:
#     return salary * 3
#   elif salary < 500 and years < 10:
#     return salary * 2
#   else:
#     return salary
  
# print(calculate_salary(400, 5))  # Output: 800


# def extract_pay(jobs):
#     pay = []
#     for job in jobs:
#         pay.append(job.split(":")[2])

#     print(pay)

# jobs = [
#     "Drive Yellow:Security Manager:$160,000",
#     "Dept Transport Vic:Cyber Security Coordinator:$127,000"
# ]

# extract_pay(jobs)  # Output: ['160,000', '127,000']

# def movie_details(movie):
#   title = movie["Title"]
#   ratings = movie["Ratings"]
 

#   numbers = [1,2,3]
#   result = map(lambda n: n*2, numbers)

#   res = map(lambda rating: rating["value"] if rating["Source"] == "Rotten Tomatoes" else None, ratings)
  
#   for rating in res:
#     if rating != None:
#       temp = rating

#   print(title)
#   print(temp)


# def movie_details(movie):
#   for rating in movie["Ratings"]:
#     if rating["Source"] == "Rotten Tomatoes":
#       print(rating["value"])
#       break;


# movie = {
#     'Title': 'Gremlins',
#     'Ratings': [
#         {'Source': 'Internet Movie Database', 'value': '7.3/10'},
#         {'Source': 'Rotten Tomatoes', 'value': '86%'},
#         {'Source': 'Metacritic', 'value': '70/100'}
#     ],
#     'BoxOffice': '$153,642,180'
# }

# movie_details(movie)  # Output: ['7.3/10', '86%', '70/100']


# quiz 5

# def total_top4(sales):
#   sales.sort(reverse=True)

#   total = 0
#   # for i in range(4):
#   #   total += sales[i]

#   total = sum(sales[:4])
#   print(total)

# total_top4([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

# def print_names(names):
#     # for name in names:
#     #     print(name)

#     while len(names) > 0:
#         print(names.pop(0), end="\n")

# names = ["Alice", "Bob", "Charlie", "David"]
# print_names(names)  # Output: Alice Bob Charlie David


# def print_names2(people):
#   index = 0
#   while index < len(people):
   

#     new_index = 0
#     while new_index < len(people[index]):
#       print(people[index][new_index], end=" ")
#       new_index += 1
#     print()

#     index += 1

# people = [["John", "Doe"], ["Jane", "Smith"], ["Alice", "Johnson"]]
# print_names2(people)  # Output: John Doe Jane Smith Alice Johnson


# def sentinel_input_loop():
#     total = 0
#     while True:
#         user_input = input("> ")
#         if user_input == "exit":
#             break
#         total += int(user_input)
    
#     print(total)

# # Example usage
# sentinel_input_loop()
