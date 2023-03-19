# This code implements the Producer-Consumer problem using
# a circular buffer in Python. The buffer has a fixed size
# of 5, and each item in the buffer is a random integer
# between 0 and 9.

import random


class ProdCons:
    BUFFER_SIZE = 5
    buffer = BUFFER_SIZE * [-1]
    producer_index = 0
    consumer_index = 0

    def producer(self):
        print("\tProducer")
        if (self.producer_index + 1) % self.BUFFER_SIZE == self.consumer_index:
            print('\t\tTerminated Producer: Index: ', self.producer_index)
            print('\t\tTerminated Producer: Buffer: ', self.buffer)
            return
        self.buffer[self.producer_index] = random.randint(0, 9)
        print('\t\tProducer: Produced ', self.buffer[self.producer_index])
        self.producer_index = (self.producer_index + 1) % self.BUFFER_SIZE
        print('\t\tProducer: Index: ', self.producer_index)
        print('\t\tProducer: Buffer: ', self.buffer)

    def consumer(self):
        print("\tConsumer")
        if self.producer_index == self.consumer_index:
            print('\t\tTerminated Consumer: Index: ', self.consumer_index)
            print('\t\tTerminated Consumer: Buffer: ', self.buffer)
            return
        consumed = self.buffer[self.consumer_index]
        print('\t\tConsumer: Consumed ', consumed)
        self.buffer[self.consumer_index] = -1
        self.consumer_index = (self.consumer_index + 1) % self.BUFFER_SIZE
        print('\t\tConsumer: Index: ', self.consumer_index)
        print('\t\tConsumer: Buffer: ', self.buffer)

    def run(self):
        for i in range(0, self.BUFFER_SIZE):
            print('| Run: Running Iteration ', i + 1)
            print('| Run: Buffer: ', self.buffer)
            self.producer()
            self.consumer()
            print('---------------------------')


if __name__ == '__main__':
    prod = ProdCons()
    prod.run()
