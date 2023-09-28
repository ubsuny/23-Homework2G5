import numpy as np
import time

#import numpy library for sciectific calcualations
import numpy as np
#import time library to calculate time
import time

#to get input vectors from the user and ask the user to enter a vector as a comma-separated string
#splits the string into a list of strings, and converts each string to a float
#It will return the list of floats as a vector
def get_vector_input():
    try:
        input_str = input("Enter a vector as comma-separated values (e.g., 1,2,3): ")
        vector = [float(x.strip()) for x in input_str.split(",")]
        return vector
    except ValueError:
        print("Invalid input. Please enter the vector in the correct format.")
        return get_vector_input()

# Get input for two vectors
print("Enter the first vector:")
vector_a = get_vector_input()

print("Enter the second vector:")
vector_b = get_vector_input()

#print the 2 vectors that the user chose.
print("Your chosen Vector A is:", vector_a)
print("Your chosen Vector B is:", vector_b, "\n")

#creat a function named inner_product to calculate the inner product
def inner_product(vector1, vector2):   
    """
   This Code Calculates the inner product of two vectors using a for loop.


   Args:
    a:   array representing the first vector.
    b:   array representing the second vector.

   Returns:
    The inner product of the two vectors.
    A numpy array representing the outer product of the two vectors.

   """
   #return error if the length of the vectors are not the same  
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length for inner product.")
    #start the timer to calculate time
    start_time=time.time()
   # calculate the inner product by summing the product of the corresponding elements of the two vectors
    result = sum(x * y for x, y in zip(vector1, vector2))
   #set the end time to timer to stop
    end_time=time.time()
  #Calculate the execution time of the function and returns it.
    execution_time_1a = end_time - start_time
    return result, execution_time_1a

#Outer Product:
#define a function that calculates the outer product of vectors
def outer_product(vector1, vector2):
 
    result = [[0] * len(vector2) for _ in range(len(vector1))]
    start_time=time.time()
   
    # iterate over the elements of the two vectors and multiplies them together, stor the result in the corresponding element of the matrix. 

    for i in range(len(vector1)):
        for j in range(len(vector2)):
            result[i][j] = vector1[i] * vector2[j]
    end_time=time.time()
# measure the execution time of the function and returns it.  
    execution_time_1b = end_time - start_time
    return result, execution_time_1b
###################################################################################################
#Einsum Numpy
#define a function that calculates the inner and outer product using einsum function from numpy library
#The np.einsum() function allows you to perform complex tensor operations in a concise way
def inner_outer_products_einsum(a, b, time):
    """
        This Code Calculates the inner and outer product of two vectors using numpy built-in einsum function
    Args:
    a:  NumPy array representing the first vector.
    b:  NumPy array representing the second vector.
    Returns:
        The inner product of the two vectors.
        A numpy array representing the outer product of the two vectors.
    
    """
    #use time function to start the time calculation
    start_time = time.time()
    # Calculate inner product using einsum
    inner_result2 = np.einsum('i,i->', a, b)
    
    # Calculate outer product using einsum
    outer_result2 = np.einsum('i,j->ij', a, b)
    end_time = time.time()
    execution_time_2 = end_time - start_time
   
    #return the results of function: inner, outer product and the time of execution    
    return inner_result2, outer_result2, execution_time_2
inner_result2, outer_result2, execution_time_2 = inner_outer_products_einsum(vector_a, vector_b, time)
##################################################################################################
#Numpy Functions:
#define a function to calculate the inner and ouer product
def inner_outer_products(a, b):
    """
    This Code Calculates the inner and outer product of two vectors using numpy built in functions
    Args:
    a:  NumPy array representing the first vector.
    b:  NumPy array representing the second vector.
    Returns:
        The inner product of the two vectors.
        A numpy array representing the outer product of the two vectors.
    
    """
    # Calculate inner product using numpy inner product function and assign the result to the variable inner_result3
    inner_result3 = np.inner(a, b)
    
    # Calculate outer product using numpy outer product function and assign the result to the variable outer_result3
    outer_result3 = np.outer(a, b)
    return inner_result3, outer_result3
    
start_time = time.time()
# variables inner_result3 and outer_result3 are the output of the function
inner_result3, outer_result3 = inner_outer_products(vector_a, vector_b)
end_time = time.time()
#calculate the execution time of Numpy functions
execution_time_3 = end_time - start_time

#Printing results
#for-loop
inner_result, execution_time_1a = inner_product(vector_a, vector_b)
outer_result, execution_time_1b = outer_product(vector_a, vector_b)

print("----------------------- For-loops-----------------------")
print("The Inner product:", inner_result)
print("The Outer product:")
for row in outer_result:
    print(row)
print(f"Execution Time: {execution_time_1b+execution_time_1a} seconds", "\n")

#Einsum
print("----------------------- numpy_einsum-----------------------")
print("Inner product:", inner_result2)
print("Outer product:")
print(outer_result2)
print("Execution time:", execution_time_2, "seconds", "\n")

#Numpy
print("----------------------- numpy-----------------------")
print("Inner product using numpy:", inner_result3)
print("Outer product using numpy:")
print(outer_result3)
print("Execution time:", execution_time_3, "seconds")
