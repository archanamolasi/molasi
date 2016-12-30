# This program performs  Quick sort with fixed partitioning.
# Run from Command line:
# python QuickSortFixedPartitionSolution2.py [Input_file_name].txt
# This program is an improved version of QuickSortFixedPartition.py which may give stack overflow error for large input values.
# QuickSortFixedPartitionSolution2.py is another Quick Sort solution which avoids this problem.
# This program uses an explicit data structure stack which keeps track of start and end values required in the partition function.

import sys
fileName=""
listOfNumbers=[]
for f in sys.argv[1:]:
    fileName=f
try:
    file=open(fileName,'r')
    for line in file.readlines():
        listOfNumbers.extend(int(i) for i in line.split()) 
    file.close()
except IOError:
    print ("Cannot read from file:") 

#Perform Quick Sort.
def quickSortIterative(listOfNumbers,p,r):
    # An explicit data structure to hold the values of start and end of the array used in the partitioning.
    stack=[]
    stack.append(p)
    stack.append(r)
    while(stack):
        start=stack.pop(0)
        end=stack.pop(0)
        q=partition(listOfNumbers,start,end)  
        if q-1>start:
            stack.append(start)
            stack.append(q-1)
            
        if q+1<end:
            stack.append(q+1)
            stack.append(end)
                     
def partition(listOfNumbers,p,r):
    i=p-1
    pivot=listOfNumbers[r]
    for j in range(p,r):
        if listOfNumbers[j]<pivot:
            i+=1
            listOfNumbers[i],listOfNumbers[j]=listOfNumbers[j],listOfNumbers[i]
    listOfNumbers[i+1],listOfNumbers[r]=listOfNumbers[r],listOfNumbers[i+1]        
    return i+1
    
length=len(listOfNumbers)
print 'n is ',length
import time
start_time = time.time() 
r=length-1
p=0     
quickSortIterative(listOfNumbers, p, r)
print "Time taken %s seconds ---" % (time.time() - start_time)
print "Sorted list."
for i in range(0,length):
    print listOfNumbers[i]