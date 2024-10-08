# def print_triangle(n):
#     for i in range(1, n + 1):
#         print('*' * i)

#     for i in range(n - 1, 0, -1):
#         print('*' * i)





# print_triangle(3)


# def print_mixed_types(a, b, c):
#     print(str(a + b) + " " + c)



# print_mixed_types(42, 3.14, "world")


# def is_even(n):
#     return n % 2 == 0

# def validate_even(numbers):
#     return [is_even(n) for n in numbers]


# print(validate_even([-2, -1, 0, 1, 2]))


# def multiplication_table(n):
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             print(i * j, end=" ")
#         print()

# multiplication_table(4)


# def swap_elements(lst, n):
#     lst[n], lst[-n-1] = lst[-n-1], lst[n]
#     return lst

# print(swap_elements(['a', 'b', 'c', 'd'], 0))


# def classify_grade(score):
#     if score >= 90:
#         print("Excellent")
#     elif 80 <= score <= 89:
#         print("Very Good")
#     elif 70 <= score <= 79:
#         print("Good")
#     elif 60 <= score <= 69:
#         print("Average")
#     elif 50 <= score <= 59:
#         print("Pass")
#     else:
#         print("Fail")

# classify_grade(78)