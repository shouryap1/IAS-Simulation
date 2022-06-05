def decimalToBinary(n):
    if(n<=1023):
        l=bin(n).zfill(12)
        return l.replace('b', '0')
    else:
        return bin(n).replace("0b","")

def binaryToDecimal(n):
    return str(int(n,2))
main_memory=[]
Memory=[0]*1000                                             #Memory
counter=500                                                 #This helps in storing data in memory at positions
x=counter                     
PC=0                                                        #Program counter
PC_dup=PC                                                   #duplicate of program counter
MAR=0                                                       #Memory Address Register
MBR=0                                                       #Memory Buffer  Register
IBR=0                                                       #Instruction Buffer Register (which holds RHS instruction)     
IR=0                                                        #Instruction Register (holds OPCode of LHS instruction)
AC=0                                                        #Accumalator
MQ=0                                                        #Memory Quotient
while(1):
    print("1->addition")
    print("2->subtraction(1st number - 2nd number)")       
    print("3->Left Shift[LSH]")
    print("4->Right Shift[RSH]")                             #Gives choice to user to select which operation he wants to perform.
    print("5->Perimeter of square")
    print("6-> HALT")
    
    i=int(input("Enter your choice: "))                     #Choice input by user.
    if(i==6):
        break
    
    
    if(i==1):
        num_1=int(input("Enter first number : "))               #Number 1 (input ) by user. 
        Memory[counter]=num_1                                   #saved in memory at a particular position.
        counter=counter+1                                       #counter increased by one. 
        num_2=int(input("Enter second number : "))              #Number 2 (input) by user.
        Memory[counter]=num_2                                   #saved in memory at a particular position.   
        counter=counter+1                                       #counter increased by one.
        Memory[PC_dup]="00000001"+decimalToBinary(x)+"00000101"+decimalToBinary(x+1)        #LOAD M({x}),ADD M({x+1})   #First instruction in adding two numbers(taken input by user).   
        PC_dup=PC_dup+1                                       
        Memory[PC_dup]="00000000000000000000"+"00100001"+decimalToBinary(x)      #Second instruction in adding two numbers (taken input by user).
        PC_dup=PC_dup+1
        MAR=PC                                              #MAR takes value of PC.
        MBR=Memory[MAR]                                     #MBR stores instruction in it which it gets from memory.
        IBR=MBR[12:]                                        #IBR stores RHS instruction.
        IR="00000001"                                       #Stores OPCode(8bits) of LHS instruction.
        MAR=decimalToBinary(x)                              #Stores address(12bits)
        MBR=Memory[int(binaryToDecimal(MAR))]               #Stores values which it gets from Memory. 
        AC=MBR                                              #Stores value in it which MBR has.
        IR="00000101"                                       #OPCode of RHS instruction(earlier) is stored.
        MAR=decimalToBinary(x+1)                  # New Address present in RHS instruction(earlier) is stored 
        MBR=Memory[int(binaryToDecimal(MAR))]               #Stores value which it gets from Memory.
        AC=AC+MBR                                           #Accumalator adds value which it has earlier with current value of MBR.
        IBR=""
        PC=PC+1                                             #Program counter is increased by one.
        MAR=PC                                              #MAR stores PC value
        MBR=Memory[MAR]                                     #MBR stores value which it gets from Memory using MAR address.
        IR="00100001"                                       #OPCode(8bits) is stored in IR.
        MAR=int(MBR[28:])           #Stores value of address present in instruction.
        MBR=AC                                              #MBR stores value of AC.
        Memory[int(binaryToDecimal(str(MAR)))]=MBR           #Now at location given in instruction the final calucalted value is being stored.
        print(Memory[int(binaryToDecimal(str(MAR)))])            #Prints the final answer.    
        PC=PC+1                                             #Increases Program Counter.
        x=x+2                                               
    if(i==2):
        num_1=int(input("Enter first number : "))               #Number 1 (input ) by user. 
        Memory[counter]=num_1                                   #saved in memory at a particular position.
        counter=counter+1                                       #counter increased by one. 
        num_2=int(input("Enter second number : "))              #Number 2 (input) by user.
        Memory[counter]=num_2                                   #saved in memory at a particular position.   
        counter=counter+1                                       #counter increased by one.
        Memory[PC_dup]="00000001"+decimalToBinary(x)+"00000101"+decimalToBinary(x+1)  #LOAD M({x}),ADD M({x+1})     #First instruction in adding two numbers(taken input by user).   
        PC_dup=PC_dup+1                                       
        Memory[PC_dup]="00000000000000000000"+"00100001"+decimalToBinary(x)     #Second instruction in adding two numbers (taken input by user).
        PC_dup=PC_dup+1
        MAR=PC                                              #MAR takes value of PC.
        MBR=Memory[MAR]                                     #MBR stores instruction in it which it gets from memory.
        IBR=MBR[12:]                                        #IBR stores RHS instruction.
        IR="00000001"                                       #Stores OPCode(8bits) of LHS instruction.
        MAR=decimalToBinary(x)                              #Stores address(12bits)
        MBR=Memory[int(binaryToDecimal(MAR))]               #Stores values which it gets from Memory. 
        AC=MBR                                              #Stores value in it which MBR has.
        IR="00000101"                                       #OPCode of RHS instruction(earlier) is stored.
        MAR=decimalToBinary(x+1)                            #New Address present in RHS instruction(earlier) is stored 
        MBR=Memory[int(binaryToDecimal(MAR))]               #Stores value which it gets from Memory.
        AC=AC-MBR                                           #Accumalator adds value which it has earlier with current value of MBR.
        IBR=""
        PC=PC+1                                             #Program counter is increased by one.
        MAR=PC                                              #MAR stores PC value
        MBR=Memory[MAR]                                     #MBR stores value which it gets from Memory using MAR address.
        IR="00100001"                                       #OPCode(8bits) is stored in IR.
        MAR=int(MBR[28:])                                   #Stores value of address present in instruction.
        MBR=AC                                              #MBR stores value of AC.
        Memory[int(binaryToDecimal(str(MAR)))]=MBR          #Now at location given in instruction the final calucalted value is being stored.
        print(Memory[int(binaryToDecimal(str(MAR)))])       #Prints the final answer.    
        PC=PC+1                                             #Increases Program Counter.
        x=x+2  
    if(i==3):
        num_1=int(input("Enter number to be left shifted[LSH] : "))               #Number 1 (input ) by user. 
        Memory[counter]=num_1                                   #saved in memory at a particular position.
        counter=counter+1                                       #counter increased by one. 
        MQ=2
        Memory[PC_dup]="00000001"+decimalToBinary(x)+"00010100"+"000000000000"  #instruction 
        PC_dup=PC_dup+1
        Memory[PC_dup]="00000000000000000000"+"00100001"+decimalToBinary(x)    #Second instruction
        PC_dup=PC_dup+1
        MAR=PC                                             
        MBR=Memory[MAR]
        IBR=MBR[12:]
        IR="00000001"
        MAR=decimalToBinary(x)
        MBR=Memory[int(binaryToDecimal(MAR))] 
        AC=MBR
        IR="00010100"
        AC=AC*MQ                                            #AC stores  the result
        PC=PC+1                                             #Program Counter is increased by one. 
        MAR=PC                                              #MAR stores value of PC in it.
        MBR=Memory[MAR]                                     #MBR stores value which it gets from Memory.
        IR="00100001"                                       #OPCode(8bits) is stored in IR
        MAR=int(MBR[28:])                #Stores value of address present in instruction.
        MBR=AC                                              #MBR stores value present in AC.
        Memory[int(binaryToDecimal(str(MAR)))]=MBR               #Value in MBR gets stored in Memory at particular position
        print(Memory[int(binaryToDecimal(str(MAR)))])            #Prints final answer.
        PC=PC+1                                             #Program Counter increased by one.
        x=x+1
    if(i==4):
        num_1=int(input("Enter number to be Right shifted[RSH] : "))               #Number 1 (input ) by user. 
        Memory[counter]=num_1                                   #saved in memory at a particular position.
        counter=counter+1                                       #counter increased by one. 
        MQ=2
        Memory[PC_dup]="00000001"+decimalToBinary(x)+"00010101"+"000000000000"
        PC_dup=PC_dup+1
        Memory[PC_dup]="00000000000000000000"+"00100001"+decimalToBinary(x)    
        PC_dup=PC_dup+1
        MAR=PC
        MBR=Memory[MAR]
        IBR=MBR[12:]
        IR="00000001"
        MAR=decimalToBinary(x)
        MBR=Memory[int(binaryToDecimal(MAR))] 
        AC=MBR
        IR="00010101"
        AC=AC//MQ                                           #AC stores  the result
        PC=PC+1                                             #Program Counter is increased by one. 
        MAR=PC                                              #MAR stores value of PC in it.
        MBR=Memory[MAR]                                     #MBR stores value which it gets from Memory.
        IR="00100001"                                       #OPCode(8bits) is stored in IR
        MAR=int(MBR[28:])                #Stores value of address present in instruction.
        MBR=AC                                              #MBR stores value present in AC.
        Memory[int(binaryToDecimal(str(MAR)))]=MBR               #Value in MBR gets stored in Memory at particular position
        print(Memory[int(binaryToDecimal(str(MAR)))])            #Prints final answer.
        PC=PC+1                                             #Program Counter increased by one.
        x=x+1    
    if(i==5):
        num_1=int(input("Enter side of square : "))               #Number 1 (input ) by user. 
        Memory[counter]=num_1                                   #saved in memory at a particular position.
        counter=counter+1                                       #counter increased by one. 
        Memory[PC_dup]="00000001"+decimalToBinary(x)+"00000101"+decimalToBinary(x+1)                                        # f'LOAD M({x}),ADD M({x})'          #First instruction in adding two numbers(taken input by user).   
        PC_dup=PC_dup+1
        
                                               
        Memory[PC_dup]="00000000000000000000"+"00100001"+decimalToBinary(x)                                    #f'STOR M({x})'                       #Second instruction in adding two numbers (taken input by user).
        PC_dup=PC_dup+1
        MAR=PC                                              #MAR takes value of PC.
        MBR=Memory[MAR]
        #print(MBR)                                     #MBR stores instruction in it which it gets from memory.
        IBR=MBR[20:]                                        #IBR stores RHS instruction.
        IR="00000001"                                       #Stores OPCode(8bits) of LHS instruction.
        MAR=(MBR[8:20])  
        #print(binaryToDecimal(MAR))               #Stores address(12bits)
        MBR=Memory[int(binaryToDecimal(MAR))]               #Stores values which it gets from Memory. 
        AC=MBR                                              #Stores value in it which MBR has.
        IR="00000101"                                       #OPCode of RHS instruction(earlier) is stored.
        MAR=(IBR[8:])                  # New Address present in RHS instruction(earlier) is stored 
        MBR=Memory[int(binaryToDecimal(MAR))]               #Stores value which it gets from Memory.
        AC=AC+MBR                                           #Accumalator adds value which it has earlier with current value of MBR.
        IBR=""
        PC=PC+1                                             #Program counter is increased by one.
        Memory[PC_dup]=f'JUMP M({PC_dup},20:39)'             
        PC_dup=PC_dup+1
        MAR=PC                                              
        MBR=Memory[MAR]                                     
        IR="00001110"
        MAR=decimalToBinary(int(MBR[7:8]))
        IR="00000101"
        MAR=decimalToBinary(x)
        MBR=Memory[int(binaryToDecimal(MAR))]
        AC=AC+MBR
        IBR=""
        PC=PC+1
        
        Memory[PC_dup]=f'JUMP M({PC_dup-1},20:39)'            
        PC_dup=PC_dup+1
        MAR=PC                                              
        MBR=Memory[MAR]                                     
        IR="00001110"
        MAR=decimalToBinary(int(MBR[7:8]))
        IR="00000101"
        MAR=decimalToBinary(x)
        MBR=Memory[int(binaryToDecimal(MAR))]
        AC=AC+MBR
        IBR=""
        PC=PC+1

        Memory[PC_dup]=f'JUMP M({PC_dup-1},20:39)'            
        PC_dup=PC_dup+1
        MAR=PC                                              
        MBR=Memory[MAR]                                     
        IR="00001110"
        MAR=decimalToBinary(int(MBR[7:8]))
        IR="00000101"
        MAR=decimalToBinary(x)
        MBR=Memory[int(binaryToDecimal(MAR))]
        AC=AC+MBR
        IBR=""
        PC=PC+1

        
        MAR=PC
        MBR=Memory[MAR]
        IR="00100001"                                       #OPCode(8bits) is stored in IR.
        
        MAR=x               #Stores value of address present in instruction.
        MBR=AC                                              #MBR stores value of AC.
        Memory[MAR]=MBR               #Now at location given in instruction the final calucalted value is being stored.
        print(Memory[MAR])            #Prints the final answer.    
        PC=PC+1                                             #Increases Program Counter.
        x=x+1         