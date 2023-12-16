from queue import Queue
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


while True:
    generate_request()
    process_request()
