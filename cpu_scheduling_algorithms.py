
'''
Description: 
    This is the file that contains the CPU scheduler class and the Process class.
    4 CPU scheduling algorithms are implemented in this file:
        1. First Come First Served (FCFS)
        2. Shortest Job First (SJF)
        3. Round Robin (RR)
        4. Priority Based

Author: 
    Masood Ahmed


'''


class Process:
    def __init__(self, arrival_time, burst_time, priority) -> None:
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.turn_around_time = 0 #Initially, has a value of zero but you should update it
        self.waiting_time = 0 #Initially, has a value of zero but you should update it

class CPUScheduler:
    def __init__(self, processes, time_quantum) -> None:
        self.processes = processes
        self.time_quantum = time_quantum
    
    # Non pre-emptive
    def first_come_first_served(self):
        """
        Implements the first-come-first-served (FCFS) scheduling algorithm (non-pre-emptive).

        Parameters:
            self (Scheduler): An instance of the Scheduler class.

        Returns:
            - Prints the process table with the process number, arrival time, burst time, priority, finish time, turnaround time,
            and waiting time.
            - Prints the average waiting time and average turnaround time.
        """

        # sort the processes based on their arrival time
        sorted_processes = sorted(self.processes, key=lambda p: p.arrival_time)
        
        # putting the arrival times and burst times into lists
        arrival_times, burst_times = [], []

        for i in range(len(sorted_processes)):
            arrival_times.append(sorted_processes[i].arrival_time)
            burst_times.append(sorted_processes[i].burst_time)
        
        current_time = arrival_times[0]
        finish_time = []
        tracker = 0

        while tracker < len(sorted_processes) - 1:
            # calculate the finish time of the current process
            finish = current_time + burst_times[tracker]
            tracker += 1
            finish_time.append(finish)

            # update the current time to the next process's arrival time or the finish time of the current process
            if finish > arrival_times[tracker]:
                current_time = finish
            else:
                current_time = arrival_times[tracker]
        
        finish_time.append(current_time + burst_times[tracker])

        # a list for turn around time
        T_AT = []
        # a list for waiting time
        W_T = []

        
        for i in range(len(sorted_processes)):
            # calculate the turn around time of each process
            T_AT.append(finish_time[i] - arrival_times[i])

        for i in range(len(sorted_processes)):
            # calculate the waiting time of each process
            W_T.append(T_AT[i] - burst_times[i])

        # print a table showing the arrival time, burst time, finish time, turn around time, and waiting time of each process
        print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format('Process', 'Arrival', 'Burst', 'Finish', 'Turnaround', 'Waiting'))

        for i in range(len(sorted_processes)):
            print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(str(i+1), str(arrival_times[i]), str(burst_times[i]), str(finish_time[i]), str(T_AT[i]), str(W_T[i])))
        
        # finding average waiting and turn around times
        t_sum, w_sum = 0, 0

        for i in range(len(sorted_processes)):
            t_sum+=T_AT[i]
            w_sum+=W_T[i]

        # printing the average waiting and turn around times
        print("\nAverage turn around time: {:.2f}".format(t_sum/len(sorted_processes)))
        print("Average waiting time: {:.2f}".format(w_sum/len(sorted_processes)))


    # non-premptive
    def shortest_job_first(self):
        """
            Implements the shortest job first (SJF) algorithm for a non-preemptive CPU scheduling.

            Parameters:
                self (Scheduler): An instance of the Scheduler class.

            Returns:
                - Prints the process table with the process number, arrival time, burst time, priority, finish time, turnaround time,
                and waiting time.
                - Prints the average waiting time and average turnaround time.
        """

        n = len(self.processes)     # get the number of processes
        # sorting the processes by arrival time
        processes = sorted(self.processes, key=lambda x: x.arrival_time)

        # creating a new list to track processes
        track_processes = []
        complete = 0
        for i in range(n):
            add = [processes[i].arrival_time, processes[i].burst_time, 0, False]
            track_processes.append(add)

        # handling the case in which there could be multiple processes with the same arrival time = 0
        process_arrival_times = []
        for i in range(n):
            if track_processes[i][0] == 0:
                process_arrival_times.append(track_processes[i])

        # now sorting the processes with 0 arrival time according to the burst time
        process_arrival_times = sorted(process_arrival_times, key=lambda x: x[1])

        process_arrival_times[0][2] = process_arrival_times[0][1]
        process_arrival_times[0][3] = True
        complete += 1

        # initializing the current time
        current_time = process_arrival_times[0][1]
        ready_queue = []

        # Loop through the processes to schedule them
        while complete != n:
            # Add processes to the ready queue if their arrival time is less than or equal to the current time,
            # they are not completed and they are not already in the ready queue
            for i in range(n):
                if track_processes[i][0] <= current_time and track_processes[i][3] == False and track_processes[i] not in ready_queue:
                    ready_queue.append(track_processes[i])
            # now sorting the ready queue according to the burst time
            ready_queue = sorted(ready_queue, key=lambda x: (x[1],x[0]))
            # Choose the process with the shortest burst time from the ready queue
            new_process = ready_queue.pop(0)
            index = track_processes.index(new_process)
            # update the completion time, set the process as completed and update the current time
            track_processes[index][2] = current_time + track_processes[index][1]
            track_processes[index][3] = True
            current_time += track_processes[index][1]
            complete+=1

        # Calculate turnaround time (TAT) and waiting time (WT) for each process
        T_AT = []
        W_T = []

        for i in range(n):
            T_AT.append(track_processes[i][2] - track_processes[i][0])
        
        for i in range(n):
            W_T.append(T_AT[i] - track_processes[i][1])

        # Print the results for each process
        print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format('Process', 'Arrival', 'Burst', 'Finish', 'Turnaround', 'Waiting'))

        for i in range(n):
            print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(str(i+1), str(track_processes[i][0]), str(track_processes[i][1]), str(track_processes[i][2]), str(T_AT[i]), str(W_T[i])))
        
        # finding average waiting and turn around times
        t_sum = 0
        w_sum = 0
        for i in range(n):
            t_sum+=T_AT[i]
            w_sum+=W_T[i]

        # printing the average waiting and turn around times
        print("\nAverage turn around time: {:.2f}".format(t_sum/n))
        print("Average waiting time: {:.2f}".format(w_sum/n))
            


    def round_robin(self):
        """
            Implements the Round Robin scheduling algorithm to schedule the given list of processes.

            Parameters:
                self (Scheduler): An instance of the Scheduler class.

            Returns:
                - Prints the process table with the process number, arrival time, burst time, priority, finish time, turnaround time,
                and waiting time.
                - Prints the average waiting time and average turnaround time.
        """

        qt = self.time_quantum      # Set the time quantum for the algorithm.
        n = len(self.processes)     # Get the number of processes in the list.

        # sorting the processes by arrival time
        processes = sorted(self.processes, key=lambda x: x.arrival_time)

        # Create a new list to track the processes and initialize it with the arrival time, burst time, remaining time,
        # completion status, and process ID for each process in the original list.
        track_processes = []
        complete = 0    # to keep track of the number of processes that have been completed
        for i in range(n):
            processId = 'p'+str(i+1)
            add = [processes[i].arrival_time, processes[i].burst_time, 0, False, processId]
            track_processes.append(add)

        # putting the original burst time in a list in order to print the table later.
        burst_times = []
        for i in range(n):
            burst_times.append(track_processes[i][1])

        # current time
        current_time = processes[0].arrival_time      # Set the current time to the arrival time of the first process.
        ready_queue = []      # Initialize an empty list to store processes that are ready to execute.
        previous_process = None
        process_in = []

        # Continue executing processes until all processes are complete.
        while complete != n:

            # Add processes to the ready queue if they have arrived, have not completed yet, and have not already been added
            # to the queue. Also, make sure that the process that was just executed is not added back to the queue again.
            for i in range(n):
                if track_processes[i][0] <= current_time and track_processes[i][3] == False and track_processes[i] != previous_process and track_processes[i][4] not in process_in:
                    ready_queue.append(track_processes[i])
                    process_in.append(track_processes[i][4])

            if previous_process != None:
                ready_queue.append(previous_process)

            # Get the first process from the ready queue and execute it for the time quantum, or until it completes if its
            # remaining time is less than the time quantum.
            new_process = ready_queue.pop(0) # popping the first process from the ready queue
 
            index = track_processes.index(new_process)
            if (track_processes[index][1] - qt) < 0:
                track_processes[index][2] = current_time + (track_processes[index][1])
                current_time += (track_processes[index][1])
            else:
                track_processes[index][2] = current_time + qt
                current_time += qt

            # Update the remaining time for the executed process and check if it has completed.
            track_processes[index][1] -= qt

            if track_processes[index][1] <= 0:
                track_processes[index][3] = True
                complete+=1
                previous_process = None
            else:
                previous_process = track_processes[index]

        # Calculate the turnaround time and waiting time for each process and print the table.
        T_AT = []    # List to store the turnaround times.
        W_T = []    # List to store the waiting times.

        for i in range(n):
            T_AT.append(track_processes[i][2] - track_processes[i][0])
        
        for i in range(n):
            W_T.append(T_AT[i] - burst_times[i])

        # Print the results for each process
        print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format('Process', 'Arrival', 'Burst', 'Finish', 'Turnaround', 'Waiting'))

        for i in range(n):
            print("{:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(str(i+1), str(track_processes[i][0]), burst_times[i], str(track_processes[i][2]), str(T_AT[i]), str(W_T[i])))
        
        # finding average waiting and turn around times
        t_sum = 0
        w_sum = 0
        for i in range(n):
            t_sum+=T_AT[i]
            w_sum+=W_T[i]

        # printing the average waiting and turn around times
        print("\nAverage turn around time: {:.2f}".format(t_sum/n))
        print("Average waiting time: {:.2f}".format(w_sum/n))



    def priority_based(self):
        """
            A function to perform priority-based scheduling on the list of processes in the scheduler.

            Assumptions:
                - Non-preemptive approach is implemented as it is not mentioned in the question what to implement.
                - The lower the number of priority, the higher the priority, i.e., process p1 with priority 1 has a higher priority than
                process p2 with priority 2.

            Parameters:
                self (Scheduler): An instance of the Scheduler class.

            Returns:
                - Prints the process table with the process number, arrival time, burst time, priority, finish time, turnaround time,
                and waiting time.
                - Prints the average waiting time and average turnaround time.
        """

        n = len(self.processes)     # get the number of processes
        # sorting the processes by arrival time
        processes = sorted(self.processes, key=lambda x: x.arrival_time)

        # creating a new list to track processes
        track_processes = []
        complete = 0
        for i in range(n):
            add = [processes[i].arrival_time, processes[i].burst_time, 0, False, processes[i].priority]
            track_processes.append(add)

        # handling the case in which there could be multiple processes with the same arrival time = 0
        process_arrival_times = []
        for i in range(n):
            if track_processes[i][0] == 0:
                process_arrival_times.append(track_processes[i])

        # now sorting the processes with 0 arrival time according to the burst time
        process_arrival_times = sorted(process_arrival_times, key=lambda x: x[4])

        process_arrival_times[0][2] = process_arrival_times[0][1]
        process_arrival_times[0][3] = True
        complete += 1

        # initializing the current time
        current_time = process_arrival_times[0][1]
        ready_queue = []


        while complete != n:
            # adding processes to the ready queue if they have arrived and are not completed
            for i in range(n):
                if track_processes[i][0] <= current_time and track_processes[i][3] == False and track_processes[i] not in ready_queue:
                    ready_queue.append(track_processes[i])
            
            # now sorting the ready queue according to the priority (the lower the number of priority, the higher the priority) 
            # and then arrival time
            ready_queue = sorted(ready_queue, key=lambda x: (x[4],x[0]))

            # selecting the process with the highest priority from the ready queue
            new_process = ready_queue.pop(0)
            index = track_processes.index(new_process)
            track_processes[index][2] = current_time + track_processes[index][1]
            track_processes[index][3] = True
            current_time += track_processes[index][1]
            complete+=1

        # calculating turnaround time and waiting time for each process
        T_AT = []
        W_T = []

        for i in range(n):
            T_AT.append(track_processes[i][2] - track_processes[i][0])
        
        for i in range(n):
            W_T.append(T_AT[i] - track_processes[i][1])

        # Print the results for each process
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format('Process', 'Arrival', 'Burst', 'Priority', 'Finish', 'Turnaround', 'Waiting'))

        for i in range(n):
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15}".format(str(i+1), str(track_processes[i][0]), str(track_processes[i][1]), str(track_processes[i][4]), str(track_processes[i][2]), str(T_AT[i]), str(W_T[i])))
        
        # finding average waiting and turn around times
        t_sum = 0
        w_sum = 0
        for i in range(n):
            t_sum+=T_AT[i]
            w_sum+=W_T[i]

        # printing the average waiting and turn around times
        print("\nAverage turn around time: {:.2f}".format(t_sum/n))
        print("Average waiting time: {:.2f}".format(w_sum/n))
        

