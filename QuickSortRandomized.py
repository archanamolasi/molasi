# This program performs  Quick sort with randomized partitioning.
# Run from Command line:
# python QuickSortRandomized.py [Input_file_name].txt
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

# Perform Quick Sort.
def quickSortRandomised(listOfNumbers,p,r):
    if p<r:
        q=partitionRandomised(listOfNumbers,p,r)  
        quickSortRandomised(listOfNumbers, p, q-1)
        quickSortRandomised(listOfNumbers, q+1,r)
import random        
def partitionRandomised(listOfNumbers,p,r):
    #Find a random pivot.  
    i=random.randint(p,r)
    #Swap the randomly chosen pivot element  with the last element of the list.
    listOfNumbers[i],listOfNumbers[r]=listOfNumbers[r],listOfNumbers[i]       
    return partition(listOfNumbers, p, r)
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
quickSortRandomised(listOfNumbers, p, r)
print "Time taken %s seconds ---" % (time.time() - start_time)
print "Sorted list."
for i in range(0,length):
    print listOfNumbers[i]