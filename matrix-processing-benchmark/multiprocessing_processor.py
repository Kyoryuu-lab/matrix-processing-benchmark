# multiprocessing_processor.py
from multiprocessing import Process, Manager
from num2words import num2words
import time

def convert_to_text(matrix, result, start_row, end_row):
    for i in range(start_row, end_row):
        result[i] = [num2words(num, lang='uk') for num in matrix[i]]

def sort_columns_range(matrix, start_col, end_col):
    for col in range(start_col, end_col):
        column = [row[col] for row in matrix]
        column.sort(key=lambda x: len(x))
        for row_idx, value in enumerate(column):
            matrix[row_idx][col] = value

def process_matrix_parallel(matrix, num_processes):
    m = len(matrix)
    n = len(matrix[0])

    with Manager() as manager:
        result = manager.list([[None] * n for _ in range(m)])
        processes = []
        rows_per_process = m // num_processes
        for i in range(num_processes):
            start_row = i * rows_per_process
            end_row = (i + 1) * rows_per_process if i != num_processes - 1 else m
            process = Process(target=convert_to_text, args=(matrix, result, start_row, end_row))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return list(result)

def process_columns_parallel(matrix, num_processes):
    m = len(matrix)
    n = len(matrix[0])

    with Manager() as manager:
        result = manager.list([[None] * n for _ in range(m)])
        processes = []
        cols_per_thread = n // num_processes
        for i in range(num_processes):
            start_col = i * cols_per_thread
            end_col = (i + 1) * cols_per_thread if i != num_processes - 1 else n
            process = Process(target=sort_columns_range, args=(matrix, start_col, end_col))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        return list(result)

def run_multiprocessing(matrix, num_processes=10):
    """Performs matrix processing by processes and returns the execution time."""
    start_time = time.time()

    text_matrix = process_matrix_parallel(matrix, num_processes)
    process_columns_parallel(text_matrix, num_processes)

    end_time = time.time()
    return end_time - start_time
