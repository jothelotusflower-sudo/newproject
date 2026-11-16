
import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer


def main():
    # Create shared queue
    event_queue = Queue()

    # Instantiate producer and consumer
    producer = CSVProducer("transactions.csv", event_queue)
    consumer = Consumer(event_queue)

    # Create threads
    producer_thread = threading.Thread(target=producer.start)
    consumer_thread = threading.Thread(target=consumer.start)

    # Start both threads
    consumer_thread.start()
    producer_thread.start()

    # Wait for both threads to finish
    producer_thread.join()
    consumer_thread.join()

    print("[Pipeline] Streaming pipeline completed.")


if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()


