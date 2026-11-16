
import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer


def main():
    # Create the shared queue
    event_queue = Queue()

    # Create producer and consumer
    producer = CSVProducer(event_queue, "transactions.csv")
    consumer = Consumer(event_queue)

    # Create threads
    producer_thread = threading.Thread(target=producer.run)
    consumer_thread = threading.Thread(target=consumer.run)

    # Start both threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for both threads to finish
    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()

