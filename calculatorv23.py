import re
import operator


def evaluateCalc(txt):
    opsPriorities = {
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
    }


    rpNotation = ""
    operatorStack = []

    for i in range(len(txt)):

        if re.search("\d",txt[i]):
            rpNotation += txt[i]

        elif txt[i] == "(":
            operatorStack.append(txt[i])

        elif txt[i] == ")":
            for j in range(len(operatorStack)):
                if operatorStack[-1] == "(":
                    operatorStack.pop()
                    break
                else:
                    rpNotation += operatorStack[-1]
                    operatorStack.pop()
        
        else:
            isAdded = False

            if len(operatorStack) == 0:

                operatorStack.append(txt[i])
            else:
                for j in range((len(operatorStack)-1), -1,-1):
                    
                    if operatorStack[j] =="("  and i == (len(operatorStack)-1):

                        operatorStack.append(txt[i])
                        isAdded = True
                    elif operatorStack[j] =="(":

                        operatorStack.insert(j+1, txt[i])
                        for k in range((len(operatorStack)-1),j+1,-1):
                           rpNotation += operatorStack[k]
                           operatorStack.pop()
                        isAdded = True
                    elif opsPriorities[txt[i]] > opsPriorities[operatorStack[j]]  and i == (len(operatorStack)-1):

                        operatorStack.append(txt[i])
                        isAdded = True
                    elif opsPriorities[txt[i]] > opsPriorities[operatorStack[j]]:

                        operatorStack.insert(j+1, txt[i])
                        for k in range((len(operatorStack)-1),j+1,-1):
                           rpNotation += operatorStack[k]
                           operatorStack.pop()
                        isAdded = True
                    elif opsPriorities[txt[i]] <= opsPriorities[operatorStack[j]] and j == 0:

                        operatorStack.insert(0, txt[i])
                        for k in range((len(operatorStack)-1),0,-1):
                           rpNotation += operatorStack[k]
                           operatorStack.pop()
                        isAdded = True

                    if isAdded:
                        break

    for i in range(len(operatorStack)):
        rpNotation += operatorStack[-1]
        operatorStack.pop()

    return rpNotation

                




    #CONVERTS CALC TO REVERSE POLISH NOTATION#######################
"""     
    rpNotation = ""
    #operatorStack = []
    skipCountdown = 0

    for i in range(len(txt)):


        if re.search("\d",txt[i]) and skipCountdown == 0:
            rpNotation += txt[i]

        elif skipCountdown != 0 :
            skipCountdown -= 1

        else:
            rpNotation += txt[i+1]
            rpNotation += txt[i]
            skipCountdown = 1

    print("Reverse Polish Notation:" , rpNotation) """
    #for i in range(len(operatorStack)):
        #rpNotation += operatorStack[i]

    ##################################################################

"""     ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    }

    calcStack = []

    for i in range(len(rpNotation)):


        if re.search("\d",rpNotation[i]):
            calcStack.append(rpNotation[i])
        else:
            top1Node = int(calcStack.pop())
            top2Node = int(calcStack.pop())
            result = ops[rpNotation[i]](top1Node,top2Node)
            calcStack.append(result)

    return calcStack[0] """

    

def checkValid(txt):
    regex = "\d|[+]|-|/|[*]|\s|[(]|[)]"

    for i in range(len(txt)):
        isCharValid = re.search(regex,txt[i])

        if isCharValid == None:
            print("Found an invalid character: " + txt[i])
            return False
        
    return True


userInput = input("Enter your calculation:")
print("\nUser inputted: "+ userInput +"\n")

txtArray = userInput.split(" ")
userInput = "".join(txtArray)

if checkValid(userInput) == True:
    rpNot = evaluateCalc(userInput)
    print(rpNot)

