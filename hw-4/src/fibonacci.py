import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def run_fibonacci_sync(n, num_runs):
    for _ in range(num_runs):
        fibonacci(n)


def run_fibonacci_with_threads(n, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def run_fibonacci_processes(n, num_processes):
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    n = 26

    num_runs = 10
    result = []
    for i in range(num_runs):
        sync_time = measure_time(run_fibonacci_sync, n+i, num_runs)
        threads_time = measure_time(run_fibonacci_with_threads, n+i, num_runs)
        processes_time = measure_time(run_fibonacci_processes, n+i, num_runs)
        temp = (
            f"n = {n+i}\n"
            f"Синхронно: {sync_time:.2f} с\n"
            f"Потоки: {threads_time:.2f} с\n"
            f"Процессы: {processes_time:.2f} с\n"
        )
        result.append(temp)
    result = "\n".join(result)
    with open("../artifacts/task_1.txt", "w") as file:
        file.write(result)

    print(result)
