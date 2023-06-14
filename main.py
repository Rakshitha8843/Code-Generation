def printLineCode(i):
    var = open('output.txt', 'a') # opens a file for appending
    temps = 1
    line = i
    x = 0
    if len(line) == 1:
        if line[0].isdigit():
            var.write('L #' + line[0] + '\n\n')
        else:
            var.write('L '+line[0] + '\n\n')
    else:
        while len(line) != 1:
            if line[x+2] in "+-*/":
                    op = line[x+2]
                    num1 = '' + line[x]
                    num2 = '' + line[x+1]
                    placehold = ''

                    if num2.isdigit():
                        placehold = '#'

                    if num1.isdigit():
                        var.write('L #' + num1 + '\n\n')
                    else:
                        var.write('L ' + num1 + '\n\n')

                    if op == '+':
                        var.write('A ' + placehold + num2 + '\n\n')
                    elif op == '-':
                        var.write('S ' + placehold + num2 + '\n\n')
                    elif op == '*':
                        var.write('M ' + placehold + num2 + '\n\n')
                    elif op == '/':
                        var.write('D ' + placehold + num2 + '\n\n')
                    else:
                        var.write('N ' + placehold + num2 + '\n\n')
                   
                    var.write('ST $' + str(temps) + '\n\n')
                    line[x] = '$' + str(temps)
                    temps += 1
                    line.pop(x + 1)
                    line.pop(x + 1)
                    x = 0                        
            else:
                    x += 1
        var.close()           
                    
open('output.txt', 'w').close() # opens a file for writing
file = open('input.txt', 'r') # opens a file for reading
for line in file:
    line = line.strip() # removes whitespaces in the beginning and end of a line
    line = line[0:len(line)]
    tokens = line.split(" ") # split each word into a list
    printLineCode(tokens) # function call
file.close()
