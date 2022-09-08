
v1=' '
v2=' '
v3=' '
v4=' '
v5=' '
v6=' '
v7=' '
v8=' '
v9=' '


positionOfVariables = [v1,v2,v3,v4,v5,v6,v7,v8,v9]

print(f' {v1} | {v2} | {v3} \n {v4} | {v5} | {v6}\n {v7} | {v8} | {v9}')

# originalGame = f'{v1} | {v2} | {v3} | \n {v4} | {v5} | {v6} |\n{v7} | {v8} | {v9} |'


userInput =int(input(" player one,enter your postion:\n"))
if 0<userInput<10:
        

    flag = True

    if flag:
        positionOfVariables[userInput-1] = 'x'
        flag = False
    else:
        positionOfVariables[userInput-1] = 'o'
        flag = True

else:
    print("Please enter correct input only")

    
print(positionOfVariables)



# game = {"v1":"" ,"v2":"","v3":"","v4":"","v5":"","v6":"","v7":"","v8":""}
# print(game[ f'{"v1"} | {"v2"} | {"v3"} | \n {"v4"} | {"v5"} | {"v6"} |\n{"v7"} | {"v8"} | {"v9"} |'])