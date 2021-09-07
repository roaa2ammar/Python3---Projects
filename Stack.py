# stack (LIFO)

def popd(y):  # pop functioin
    last = len(y) - 1 # get last index
    del y[last] # remove last element 
    return y


def push(x,i): # add item to array 
    x.append(i)
    print(x)
    return x

def pop1(x):  
    #remove = x.pop()
    popd(x)
    return x

# main

print("Welcome to the Stack simulator:")

stack = []
pointer = -1


while  pointer >= -1 :
    print (" press 1 : push an item into the stack")
    print (" press 2 : pop an item from the stack")
    ans = int(input("Please enter your choice:"))
    if ans == 1 :
              item = int(input("please enter the number you would like to push"))
              push(stack,item) # call push function
              pointer = pointer + 1  # change the pointer 
              print (stack)
    else :
              pop1(stack)  # call pop function
              pointer = pointer - 1
              print (stack) 

    


