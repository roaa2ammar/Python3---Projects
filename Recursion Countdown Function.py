# Countdown using a recursive function

def countdown(n):
    if n == 0:  # base case
        return
    else: 
        print (n)
        countdown(n - 1) # Call function
    return
        
countdown(10)   # Call function
 

