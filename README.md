# IAS-Simulation
======================IAS IMPLEMENTATION IN PYTHON======================

AIM: To implement IAS architecture and test various instruction set using it.

PROCESS :
 
      i)Registers involved in implemented IAS:
          a)AC  : Accumulator
	          Accumulate/hold results of an ALU operation
	  b)IR  : Instructions Register
	          8 bit OPCode of the instruction to be executed.
	  c)IBR : Instructions Buffer register
	          Holds the RHS instruction temporarily till time comes for its execution
	  d)MBR : Memory BUffer register
	         Contains a word to be read/stored in memory for I/O
	  e)MQ  : Multiplier/Quotioent Register
	          LSB of product
	  f)PC  : Program Counter
	          Holds the next instruction’s address
	  g)MAR : Memory Adress register
	          Specifies the address in memory of the word to be written/read into MBR
	     
	     
	ii)Program execution involves two cycles:-
	    a)Fetch cycle:
	       Opcode of the upcoming instruction is loaded into the IR.And the address part is loaded into the MAR. 
	       In this phase the value of Program Counter(PC) is moved to the Memory Address Register(MAR) and the value at the memory location(at value of  MAR) is loaded in Memory Buffer Register(MBR).
	       
	   Once this is done, the OPCODE of the LEFT instruction is loaded into the Instruction Register(IR)and the address portion is loaded into the MAR and the right instruction is loaded into the Instruction Buffer Register(IBR).
	   
	   b)Execute cycle:
	           In this the ALU perform actions as specified by the instrcution(OPCode).
	    
           Order of the process is :
             1.)User will hae to select which process he wants to do
             2.)input of values from user according to the instruction selected.
             3.)Check the value stored in each memory location, toggle through the options displayed. Increment or decrement through the memory, or choose execute.To go into the execution cycle. The instructions are hard-coded into the memory hence choose the memory location from where one wishes to execute the instructions.
             4.)Storing  of final answer into the memory location specified.
             5.)6th option is HALT and  hence it will stop taking input.
             
Choices available to users:-
  1.)Addition
  2.)Subtraction
  3.)Left shift (LSH)
  4.)Right shift(RSH)
  5.)Perimeter of Square
  6.)HALT
	            
	            
CREATED BY PANDEY SHOURYA PRASAD	            
