# threading_processor.py
import threading
import time
from num2words import num2words

def convert_to_text(matrix, result, start_row, end_row):
    for i in range(start_row, end_row):
        result[i] = [num2words(num, lang='uk') for num in matrix[i]]

def sort_columns_range(matrix, start_col, end_col):
    for col in range(start_col, end_col):
        column = [row[col] for row in matrix]
        column.sort(key=lambda x: len(x))
        for row_idx, value in enumerate(column):
            matrix[row_idx][col] = value

def process_matrix_parallel(matrix, num_threads):
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    result = [[None] * n for _ in range(m)]

    threads = []
    rows_per_thread = m // num_threads
    for i in range(num_threads):
        start_row = i * rows_per_thread
        end_row = (i + 1) * rows_per_thread if i != num_threads - 1 else m
        thread = threading.Thread(target=convert_to_text, args=(matrix, result, start_row, end_row))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

def process_columns_parallel(matrix, num_threads):
    if not matrix:
        return
    n = len(matrix[0])
    threads = []
    cols_per_thread = n // num_threads
    for i in range(num_threads):
        start_col = i * cols_per_thread
        end_col = (i + 1) * cols_per_thread if i != num_threads - 1 else n
        thread = threading.Thread(target=sort_columns_range, args=(matrix, start_col, end_col))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

def run_threading(matrix, num_threads=10):
    """Performs matrix processing in threads and returns the execution time."""
    start_time = time.time()

    text_matrix = process_matrix_parallel(matrix, num_threads)
    process_columns_parallel(text_matrix, num_threads)

    end_time = time.time()
    return end_time - start_time
