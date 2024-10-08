# question 1

# def total_top4(sales):
#     sorted_sales = sorted(sales, reverse=True)
#     top4_sales = sorted_sales[:4]
#     return sum(top4_sales)

# print(total_top4([967, 345, 98, 230, 650]))  # Should return 2192


# question 2
# def print_names(names):
#     index = 0
#     while index < len(names):
#         print(names[index])
#         index += 1

# print_names(['John', 'Mary', 'Donald'])


# question 3
# def print_names2(people):
#     person_index = 0
#     while person_index < len(people):
#         person = people[person_index]
#         to_print = ""
        
#         name_index = 0
#         while name_index < len(person):
#             to_print += person[name_index] + " "
#             name_index += 1
            
#         print(to_print.strip())  
#         person_index += 1

# # Example usage:
# print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])


# question 4
# total = 0

# while True:
#     command = input(">")
#     if command.lower() == "exit":
#         break
#     else:
#         total += int(command)

# print(total)


# question 5
# def num_rushes(slope_height, rush_height_gain, back_sliding):
#     current_height = 0
#     num_rushes = 0
    
#     while current_height < slope_height:
#         num_rushes += 1
#         current_height += rush_height_gain        
#         if current_height >= slope_height:
#             break

#         current_height -= back_sliding
    
#     return num_rushes

# ans = num_rushes(10, 10, 9)
# print(ans)  

