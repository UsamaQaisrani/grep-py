import queue
import threading
class Reader:
    def read_line_by_line(self, file_path):
        q = queue.Queue()
        producer_thread = threading.Thread(target=self.producer, args=(file_path, q))

        producer_thread.start()
        self.consumer(q)
        producer_thread.join()


    def producer(self, file_path, queue):
        with open(file_path, "r") as file:
            for line in file:
                queue.put(line.strip())
            queue.put(None)

    def consumer(self, queue):
        while True:
            line = queue.get()
            if line is None:
                break
            print("Processed: :", line)

            
