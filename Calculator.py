#Calculator app
    # read input
    # figure out order of operations
    
    # consider edge cases
        #divide by zero

    #formula : string => "1 + 2 + 3"

def Calculator(formula):
    """Calculator handler executes calculation and returns float result"""
    ans = 0
    #read input into a list
    tokens = formula.split()
    print(tokens)

    #execute multiplication and division first
    oopList = oopFirstPass(tokens)

    print(oopList)
    
    #addition and subtraction second
    if (oopList is not None):
        tokens2 = oopList.split()
        print(tokens2)
        ans = oopSecondPass(tokens2)

    return ans

def oopFirstPass(tokens):
    """checks for add/sub operations to add to new string and executes mult/div operations"""
    oopList = ""
    num1 = None
    num2 = None
    operation = None
    for val in tokens:
        if (num1 is None):
            num1 = float(val)
            continue
        if (val == "+" or val == "-"):
            #add to oopList
            oopList += str(num1) + " " + val + " "
            num1 = None
            continue
        if (operation is None):
            operation = val
            continue
        if (num2 is None):
            num2 = float(val)
        
        # do multiply/division
        if (operation == "*"):
            num1 = multiply(num1, num2)
        elif (operation == "/"):
            num1 = divide(num1, num2)
        else:
            return "Incorrect Input Formula"
        num2 = None
        operation = None
    oopList += str(num1)    
    return oopList

def oopSecondPass(tokens):
    """executes add/sub operations and returns final result"""
    num1 = None
    num2 = None
    operation = None
    for val in tokens:
        if (num1 is None):
            num1 = float(val)
            continue
        if (operation is None):
            operation = val
            continue
        if (num2 is None):
            num2 = float(val)
        
        #do add/subtract
        if (operation == "+"):
            num1 = add(num1, num2)
        elif (operation == "-"):
            num1 = subtract(num1, num2)
        else:
            return "Incorrect Input Formula"
        num2 = None
        operation = None
    return num1

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


    

answer = Calculator("1 * 2 * 2 / 3")
print(answer)