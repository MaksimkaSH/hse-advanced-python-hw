import multiprocessing
import time
import codecs
from datetime import datetime


def run_process_a(queue_a, queue_b):
    while True:
        if queue_a.empty():
            continue
        message = queue_a.get()
        queue_b.put(message.lower())
        time.sleep(5)


def run_process_b(queue_b, queue_main):
    while True:
        if queue_b.empty():
            continue
        message = queue_b.get()
        result = codecs.encode(message, 'rot_13')
        print(f"{datetime.now()}: B: {result}")
        queue_main.put(result)


def main():
    main_queue = multiprocessing.Queue()
    queue_a = multiprocessing.Queue()
    queue_b = multiprocessing.Queue()
    process_a = multiprocessing.Process(target=run_process_a, args=(queue_a, queue_b))
    process_b = multiprocessing.Process(target=run_process_b, args=(queue_b, main_queue))
    process_a.start()
    process_b.start()

    try:
        while True:
            message = input()
            queue_a.put(message)
    except KeyboardInterrupt:
        process_a.terminate()
        process_b.terminate()


if __name__ == "__main__":
    main()
