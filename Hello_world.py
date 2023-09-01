from math import * 
import math as m

# This is the first program
print('Hello World')

num_int = 10 # this is an integer  
num_float = 0.8 # this number is a float
print(num_int * (num_int + num_float))
print(num_int % 3)
print('max function for', num_int, 'is', max(num_int, 9))
print('abs function for', -num_int, 'is', abs(-num_int))
print('pow function 2 for', num_int, 'is', pow(num_int, 2))
print('round function for', num_float, 'is', round(num_float))

print('floor function for',num_float, 'is', floor(num_float))
print('ceil function for', num_float, 'is', ceil(num_float))
print('sqrt function for', num_int, 'is', sqrt(num_int))
print('exp function for',num_int, 'is', exp(num_int))
print('There are ' + str(num_int) + ' arm robots in the factory, ' + str(num_float) + ' of them are broken.')
print('There are', num_int, 'arm robots in the factory,', num_float, 'of them are broken.')

factory_name = "ABC"
print("The factory's name is  "+ factory_name)
print("The first character in the factory name is " + factory_name[0])
print("The third character in the factory name is " + factory_name[2])
print("Transform the factory name into lowercases",factory_name.lower())
print("check if tactory_name is lowercase: ", factory_name.islower())
print("Transform factory_name ", factory_name.upper().isupper())
print("print the length of factory_name:", len(factory_name))
print("Access to factory name, characters from 0 to -1 index", factory_name[0:len(factory_name)-1])
print("print the index of character A in factory_name", factory_name.index("A"))
print("replace ABC for DEF in factory_name", factory_name.replace("ABC", "DEF"))

print("Section 2")
print("-------------------------------------------------------------")


num_int = 10 # this is an integer
num_float = 0.5 # this is a float

# combining numbers with strings
print("There are " + str(num_int) + " arm robots in the factory, "+ str(num_float) + " of them are broken.") 

# using string variables
factory_name = "ABC"
print("The factory's name is " + factory_name)

# list of robot brands
robot_brands = ["ABB", "KUKA", "FANUC", "Omron"]

print(robot_brands)

# access the second robot brand in the above list
print(robot_brands[1])

# print the first three items in the list
print(robot_brands[:3])

# add another manufacturer "UR" to the above list
robot_brands.append("UR")
print(robot_brands)

# remove the manufacturer that we just added
robot_brands.remove("UR")
print(robot_brands)

# insert the manufacturer "UR" to the second index
robot_brands.insert(1, "UR")
print(robot_brands)

# sort() function --> sorts the list in assending order
robot_brands.sort()
print(robot_brands)

# reverse the order of the list
robot_brands.reverse()
print(robot_brands)

# length of the list
print(len(robot_brands))

# we now want to append another list to the robot_brands list
robot_brands_1 = ["Yaskawa", "Staubli"]
robot_brands.extend(robot_brands_1)
print(robot_brands)

# we want to get rid of the last element of the robot_brands list
robot_brands.pop()
print(robot_brands)

# find the index of the value "ABB"
print(robot_brands.index("ABB"))

# now let's find out how many times "ABB" is repeated 
print(robot_brands.count("ABB"))

# we want to make a copy of the robot_brands list
robot_brands2 = robot_brands.copy()
print(robot_brands)
print(robot_brands2)
# we can iterate through a list with a for loop
for robot_brand in robot_brands:
    print(robot_brand)
# we can remove everything in a list with clear function
robot_brands.clear()
print(robot_brands)



print ("Section 3, 2D lists, tuples, and dictionaries")
print("--------------------------------------------------------------------------")
# this is an example of a 2D lists
# 2D lists --> lists inside lists

# lets create a 3*3 matrix using 2D lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
# this matrix has 3 rows and 3 columns

# we can access individual elements within a 2D list using the row and column indices 
# the indices start from 0 

# we want to access the element in the first row and first column:
print(matrix[0][0])

# how about in the second row and third column?
print(matrix[1][2])
# this section is about tuples

robotic_engineers = ("Hannah", "Jim", "Bella", "John")
print(robotic_engineers)

# print the 2nd value in the tuple
print(robotic_engineers[1])

# unpack the tuple into the variables e1, e2, e3, and e4 that stand for engineers 1 through 4

e1, e2, e3, e4 = robotic_engineers
print(e1, e2, e3, e4)
print(e3)

# we cannot change anything inside the tuple
# robotic_engineers[1] = "Bob"

# we can make a list of tuples
robotic_partners = [(robotic_engineers[0],robotic_engineers[3]), (robotic_engineers[1], robotic_engineers[2])]
print(robotic_partners)
print(robotic_partners[0])


# this dictionary maps the name of the object to its corresponding color

objects_colors = {
    "ball": "red",
    "cube": "green",
    "flower": "pink",
    "pyramid": "blue"

}

print("the ball is " + objects_colors["ball"])
print("the cube is " + objects_colors["cube"])

print(objects_colors.get("floer", "no such object"))

# this dictionary maps the name of the object to its corresponding color

objects_colors = {
    "ball": "red",
    "cube": "green",
    "flower": "pink",
    "pyramid": "blue"

}

print("the ball is " + objects_colors["ball"])
print("the cube is " + objects_colors["cube"])

print(objects_colors.get("floer", "no such object"))
# a dictionary that maps robot arm joints to their corresponding min, max, and default joint angles
import math as m

arm_dict = {
    "joint1": {
        "min" : -m.pi/2,
        "max" : m.pi/2,
        "default" : 0,
    },

        "joint2": {
        "min" : -m.pi,
        "max" : m.pi,
        "default" : 0,
    },

        "joint3": {
        "min" : -m.pi/2,
        "max" : m.pi/2,
        "default" : 0,
    },

}


# now we can access the keys and values in this dictionary
joint_angles_1 = arm_dict["joint1"]
print(joint_angles_1)

# you can also access to individual angles within each joint in the dictionary
# this gives the max angle of joint 2
print(arm_dict["joint2"]["max"])

# print the min angle of joint3
print(arm_dict["joint3"]["min"])