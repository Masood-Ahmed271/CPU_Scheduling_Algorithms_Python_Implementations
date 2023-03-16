# Implementations of CPU Scheduling Algorithms

## Contributors:
---
Author: Masood Ahmed <br>
Email: masood20@connect.hku.hk<br>

---

## Description:

This repository contains different different CPU Scheduling algorithms implementations using python. It provides the basic statistics such as average turnaround time and waiting time.

## Background:

Scheduling of processes/work is done to finish the work on time. CPU Scheduling is a process that allows one process to use the CPU while another process is delayed (in standby). The purpose of CPU Scheduling is to make the system more efficient, faster, and fairer.

Whenever the CPU becomes idle, the operating system must select one of the processes in the line ready for launch. The selection process is done by a temporary (CPU) scheduler. The Scheduler selects between memory processes ready to launch and assigns the CPU to one of them.

## What is a process?

In computing, a process is the instance of a computer program that is being executed by one or many threads. It contains the program code and its activity. Depending on the operating system (OS), a process may be made up of multiple threads of execution that execute instructions concurrently.

## What is Process Scheduling?

Process Scheduling is the process of the process manager handling the removal of an active process from the CPU and selecting another process based on a specific strategy.

Process Scheduling is an integral part of Multi-programming applications. Such operating systems allow more than one process to be loaded into usable memory at a time and the loaded shared CPU process uses repetition time.

## What is the need for a CPU scheduling algorithm?

CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended. The main function of CPU scheduling is to ensure that whenever the CPU remains idle, the OS has at least selected one of the processes available in the ready-to-use line.

In Multiprogramming, if the long-term scheduler selects multiple I / O binding processes then most of the time, the CPU remains idle. The function of an effective program is to improve resource utilization.

If most operating systems change their status from performance to waiting then there may always be a chance of failure in the system. So in order to minimize this excess, the OS needs to schedule tasks in order to make full use of the CPU and avoid the possibility of deadlock.

## Objectives of Process Scheduling Algorithm:

- Utilization of CPU at maximum level. Keep the CPU as busy as possible.
- Allocation of CPU should be fair.
- Throughput should be Maximum. i.e. Number of processes that complete their execution per time unit should be maximized.
- Minimum turnaround time, i.e. time taken by a process to finish execution should be the least.
- There should be a minimum waiting time and the process should not starve in the ready queue.
- Minimum response time. It means that the time when a process produces the first response should be as less as possible.

## What are the different types of CPU scheduling algorithms?

There are mainly two types of scheduling methods:
- re-emptive Scheduling: Pre-emptive scheduling is used when a process switches from a running state to a ready state or from the waiting state to the ready state.
- Non-Preemptive Scheduling: Non-Preemptive scheduling is used when a process terminates, or when a process switches from a running state to waiting state.


## 1. First Come First Served (FCFS)

FCFS considered being the simplest of all operating system scheduling algorithms. First come first serve scheduling algorithm states that the process that requests the CPU first is allocated the CPU first and is implemented by using FIFO queue.

*Characteristics of FCFS:*
- FCFS supports non-preemptive and preemptive CPU scheduling algorithms.
- Tasks are always executed on a First-come, First-serve concept.
- FCFS is easy to implement and use.
- This algorithm is not much efficient in performance, and the wait time is quite high.

## 2. Shortest Job First (SJF)

Shortest job first (SJF) is a scheduling process that selects the waiting process with the smallest execution time to execute next. This scheduling method may or may not be preemptive. Significantly reduces the average waiting time for other processes waiting to be executed. The full form of SJF is Shortest Job First.

## 3. Round Robin (RR)

The Round-robin scheduling algorithm is a kind of preemptive First come, First Serve CPU Scheduling algorithm where each process in the ready state gets the CPU for a fixed time in a cyclic way (turn by turn). It is the oldest scheduling algorithm, which is mainly used for multitasking.

The Round robin scheduling algorithm is one of the CPU scheduling algorithms in which every process gets a fixed amount of time quantum to execute the process.

## 4. Priority Based Scheduling (PB)

Priority scheduling is one of the most common scheduling algorithms in batch systems. Each process is assigned a priority. Process with the highest priority is to be executed first and so on. Processes with the same priority are executed on first come first served basis. Priority can be decided based on memory requirements, time requirements or any other resource requirement. Also priority can be decided on the ratio of average I/O to average CPU burst time.

*Thank you for reading. Stay happy and stay safe :)*