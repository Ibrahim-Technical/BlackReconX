
from concurrent.futures import ThreadPoolExecutor

def threaded_runner(targets, worker_func, max_threads=5):
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(worker_func, targets)
