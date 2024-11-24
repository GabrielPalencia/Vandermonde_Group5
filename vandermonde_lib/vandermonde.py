def vandermonde_matrix(x):
    n = len(x)
    vandermonde = []
    for i in range(n):
        row = [x[i]**j for j in range(n)]
        vandermonde.append(row)
    return vandermonde

def gauss_jordan(matrix):
    n = len(matrix)
    augmented = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    for i in range(n):
        if augmented[i][i] == 0:
            raise ValueError("The matrix is ​​not invertible.")

        pivot = augmented[i][i]
        augmented[i] = [elem / pivot for elem in augmented[i]]

        for j in range(n):
            if j != i:
                factor = augmented[j][i]
                augmented[j] = [augmented[j][k] - factor * augmented[i][k] for k in range(2 * n)]

    inverse = [row[n:] for row in augmented]
    return inverse

def matrix_dot_vector(matriz, vector):
    result = []
    for row in matriz:
        product = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(round(product, 3))
    return result

def interpolated_polynomial(coefficients):
    n = len(coefficients)
    polynomial = ""
    for i in range(n):
        if coefficients[i] != 0:
            if i == 0:
                polynomial += f"{coefficients[i]}"
            elif i == 1:
                polynomial += f" + {coefficients[i]}x"
            else:
                polynomial += f" + {coefficients[i]}x^{i}"
    return polynomial

def roots_evaluations(coefficients, x):
    n = len(coefficients)
    for i in range(n):
        result = 0
        for j in range(n):
            result += coefficients[j] * x[i]**j
        print(f"f({x[i]}) = {result}")

def Vandermonde(set_of_points):
    x = [point[0] for point in set_of_points]
    b = [point[1] for point in set_of_points]
    V = vandermonde_matrix(x)
    I = gauss_jordan(V)
    coefficients = matrix_dot_vector(I, b)
    polynomial = interpolated_polynomial(coefficients)

    print("Roots and evaluations:")
    roots_evaluations(coefficients, x)

    return polynomial
