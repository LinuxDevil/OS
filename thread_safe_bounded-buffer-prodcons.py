import array
import random
import threading
import time


class ProdCons:
    BUFFER_SIZE = 5
    buffer = BUFFER_SIZE * [-1]
    producer_index = 0
    consumer_index = 0
    lock = threading.Lock()

    def producer(self):
        while True:
            item = random.randint(0, 9)
            self.lock.acquire()
            if (self.producer_index + 1) % self.BUFFER_SIZE == self.consumer_index:
                print('Terminated Producer: Index:', self.producer_index)
                print('Terminated Producer: Buffer:', self.buffer)
                self.lock.release()
                break
            self.buffer[self.producer_index] = item
            print('Producer: Produced', item)
            self.producer_index = (self.producer_index + 1) % self.BUFFER_SIZE
            print('Producer: Index:', self.producer_index)
            print('Producer: Buffer:', self.buffer)
            self.lock.release()

    def consumer(self):
        while True:
            self.lock.acquire()
            if self.consumer_index == self.producer_index:
                print('Terminated Consumer: Index:', self.consumer_index)
                print('Terminated Consumer: Buffer:', self.buffer)
                self.lock.release()
                break
            item = self.buffer[self.consumer_index]
            self.buffer[self.consumer_index] = -1
            self.consumer_index = (self.consumer_index + 1) % self.BUFFER_SIZE
            print('Consumer: Consumed', item)
            print('Consumer: Index:', self.consumer_index)
            print('Consumer: Buffer:', self.buffer)
            self.lock.release()
            time.sleep(0.01)

    def run(self):
        threads = []
        producer_thread = threading.Thread(target=self.producer)
        consumer_thread = threading.Thread(target=self.consumer)
        threads.append(producer_thread)
        threads.append(consumer_thread)
        producer_thread.start()
        consumer_thread.start()
        for thread in threads:
            thread.join()


if __name__ == '__main__':
    prod = ProdCons()
    prod.run()
