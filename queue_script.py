from queue import Queue
import time
import uuid


queue = Queue()


def generate_request():
    task = str(uuid.uuid4())
    queue.put(task)


def process_request():
    if not queue.empty():
        task = queue.get()
        print("task - ", task)
    else:
        print("Queue is empty.")


try:
    while True:
        generate_request()
        time.sleep(2)
        process_request()
        time.sleep(3)
except KeyboardInterrupt:
    print("Bye!")
