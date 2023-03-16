import cpu_scheduling_algorithms as scheduling_algorithms


def main():
    #Initialize a set of processes

    p1 = scheduling_algorithms.Process(0, 5, 2)
    p2 = scheduling_algorithms.Process(1, 6, 2)
    p3 = scheduling_algorithms.Process(2, 3, 1)
    p4 = scheduling_algorithms.Process(3, 3, 3)
    p5 = scheduling_algorithms.Process(4, 5, 2)
    p6 = scheduling_algorithms.Process(6, 4, 3)

    processes = [p1, p2, p3, p4, p5, p6]
    time_quantum = 2 # used for Round Robin algorithm only
    scheduler = scheduling_algorithms.CPUScheduler(processes, time_quantum)

    print("FCFS algorithm results: ")
    scheduler.first_come_first_served()
    print(" ")
    print("=====================================")
    print("=====================================")
    print(" ")

    print("SJF algorithm results: ")
    scheduler.shortest_job_first()
    print(" ")
    print("=====================================")
    print("=====================================")
    print(" ")

    print("Round Robin algorithm results: ")
    scheduler.round_robin()
    print(" ")
    print("=====================================")
    print("=====================================")
    print(" ")

    print("Priority algorithm results: ")
    scheduler.priority_based()
    print(" ")
    print("=====================================")
    print("=====================================")
    print(" ")


if __name__ == "__main__":
    main()



