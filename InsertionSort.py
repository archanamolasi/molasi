# This program performs  Insertion sort.
# Run from Command line:
# python InsertionSort.py [Input_file_name].txt
# where [Input_file_name].txt is the text file of inputs.
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

#Perform insertion sort.
def insertionSort(listOfNumbers):
    for i in range(1,length):
        num=listOfNumbers[i]
        j=i-1
        while j>=0 and listOfNumbers[j]>num:
            listOfNumbers[j+1]=listOfNumbers[j]
            j-=1
        listOfNumbers[j+1]=num

length=len(listOfNumbers)  
print 'n is ',length
import time
start_time = time.time()   
insertionSort(listOfNumbers)
print "Time taken  %s seconds." % (time.time() - start_time)
print "Sorted list."
for i in range(0,length):
    print listOfNumbers[i]

    