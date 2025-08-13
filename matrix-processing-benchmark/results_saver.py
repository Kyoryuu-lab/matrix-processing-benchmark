# results_saver.py
import os
from datetime import datetime

def save_results_to_desktop(threading_time, multiprocessing_time):
    """Saves test results to results.txt on your desktop (appends to the end of the file)."""
    # Path to Desktop (Cross-Platform)
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    results_file = os.path.join(desktop_path, "results.txt")

    with open(results_file, "a", encoding="utf-8") as f:
        f.write(f"=== Test from {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")
        f.write(f"Threading time: {threading_time:.6f} seconds\n")
        f.write(f"Multiprocessing time: {multiprocessing_time:.6f} seconds\n")
        if threading_time < multiprocessing_time:
            f.write("Threading is faster.\n")
        elif multiprocessing_time < threading_time:
            f.write("Multiprocessing is faster.\n")
        else:
            f.write("Both methods took the same amount of time.\n")
        f.write("\n")  # Empty line between tests

    print(f"[INFO] Results added to {results_file}")
