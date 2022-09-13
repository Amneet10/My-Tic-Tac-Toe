def printFunction(grid):
    print(f'{grid[1]} | {grid[2]} | {grid[3]}\n -----\n{grid[4]} | {grid[5]} | {grid[6]}\n -----\n{grid[7]} | {grid[8]} | {grid[9]}')
   
def checkWinner(grid):
    if ((grid[1]==grid[4]==grid[7]) and grid[1] ) or ((grid[4]==grid[5]==grid[6]) and grid[4]) or ((grid[1]==grid[2]==grid[3]) and grid[1]) or((grid[7]==grid[8]==grid[9]) and grid[7]) or ((grid[2]==grid[5]==grid[8]) and grid[2]) or ((grid[1]==grid[5]==grid[9]) and grid[1]) or ((grid[3]==grid[5]==grid[7]) and grid[3]) or (( grid[3]==grid[6]==grid[9]) and grid[3]):
        print("winner found")
        return True
    else:
        return False


listOfBoxes =  {1:"" ,2 : "",3 : "",4:"",5: "",6:"",7:"",8:"",9:""}
print(listOfBoxes)

flag = True
moveCounter = 0

while True:
    if moveCounter < 9:
        userInput1 = int(input(f" {'1st' if flag else '2nd'} player turn, enter your box number\n"))
        if listOfBoxes[userInput1] in ('X','o'):
            print("value is already entered.Plaese choose a differnt number")
        else:
            if moveCounter < 9:
                listOfBoxes[userInput1] = 'X' if flag else 'o' #a if condition else b
                moveCounter+=1
                if checkWinner(listOfBoxes) == True:
                    break
                printFunction(listOfBoxes)
                flag = not flag

    else:
        print("game drawn")
        break


printFunction(listOfBoxes)










    




