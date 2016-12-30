# This program performs  Quick sort with fixed partitioning.
# Run from Command line:
# python QuickSortFixedPartition.py [Input_file_name].txt
# This program may give stack overflow error for large input values.
# QuickSortFixedPartitionSolution2.py is another Quick Sort solution which avoids this problem.
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
    print "Cannot read from file:"

#Perform Quick Sort.
def quickSort(listOfNumbers,p,r):
    if p<r:
        q=partition(listOfNumbers,p,r)  
        quickSort(listOfNumbers, p, q-1)
        quickSort(listOfNumbers, q+1,r)
    
def partition(listOfNumbers,p,r):
    i=p-1
    #Last element chosen as pivot.
    pivot=listOfNumbers[r]
    for j in range(p,r):
        if listOfNumbers[j]<pivot:
            i+=1
            listOfNumbers[i],listOfNumbers[j]=listOfNumbers[j],listOfNumbers[i]
    listOfNumbers[i+1],listOfNumbers[r]=listOfNumbers[r],listOfNumbers[i+1]        
    return i+1
    
length=len(listOfNumbers)
print 'n is ' ,length
import time
start_time = time.time() 
r=length-1
p=0     
quickSort(listOfNumbers, p, r)
print "Time taken %s seconds " % (time.time() - start_time)
print "Sorted list."
for i in range(0,length):
    print listOfNumbers[i]