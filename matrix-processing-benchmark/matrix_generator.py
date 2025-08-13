# matrix_generator.py
import random

def generate_matrix(m, n):
    """Generates an MxN matrix with random integers in the range [-1000, 1000]."""
    return [[random.randint(-1000, 1000) for _ in range(n)] for _ in range(m)]

def main():
    M, N = 60, 60  # Matrix size
    print(f"[INFO] Generate a matrix of size {M}x{N}...")
    
    matrix = generate_matrix(M, N)
    print("[INFO] The matrix is generated.")
if __name__ == "__main__":
    main()
