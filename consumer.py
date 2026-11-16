
import time
from queue import Queue


class Consumer:
    def __init__(self, q):
        self.q = q
        self.total_amount = 0.0

    def start(self):
        while True:
            event = self.q.get()

            # Stop signal from producer
            if event is None:
                self.q.task_done()
                break

            print(f"[Consumer] Received: {event}")
            self.process(event)

            self.q.task_done()

    def process(self, event):
        time.sleep(0.5)

        amount = float(event["amount"])
        self.total_amount += amount

        print(
            f"[Consumer] Processed transaction: "
            f"{event['transaction_id']} | "
            f"Amount: {amount:.2f} | "
            f"Running total: {self.total_amount:.2f}"
        )


if __name__ == "__main__":
    q = Queue()
    consumer = Consumer(q)
    consumer.start()

