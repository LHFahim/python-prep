# q1
# def calculate_raise(salary, years):
#     if salary < 500:
#         if years >= 10:
#             return salary * 3
#         else:
#             return salary * 2
#     else:
#         return salary
# print(calculate_raise(400,29))

# q2
# def display(magic_square):
#     for row in magic_square:
#         print('|', ' '.join(map(str, row)), '|')

# square = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 1, 1, 2],
#     [3, 4, 5, 6]
# ]
# display(square)

# q3
# jobs = [
#     "Drive Yellow:Security Manager:$160,000",
#     "Dept Transport Vic:Cyber Security Coordinator:$127,000"
# ]

# pays = list(map(lambda job: job.split(':')[-1], jobs))
# pays = [pay.strip().replace(",", "") for pay in pays]

# print(pays)


# q4
def movie_details(movie):
    title = movie['Title']
    ratings = movie['Ratings']

    rotten_tomatoes_rating = None
    for rating in ratings:
        if rating['Source'] == 'Rotten Tomatoes':
            rotten_tomatoes_rating = rating['Value']
            break

    if rotten_tomatoes_rating:
        print(f"Title: {title}")
        print(f"Rating: {rotten_tomatoes_rating}")
    else:
        print(f"Title: {title}")
        print("Rating: Not found")


movie={'Title': 'Gremlins',
  'Ratings': [ {'Source': 'IMDb', 'Value': '7.3'},
               {'Source': 'Rotten Tomatoes', 'Value': '86%'} ]
}
movie_details(movie)