my_list = [0, 1, 2, 3, 4, 5, "yo"]
# print(f"This is my list {my_list}")
# print(f"Value of an index {my_list[-1]}")
# for element in my_list:
#     print(element,end=" ")

my_tuple = (1, 2, 3)

# print(", ".join(map(str,my_list)))
# for element in my_tuple:
#     print(element,end=" ")


def multiply_by_two(numbers):
    # return [number * 2 for number in numbers]
    new_list = []
    for number in numbers:
        new_list.append(number * 2)

    return new_list


# print(multiply_by_two([1, 2, 3, 4, 5]))


def multiply_list_by_two(number_list):
    new_number_list = []

    for number in number_list:
        result = multiply_number_by_two(number)
        new_number_list.append(result)

    # print(new_number_list)


def multiply_number_by_two(number):
    return number * 2


numbers = [1, 2, 3, 4, 5]

multiply_list_by_two(numbers)

length_of_numbers = len(numbers)
# print(length_of_numbers)


temp_array = [1, 2, 3, 4, 5]

# temp  = temp_array[0]
# temp_array[0] = temp_array[1]
# temp_array[1] = temp


def multiply_even_numbers(numbers):
    new_numbers = []
    for number in numbers:
        result = number * 2 if number % 2 == 0 else number
        new_numbers.append(result)
    return new_numbers


# print(multiply_even_numbers(temp_array))


for i in range(1, 4):
    for j in range(0, 4):
        print(2 * (i + j), end=" ")
    print()

# 2 4 6 8
# 4 6 8 10
# 6 8 10 12
