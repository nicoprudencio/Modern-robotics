import numpy as np 



# FIRST WE DEFINE AND PRINT THE MATRIX
rotation_matrix = np.array([[-0.5,0.866,0], [-0.866, -0.5, 0], [0,0,1]]) 
print ("Rotation Matrix:")
print (rotation_matrix) 

condition = False # we initialize the condition as false

# THEN WE VERIFY THAT THE TRANSPOSE IS EQUAL TO THE INVERSE MATRIX AND IN CASE IT IS TRUE WE GET A TRUE CONDITION
inverse_matrix = resultInverse= np.linalg.inv(rotation_matrix)
# print (inverse_matrix)
transpose_matrix = rotation_matrix.transpose()
# print (transpose_matrix)
if np.array_equal(np.round(transpose_matrix,decimals = 3), np.round(inverse_matrix,decimals = 3)):
    condition = True
else:
    condition = False

determinant = np.linalg.det(rotation_matrix)

if ( (condition == True and (determinant == 1)) or ((condition == True and (determinant > 0.9999) and (determinant < 1.0001))) ):
    print ("This is a rotation matrix because its determinant is: " , determinant, "(1 or very close to 1), and the inverse of the matrix is equal to the transpose of the same matrix")

else:
    print("This is NOT a rotation matrix, its determinant is: ", determinant)



