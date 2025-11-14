# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    max1 = max(numbers)
    rest = [nums for nums in numbers if nums != max1]
    max2 = max(rest) if rest else None

    return (max1, max2)



# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(set(numbers))


# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    j = 0

    while j < len(arr):
        total += arr[j]
        result.append(total) 
        j += 1
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed = [[0] * rows for _ in range(columns)]

    i = 0
    while i < rows:
        j = 0
        while j < columns:
           transposed[j][i] = matrix [i][j]
           j += 1
        i += 1
    return transposed    


# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]


# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows_A = len(matrix1)
    column_A = len (matrix1[0])
    rows_B = len(matrix2)
    column_B = len(matrix2[0])

    if column_A != rows_B:
        return None
    
    result = [[0] * column_B for _ in range(rows_A)]

    i = 0

    while i < rows_A:
        j = 0 
        while j < column_B:
            k = 0
            while k < column_A:
                result [i][j] += matrix1[i][k] * matrix2[k][j]
                k += 1
            j += 1
        i += 1
    return result

