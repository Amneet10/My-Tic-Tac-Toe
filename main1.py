# firstBox = ' '
# secondBox = ' '
# thirdBox = ' '
# forthBox =' '
# fifthBox = ' '
# sixthBox = ' '
# seventhBox = ' '
# eightBox = ' '
# ninthBox = ' '

# allBoxeslist=[firstBox,secondBox,thirdBox,forthBox,fifthBox,sixthBox,seventhBox,eightBox,ninthBox]


# userInput = int(input("PlayerOne: Enter your Turn" ))

def printFunction(grid):
    print(f'{grid[1]}|{grid[2]}|{grid[3]}|\n -----{grid[4]}|{grid[5]}|{grid[6]}\n -----{grid[7]}|{grid[8]}|{grid[9]}')
   




listOfBoxes =  {1:" " ,2 : " ",3 : " ",4:" ",5: "",6:" ",7:" ",8:" ",9:" "}
print(listOfBoxes)

flag = True

while True:
    if flag:
        userInput1 = int(input("first player turn : select your box\n"))
        listOfBoxes[userInput1] = 'X'
        printFunction(listOfBoxes)
        flag=False
        

    else:
        userInput2 = int(input("second player turn : select your box\n"))
        listOfBoxes[userInput2] = 'o'
        printFunction(listOfBoxes)
        flag=True
    print(listOfBoxes)








    




