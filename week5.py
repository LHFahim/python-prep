# dictionary for key and value pair

student_marks = {"Rabi" : 84, "Namul" : 64, "Pok" : 95}

# print(f"Rabi's mark is : {student_marks["Rabi"]}")

cars = {"brand" : "Toyota", "year" : 2010, "milage" : 60000}

# print specfic dict using variable
def car_info(i):
    print(cars[i])

# car_info("year")

# correct answer
def car_info(cars):

    print(f"Brand : {cars["brand"]}")
    print(f"Year : {cars["year"]}")
    print(f"Milage : {cars["milage"]}")

# car_info(cars)

# # if dict is not defined, put the dict into the calling function
def car_info(car2):

    # add if to check the key is there
    if "brand" in cars: print(f"Brand : {cars["brand"]}")
    if "year" in cars: print(f"Year : {cars["year"]}")
    if "model" in cars: print(f"Model : {cars["model"]}")

# car_info({"brand" : "Toyota", "year" : 2010, "milage" : 60000})
# car_info(cars) # the variable "cars" here is referring to the dict

# value in dict can be a list
courses = {"COIT20245" : [2, 3], "COIT20246" : [2, 3], "COIT20248" : [2,2]}

for i in courses:
    lect_and_tut_hours = courses[i] # get the value (the list) from the dict
    lect_hrs = lect_and_tut_hours[0]
    tut_hours = lect_and_tut_hours[1]

# for i in courses:
#     print(i)

# # use .keys to get the keys (left columns in the dict)
# for i in courses.keys():
#     print(i)

cars2 = {"brand" : "Toyota", "year" : 2010, "milage" : 60000}

# # use .items to get the items in the dict
cars2_items = cars2.items()

# print(cars2_items) # the result will be dict_item(...)

# # use round blanket () as a tuple; [] as a list
# # tuple is fixed and cannot replace the elements in it
my_tuple = (1, 2, 3, 5)

# # use list method to remove the dict_item
# print(list(cars2_items))

# # set key_value_pairs as a list of key value pair
# key_value_pairs = list(cars2_items)

# brand = key_value_pairs[0][1] # extract the element from the list

# print(brand)