import random

def generate_random_matrix(size):
    """Generates a square matrix of given size with random integers."""
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

def determinant_recursive(matrix):
    """Calculates the determinant of a square matrix recursively."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(size):
        sub_matrix = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant_recursive(sub_matrix)
    return det

def determinant_iterative(matrix):
    """Calculates the determinant of a square matrix iteratively using Gaussian elimination."""
    size = len(matrix)
    mat = [row[:] for row in matrix]  
    det = 1

    for i in range(size):
        
        if mat[i][i] == 0:
            for j in range(i + 1, size):
                if mat[j][i] != 0:
                    mat[i], mat[j] = mat[j], mat[i]
                    det *= -1
                    break
            else:
                return 0  

        det *= mat[i][i]
        for j in range(i + 1, size):
            factor = mat[j][i] / mat[i][i]
            for k in range(i, size):
                mat[j][k] -= factor * mat[i][k]

    return round(det)


if __name__ == "__main__":
    size = 3
    matrix = generate_random_matrix(size)
    print("Generated 3x3 Matrix:")
    for row in matrix:
        print(row)

    det_recursive = determinant_recursive(matrix)
    det_iterative = determinant_iterative(matrix)

    print(f"\nDeterminant (Recursive): {det_recursive}")
    print(f"Determinant (Iterative): {det_iterative}")