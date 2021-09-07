
def BubbleSort(Array):
  
     anyswaps = 1
     length = len(Array) # SET length TO LENGTH(Array)
     print ("length =",length)
     while anyswaps == 1 :# WHILE anyswaps = 1 DO
        print ("********************* NEW PASS ***********************")
        index = 0   # SET index TO 0
        anyswaps = 0 # SET anyswaps TO 0
        while index < length - 1: #WHILE index <= length - 1 DO 
            print (Array)

            if Array[index] > Array[index + 1] :# IF Array[index] > Array[index+1] THEN
                anyswaps = 1 # SET anyswaps TO 1
                temp = Array[index] # SET temp TO Array[index]
                print ("temp =",temp)
                Array[index] = Array[index + 1]# SET Array[index] TO Array[index+1]
                print ("Array[index + 1] =",Array[index + 1])
                Array[index + 1] = temp # SET Array[index + 1] TO temp
                print ("Array[index] =",Array[index])
            index = index + 1# SET index TO index+1
            print ("index =",index)
            # END IF
        # END WHILE
    # END WHILE 
     return Array

 
x = BubbleSort([65, 34, 28, 68, 52, 21  ])
print (x)



