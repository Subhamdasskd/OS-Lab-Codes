# Function to find the waiting time for all processes
def find_waiting_time(processes, n, waiting_time):
    remaining_time = [0] * n  # Remaining time for each process
    
    # Copy the burst time into remaining_time[]
    for i in range(n):
        remaining_time[i] = processes[i][1]
    
    complete = 0  # Total processes completed
    t = 0  # Current time
    minm = float('inf')  # Minimum remaining time
    shortest = 0  # Index of the process with the shortest remaining time
    check = False  # Flag to check if any process arrived
    
    # Process until all processes get completed
    while complete != n:
        # Find process with the minimum remaining time among the processes
        # that arrived till the current time (t)
        for j in range(n):
            if (processes[j][2] <= t) and (remaining_time[j] < minm) and remaining_time[j] > 0:
                minm = remaining_time[j]
                shortest = j
                check = True
        
        if check == False:
            t += 1
            continue
        
        # Reduce remaining time by one
        remaining_time[shortest] -= 1
        
        # Update minimum
        minm = remaining_time[shortest]
        if minm == 0:
            minm = float('inf')
        
        # If a process gets completely executed
        if remaining_time[shortest] == 0:
            complete += 1
            check = False
            
            # Find finish time of current process
            finish_time = t + 1
            
            # Calculate waiting time
            waiting_time[shortest] = (finish_time - processes[shortest][1] - processes[shortest][2])
            
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0
        
        # Increment time
        t += 1

# Function to calculate turn around time
def find_turnaround_time(processes, n, waiting_time, turnaround_time):
    # Calculating turnaround time by adding burst time and waiting time
    for i in range(n):
        turnaround_time[i] = processes[i][1] + waiting_time[i]

# Function to calculate average time
def find_avg_time(processes, n):
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Function to find waiting time of all processes
    find_waiting_time(processes, n, waiting_time)
    
    # Function to find turn around time for all processes
    find_turnaround_time(processes, n, waiting_time, turnaround_time)
    
    # Display processes along with all details
    print("Processes    Burst Time     Arrival Time   Waiting Time   Turn-Around Time")
    total_waiting_time = 0
    total_turnaround_time = 0
    for i in range(n):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turnaround_time = total_turnaround_time + turnaround_time[i]
        print(f"  {i + 1}\t\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print(f"\nAverage waiting time = {total_waiting_time / n:.5f}")
    print(f"Average turn around time = {total_turnaround_time / n:.5f}")

# Driver code
if __name__ == "__main__":
    # Process ID, Burst Time, Arrival Time
    processes = [
        [1, 6, 1],  # Process 1 has burst time 6 and arrival time 1
        [2, 8, 1],  # Process 2 has burst time 8 and arrival time 1
        [3, 7, 2],  # Process 3 has burst time 7 and arrival time 2
        [4, 3, 3]   # Process 4 has burst time 3 and arrival time 3
    ]
    n = len(processes)
    
    find_avg_time(processes, n)
