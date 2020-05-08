# Write a program that prints a pattern like this
# 11111
# 1   1
# 1   1
# 1   1
# 11111
# When given the input 5

# Credit to @programmingtask on instagram for the task


size = int(input("square size: "))

def fullLine(length,output):
    if size > length:
        fullLine((length + 1), (output + str(1)))
    else:
        print(output)

def middle(length):
    if length > 0:
        output = str(1)
        for i in range (0,size - 2):
            output = output + " "
        output = output + str(1)
        print(output)
        middle(length - 1)


if size < 2:
    print(1)
else:
    fullLine(0,"")
    middle(size-2)
    fullLine(0,"")
