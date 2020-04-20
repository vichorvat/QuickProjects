# Write a program that prints a pattern like this
# 7
# 66
# 555
# 4444
# 33333
# 222222
# 1111111
#
# Credit to @programmingtask on instagram for the task

inputNum = int(input("input: "))

def mainFunc(outputNum, amount):
    if amount <= inputNum:
        output = ""
        for i in range(0,amount):
            output = output + str(outputNum)
        print(output)
        mainFuncHelper((outputNum - 1), (amount + 1) )


mainFuncHelper(inputNum, 1)

