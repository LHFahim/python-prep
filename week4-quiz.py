# question 1
# def ticket_price(age, is_member):
#     if is_member:
#         return 7
#     elif not is_member and (age < 12 or age >= 60):
#         if age < 12:
#             return 5
#         else:
#             return 6
#     else:
#         return 10

# print(ticket_price(10, False))
# print(ticket_price(65, False))


# question 2
# def process_transactions(transactions):
#     return [x ** 2 for x in transactions if x >= 100 or x <= -100]

# print(process_transactions([50, -200, 100, -150, 75]))
# print(process_transactions([0, 99, 101, -101]))

# question 3
# def extract_acronyms(product_name):
#     words = product_name.split()
#     acronym = ''.join(word[0].upper() for word in words)
#     return acronym

# print(extract_acronyms("advanced micro Devices"))
# print(extract_acronyms("international business machines"))
# print(extract_acronyms("graphic Processing unit"))


# question 4
# def multiply_vectors(row_vector, col_vector):
#     p = len(row_vector)
#     q = len(col_vector)
    
#     if p != q:
#         return "The vectors must be of the same length."
#     else:
#         product = sum(row_vector[i] * col_vector[i] for i in range(p))
#         return product

# print(multiply_vectors([1, 2, 3], [4, 5, 6]))
# print(multiply_vectors([-1, -2, -3], [-4, -5, -6]))
# print(multiply_vectors([7, 8], [9, 10]))