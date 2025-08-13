# main.py
from matrix_generator import generate_matrix
from threading_processor import run_threading
from multiprocessing_processor import run_multiprocessing
from results_saver import save_results_to_desktop

def main():
    M, N = 60, 60
    NUM_THREADS = 10
    NUM_PROCESSES = 10

    print("[INFO] Generating matrix...")
    matrix = generate_matrix(M, N)

    print("[INFO] Launching Threading...")
    threading_time = run_threading(matrix, NUM_THREADS)
    print(f"[RESULT] Threading time: {threading_time:.6f} seconds")

    print("[INFO] Launching Multiprocessing...")
    multiprocessing_time = run_multiprocessing(matrix, NUM_PROCESSES)
    print(f"[RESULT] Multiprocessing time: {multiprocessing_time:.6f} seconds")

    save_results_to_desktop(threading_time, multiprocessing_time)

if __name__ == "__main__":
    main()
