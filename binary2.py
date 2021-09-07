
#BINARY SEARCH V2
    
import timeit

def BinarySearch ( Array, Target):
    start = 0
    end = len(Array) - 1
    found = False
    while start <= end and found == False :
        print ("start =",start) #Creating tracing table for Debugging
        middle = int((start + end )/2)
        print ("middle =",middle) #Creating tracing table for Debugging
        print ("Array[middle] =", Array[middle])
        print ("*******************")   #Creating tracing table for Debugging
        if Array[middle] == Target:
            
        
            found = True
            print (Target ,"is in the list")
        elif Target < Array[middle]:
            end = middle - 1 
        else:
            start = middle + 1
    if found == False :
        print ("this search item is not in the list")
    return found

def ListCreator (size):
    x = list(range(0,size))
    return x 

L10 = ListCreator(10)
L50 = ListCreator(50)
L100 = ListCreator(100)
L200= ListCreator(200)
L1000 = ListCreator(1000)
L60 = ListCreator(60)

B = BinarySearch(L60,64)
print (B)



#print(min(timeit.repeat(lambda: BinarySearch(L10,0),repeat= 1,number = 1)))
