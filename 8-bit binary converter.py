binary = input(str("please enter 8-bit binary number"))
denary = 0
length = len(binary) - 1
index = length
total = 0
while index <= length and index > -1 :
    print ("binary[index]",binary[index])
    print ("index",index)
    print ("binary[index]", binary[index])
    if index != 0 :
        power = 7 - index
        print ("power", power)
        total = (pow(2,power) )* int(binary[index])
        print ("total " , total)
    else:
        power = 7
        print ("power", power)
        total = (pow(2,power) )* int(binary[index])
        print ("total " , total)
    denary =  denary + total 
    print ("binary[index]",binary[index])
    print ("denary",denary) 
    index = index - 1
    print ("binary[index]",binary[index])
    print ("index",index)
    print ("//////////////////////////////////////////////////////////")
print ("denary",denary) 
 

