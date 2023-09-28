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
#return error if the length of the vectors are not the same    
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length for inner product.")
   #to calculate the inner product by summing the product of the corresponding elements of the two vectors
   #to measure the execution time of the function and returns it.
    start_time=time.time()
    result = sum(x * y for x, y in zip(vector1, vector2))
    end_time=time.time()
    execution_time_1a = end_time - start_time
    return result, execution_time_1a
#define a function that calculates the outer product of vectors
#create zero matrix of the appropriate size(len(a) x len(b)). 
# iterate over the elements of the two vectors and multiplies them together, stor the result in the corresponding element of the matrix. 
#to measure the execution time of the function and returns it.
def outer_product(vector1, vector2):
    result = [[0] * len(vector2) for _ in range(len(vector1))]
    start_time=time.time()
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            result[i][j] = vector1[i] * vector2[j]
    end_time=time.time()
    execution_time_1b = end_time - start_time
    return result, execution_time_1b
#define a function that calculates the inner and outer product using einsum function from numpy library
#The np.einsum() function allows you to perform complex tensor operations in a concise way
def inner_outer_products_einsum(a, b, time):
    start_time = time.time()
    # Calculate inner product
    inner_result2 = np.einsum('i,i->', a, b)
    
    # Calculate outer product
    outer_result2 = np.einsum('i,j->ij', a, b)
    end_time = time.time()
    execution_time_2 = end_time - start_time
#return the results of einsum: inner, outer product and the time of execution    
    return inner_result2, outer_result2, execution_time_2
inner_result2, outer_result2, execution_time_2 = inner_outer_products_einsum(vector_a, vector_b, time)
#define a function to calculate the inner and outer product using numpy inner and outer product functions
def inner_outer_products(a, b):
    # Calculate inner product
    inner_result3 = np.inner(a, b)
    
    # Calculate outer product
    outer_result3 = np.outer(a, b)
    #return the inner and outer priduct calculated by numpy built in functions
    return inner_result3, outer_result3
  
start_time = time.time()
# Calculate inner and outer products
#calculta the execution time of the numpy inner and outer functions
inner_result3, outer_result3 = inner_outer_products(vector_a, vector_b)
end_time = time.time()
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
