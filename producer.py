
import csv
import time
from queue import Queue


class CSVProducer:
    def __init__(self, csv_path, q, delay=1.0):
        self.csv_path = csv_path
        self.q = q
        self.delay = delay

    def start(self):
        try:
            with open(self.csv_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    print(f"[Producer] Sending: {row}")
                    self.q.put(row)

                    time.sleep(self.delay)

        finally:
            # Tell the consumer that there are no more events
            self.q.put(None)
            print("[Producer] Finished sending events.")


if __name__ == "__main__":
    q = Queue()
    producer = CSVProducer("transactions.csv", q)
    producer.start()
