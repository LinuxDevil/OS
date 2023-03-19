from collections import deque


class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def execute(self, time_slice):
        """
        Simulate the execution of the process for a given time slice.

        Returns the amount of time taken.
        """
        if self.remaining_time > time_slice:
            self.remaining_time -= time_slice
            return time_slice
        else:
            completed_time = self.remaining_time
            self.remaining_time = 0
            return completed_time


def get_next_arrival_time(processes, current_time):
    """
    Calculate the time until the next process arrives.

    Returns the next arrival time or None if no processes are pending.
    """
    remaining_processes = [p for p in processes if p.remaining_time > 0 and p.arrival_time > current_time]
    if remaining_processes:
        return min(p.arrival_time for p in remaining_processes)
    else:
        return None


def run_round_robin(queue, processes, time_slice, current_time):
    """
    Run the Round Robin algorithm on the given queue of processes.

    Returns a list of tuples containing the process ID and completion time for each process.
    """
    completed = []

    while queue:
        process = queue.popleft()
        time_taken = process.execute(time_slice)
        current_time += time_taken

        print(f"Process {process.pid} executed for {time_taken} time units.")
        print(f"Remaining burst time for process {process.pid}: {process.remaining_time}")

        if process.remaining_time > 0:
            queue.append(process)
        else:
            completed.append((process.pid, current_time))
            print(f"Process {process.pid} completed at time {current_time}.")

        next_arrival_time = get_next_arrival_time(processes, current_time)
        if next_arrival_time is not None:
            if not queue and next_arrival_time > current_time:
                print(f"Waiting for next process arrival at time {next_arrival_time}.")
            else:
                queue.append(process)

    return completed


def round_robin(processes, time_slice):
    """
    Schedule a list of processes using the Round Robin algorithm.

    Takes a list of `Process` objects and a time slice value as input,
    and returns a list of tuples containing the process ID and
    completion time for each process.
    """
    queue = deque(processes)
    completed = []
    current_time = 0

    while queue:
        completed += run_round_robin(queue, processes, time_slice, current_time)
        current_time = max(completion_time for _, completion_time in completed)

    return completed


if __name__ == '__main__':
    _processes = [
        Process(1, 0, 10),
        Process(2, 2, 5),
        Process(3, 4, 8),
        Process(4, 6, 2),
        Process(5, 8, 4)
    ]

    _completed = round_robin(_processes, 3)

    print(_completed)
