import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing


def integrate(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate_parallel(f, a, b, n_jobs, executor_class=None):
    chunk_size = 10000000 // n_jobs
    futures = []
    results = []
    with executor_class(max_workers=n_jobs) as executor:
        delta = (b - a) / n_jobs
        for i in range(n_jobs):
            start = a + i * delta
            end = start + delta
            futures.append(executor.submit(integrate, f, start, end, chunk_size))
        for future in futures:
            results.append(future.result())

    return sum(results)


if __name__ == "__main__":

    cpu_count = multiprocessing.cpu_count()
    results = []

    for n_jobs in range(1, cpu_count * 2 + 1):
        start_time = time.time()
        integrate_threaded = integrate_parallel(math.cos, 0, math.pi / 2, n_jobs, executor_class=ThreadPoolExecutor)
        threads_time = time.time() - start_time

        start_time = time.time()
        integrate_processed = integrate_parallel(math.cos, 0, math.pi / 2, n_jobs, executor_class=ProcessPoolExecutor)
        processes_time = time.time() - start_time

        results.append(f"n_jobs = {n_jobs}: потоки = {threads_time:.2f}с, процессы = {processes_time:.2f}с\n")

    with open("../artifacts/task_2.txt", "w") as f:
        for el in results:
            print(el)
            f.write(el)
