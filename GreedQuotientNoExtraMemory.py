#This program calculates the greed quotient.
#Run from command line:
#python GreedQuotientNoExtraMemory.py [size] [elements of list separated by ,]

#Commented code for taking input from a text file.
#import sys
#fileName=""
#for f in sys.argv[1:]:
#    fileName=f
#try:
#    file=open(fileName,'r')
#    for line in file.readlines():
#        listOfNumbers.extend(int(i) for i in line.split()) 
#    file.close()
#except IOError:
#    print "Cannot read from file:"

listOfNumbers=[]
#Calculate greed quotient. 
#Iterate over the sorted input list backwards.
def greedQuotient():
    
    #If all elements of the list are greater than or equal to number of elements, return the greed quotient as number of elements.
    if listOfNumbers[0]>=length:
        return length
    #If all elements of the list are equal to 1, return the greed quotient 1.    
    elif listOfNumbers[length-1]==1:
        return 1
    #If all elements of the list are 0, return 0.    
    elif listOfNumbers[length-1]==0:
        return 0
    #Keep finding the element in the list which is greater than or equal to the number of elements above it.   
    i=length-1    
    while(listOfNumbers[i]>=length-i):       
        i-=1
    return length-i-1   
                     
#Sort the list using randomised quick sort.
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

import sys            
length=int(sys.argv[1])
listOfNumbers=map(int,sys.argv[2].split(','))
if length==len(listOfNumbers):   
    p=0
    r=length-1
    quickSortRandomised(listOfNumbers, p, r)
    gq=greedQuotient()
    print "Greed Quotient is ",gq
else:
    print "Entered size and number of elements don't match." 