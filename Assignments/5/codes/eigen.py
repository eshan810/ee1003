import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('./qr_decomposition.so')

# Define the function prototype
lib.find_real_eigenvalues.argtypes = [ctypes.POINTER(ctypes.c_double * 2 * 2), ctypes.POINTER(ctypes.c_double * 2)]
lib.find_real_eigenvalues.restype = None

# Define the companion matrix for the quadratic equation x^2 - 4x + 6 = 0
companion_matrix = np.array([[0, -182], [1, 27]], dtype=np.float64)

# Prepare input for the C function
matrix_data = (ctypes.c_double * 4)(*companion_matrix.flatten())  # Flatten the 2x2 matrix
matrix_ptr = ctypes.POINTER(ctypes.c_double * 2 * 2)((ctypes.c_double * 2 * 2).from_buffer(matrix_data))
eigenvalues = (ctypes.c_double * 2)()  # To hold 2 real eigenvalues

# Call the function
lib.find_real_eigenvalues(matrix_ptr, eigenvalues)

# Extract the eigenvalues
eigenvalues_extracted = [eigenvalues[i] for i in range(2)]

# Print the roots of the quadratic equation
print("Roots of the quadratic equation:", eigenvalues_extracted)

