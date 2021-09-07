# Queue FIFO

def popd(y):  # pop functioin
    del y[0] # remove first element 
    return y

def push(x,i): # add item to array 
    x.append(i)
    print(x)
    head = x[0]
    tail = x[len(queue)-1]
    print ("head of queue :",head)
    print ("tail of queue :",tail)
    return x

def pop1(x) :
    popd(x)
    head = x[0]
    tail = x[len(queue)-1]
    print ("head of queue :",head)
    print ("tail of queue :",tail)
    return x
    
print("Welcome to the Queue simulator:")

queue = []
pointer = -1

##head = queue[0]
##tail = queue[len(queue)-1]

while  pointer >= -1 :
    print (" press 1 : push an item into the queue")
    print (" press 2 : pop an item from the queue")
    ans = int(input("Please enter your choice:"))
    if ans == 1 :
          item = int(input("please enter the number you would like to push"))
          push(queue,item)
          pointer = pointer + 1
          print (queue)
    else :
          pop1(queue)
          pointer = pointer -1
          print (queue)
