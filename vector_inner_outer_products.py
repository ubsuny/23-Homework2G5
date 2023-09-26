#This code asks user two vectors and finds out its inner and outer products.
import time
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

print("Your chosen Vector A is:", vector_a)
print("Your chosen Vector B is:", vector_b)

def inner_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length for inner product.")
    start_time=time.time()
    result = sum(x * y for x, y in zip(vector1, vector2))
    end_time=time.time()
    execution_time_1a = end_time - start_time
    return result, execution_time_1a

def outer_product(vector1, vector2):
    result = [[0] * len(vector2) for _ in range(len(vector1))]
    start_time=time.time()
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            result[i][j] = vector1[i] * vector2[j]
    end_time=time.time()
    execution_time_1b = end_time - start_time
    return result, execution_time_1b

# Example usage:
#vector_a = [1, 2, 3]
#vector_b = [4, 5, 6]

inner_result, execution_time_1a = inner_product(vector_a, vector_b)
outer_result, execution_time_1b = outer_product(vector_a, vector_b)

print("The Inner product is:", inner_result)
print(f"Execution Time for the Inner Product is: {execution_time_1a} seconds")
print("The Outer product is:")
for row in outer_result:
    print(row)
print(f"Execution Time for the Outer Product is: {execution_time_1b} seconds")
