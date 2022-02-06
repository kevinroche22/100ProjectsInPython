## Define addition function
def add(*args):
    """ Calculates the sum of inputs. """
    sum = 0
    for i in args:
        if type(i) != int and type(i) != float:
            return "Inputs must be numeric."
        sum += i
    return sum

## Define subtraction function
def subtract(firstNumber, *args):
    """ Subtracts all other arguments from the first number. """
    if type(firstNumber) != int and type(firstNumber) != float:
        return "Inputs must be numeric."
    result = firstNumber
    for i in args:
        if type(i) != int and type(i) != float:
            return "Inputs must be numeric."
        result -= i
    return result

## Define multiplication function
def multiply(*args):
    """ Calculates the product of inputs. """
    product = 1
    for i in args:
        if type(i) != int and type(i) != float:
            return "Inputs must be numeric."
        product *= i
    return product

## Define division function
def divide(firstNumber, *args):
    """ Divides the first number by the second argument, and each successive argument from the result of the previous calculation. """
    if type(firstNumber) != int and type(firstNumber) != float:
        return "Inputs must be numeric."
    result = firstNumber
    for i in args:
        if type(i) != int and type(i) != float:
            return "Inputs must be numeric."
        result /= i
    return result

## Add to operations dictionary
operationsDictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
