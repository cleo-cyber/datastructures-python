# Implement a prototype service for resource estimation
# Given a set of n tasks, the ith (0<=i<1) tasks runs from time start[i] through end[i]. 
# Implement a task scheduler method that finds the minimum number of machines required to complete the tasks.
# A task can be scheduled on exactly one machine, and one machine can run only one task at a time.

# Example
# suppose n=5, start=[1,8,3,9,6], end=[7,9,6,14,7]

# Consider the following task schedule:
# Time in parenthesis are the inclusinve start and end times for each job
# machine 1:[(1,7), (8,9)]
# machine 2:[(3,6), (9,14)]
# machine 3:[(6,7)]

# Here the  number of machines required is 3


# Function Description
# Complete the function getMinMachines below
# getMinMachines has the following parameter(s):
# int start[n]: the start time of the tasks
# int end[n]: the end time of the tasks

# Returns
# int: the minimum number of machines required to run all the tasks

# Constraints
# 1<=n<=2*10^5
# 1<=start[i]<=end[i]<=10^9

# Solution
def getMinMachines(start, end):
    n = len(start)
    start.sort()
    end.sort()
    i = 0
    j = 0
    machines = 0
    while i < n:
        if start[i] < end[j]:
            machines += 1
            i += 1
        else:
            i += 1
            j += 1
    return machines