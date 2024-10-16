# Function to find the waiting time for all processes
def findWaitingTime(processes, n, burst_time, waiting_time):
    # Waiting time for first process is 0
    waiting_time[0] = 0

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

# Function to calculate turn around time
def findTurnAroundTime(processes, n, burst_time, waiting_time, turnaround_time):
    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# Function to calculate average waiting and turnaround time
def findAverageTime(processes, n, burst_time):
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Function to find waiting time for all processes
    findWaitingTime(processes, n, burst_time, waiting_time)

    # Function to find turn around time for all processes
    findTurnAroundTime(processes, n, burst_time, waiting_time, turnaround_time)

    # Display the process details
    print("Processes    Burst time    Waiting time    Turn around time")
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        print(f" {i + 1}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage waiting time = {total_waiting_time / n}")
    print(f"Average turn around time = {total_turnaround_time / n}")

# Function to implement SJF
def sjfScheduling(processes, n, burst_time):
    # Sort processes based on burst time
    sorted_processes = sorted(zip(processes, burst_time), key=lambda x: x[1])
    
    # Extract sorted processes and burst times
    processes_sorted, burst_time_sorted = zip(*sorted_processes)

    # Call function to calculate average time
    findAverageTime(processes_sorted, n, burst_time_sorted)

# Driver code
if __name__ == "__main__":
    processes = [1, 2, 3, 4]  # Process IDs
    burst_time = [6, 8, 7, 3]  # Burst times for each process

    n = len(processes)
    sjfScheduling(processes, n, burst_time)
