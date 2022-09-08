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

def printFunction():
    print(f'------|------|------| \n ------|------|------| \n -----|------|------|')

printFunction()



listOfBoxes =  {1:" " ,2 : " ",3 : " ",4:" ",5: "",6:" ",7:" ",8:" ",9:" "}
print(listOfBoxes)

flag = True

while True:
    if flag:
        userInput1 = int(input("first player turn : select your box\n"))
        listOfBoxes[userInput1] = 'X'
        flag=False
        

    else:
        userInput2 = int(input("second player turn : select your box\n"))
        listOfBoxes[userInput2] = 'o'
        flag=True
    print(listOfBoxes)








    




