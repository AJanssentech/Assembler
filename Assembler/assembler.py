def interpreterMove(instruction) : 
    memoryInstruction = "6"
    if (instruction[1] == "Y") :
        memoryInstruction = memoryInstruction + str(1) 
        memoryInstruction += instruction[2]
        print(memoryInstruction)
    elif (instruction[1] == "x") : 
        memoryInstruction = memoryInstruction + str(0)
        memoryInstruction += instruction[2]
        print(memoryInstruction)

def interpreterAdd(instruction) :  
    memoryinstrion = "8" 
    memoryinstrion = memoryinstrion + instruction[1] + instruction[2] + str(4)
    print(memoryinstrion)

# branch if not equal
def inerpreterBNE(instruction):
    memomoryInstruction = "4"
    memomoryInstruction = memomoryInstruction +instruction[1] + instruction [2] + str(8)
    print(memomoryInstruction) 


def main () : 
    with open ("/Users/annelotjanssen/Desktop/Assembler/assembler.txt") as file : 
        x = 0
        y = 0 
        for i in file : 
            instruction = i.split()
            if(instruction[0] == "MOV" ) :
                interpreterMove(instruction)
            elif(instruction[0] == 'ADD') : 
                interpreterAdd(instruction)
            elif(instruction[0] == "BNE") :
                inerpreterBNE(instruction) 

                



                  


main()