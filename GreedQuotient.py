#This program calculates the greed quotient.
#Run from command line:
#python GreedQuotient.py [size] [elements of list separated by ,]

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
def greedQuotient():
    #Auxillary storage.
    temp_list=[0]*(length+1)  
    for i in range(length-1,-1,-1):
        # Store count of elements>=length of list
        if listOfNumbers[i]>length:
            temp_list[length]+=1
        # Store the count of elements <length of list    
        else:
            temp_list[listOfNumbers[i]]+=1   
    max_till_now=0    
    # Traverse the auxillary storage backwards and count the total elements. As soon as the total of elements    
    # becomes >= its index i, return i.   
    for i in range(length,0,-1):
        max_till_now+=temp_list[i]
        if max_till_now>=i:
            return i

import sys            
length=int(sys.argv[1])
listOfNumbers=map(int,sys.argv[2].split(','))
if length==len(listOfNumbers):
    gq=greedQuotient()
    print "Greed Quotient is ",gq
else:
    print "Entered size and number of elements don't match."    