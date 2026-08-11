def calculator(num1: float = None, num2: float = None, operation: str = None) -> str:
    """A mini calculator that performs addition, subtraction, division, and multiplication.

    Args:
        num1 (float): The first input number
        num2 (float): The second input number
        operation (str): 1=addition, 2=subtraction, 3=multiplication, 4=division

    Returns:
        str: The result of the calculation

    Example:
        >>> calculator(10.0, 5.0, 3)
        '50.0'
    """
    agen=True
    print("Welcome to the sample Calculator!")
    while agen:
        operation = input("Select an operation:\n1-addition +\n2-subtraction -\n3-multiplication *\n4-division /\n" \
            "Enter your chose (1/2/3/4) or ( exit ) to quit:"
        )
        if operation == "exit":
            agen=False
            return print("Thank you for you time.")
        num1 = float(input("Input first number : "))
        num2 = float(input("Input second number : "))

        while operation == "4" and num2 == 0.0:
            num2 = float(input("Number 2 can't be zero for division. Please enter it again: "))

        if operation == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "4":
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("I am sorry, that is not a valid operation.")
            return calculator()



    return str(result)



def MultiplicationTable(number: int = None) -> None:
    """Generate a Multiplication Table.

    Args:
        number (int): The input number

    Prints:
        The multiplication table of the input number, from 1 to 10.

    Example:
        >>> MultiplicationTable(4)
        4 * 1 = 4
        4 * 2 = 8
        4 * 3 = 12
        4 * 4 = 16
            .
            .
            .
        4 * 10 = 40
    """
    while True:
        number = input("Please, enter an integer number: ")
        try:
            number = int(number)
            break
        except ValueError:
            print("That is not a valid integer, please try again.")

    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

def TwinPrimes() -> str:
    '''
    this function print twin primes less than 1000
    If two consecutive odd numbers are both prime then they are known as twin primes
    Args
        None
    Returns:
        str: print twin primes
    Example:
        >>> TwinPrimes()
        3   and   5
        5   and   7
            |
            |
            |
        821 and 823
        827 and 829
        857 and 859
        881 and 883
    '''
    print("Twin Primes:")
    for j in range(3, 1000, 2):
        num1 = j
        num2 = j + 2

        ChickNum1 = True
        i = 2
        while i < num1:
            if num1 % i == 0:
                ChickNum1 = False
                break
            i += 1

        ChickNum2 = True
        i = 2
        while i < num2:
            if num2 % i == 0:
                ChickNum2 = False
                break
            i += 1

        if ChickNum1 and ChickNum2:
            print(f"{num1} and {num2}")

def PrimeFactors(num:int)->list:
    '''
        this function return prime factors whith input
        Args
            None
        Returns:
            list: returns Prime Factors
        Example:
            >>> PrimeFactors(56)
            [2,2,2,7]
        '''
    result = []
    num = int(num)
    for i in range(2,num):
        while num % i == 0 :
            num/=i
            result.insert(0,i)
    return result



def decBin(num: int) -> str:
    '''
    this function converts a decimal number to binary number
    Args
        num (int): The input Number
    Returns:
        str: Binary number
    Example:
        >>> decBin(5)
            101
        >>> decBin(0)
            0
    '''
    if num == 0:
        return "0"

    Binary = ""
    n = num
    while n > 0:
        remaind = n % 2
        Binary = str(remaind) + Binary
        n = n // 2
    return f"decimal {num} to Binary {Binary}"


def PerfectNum(start : int , end : int)-> list:
    '''
    this function finds all perfect numbers within a given range
    Args
        start (int): The start of the range
        end (int): The end of the range
    Returns:
        list: Perfect numbers found in the range
    Example:
        >>> PerfectNum(0, 100)
            [0, 6, 28]
    '''
    result=[]
    
    for i in range(start,end+1):
            ChickTotal=0
            resultSingleNum = []
            for j in range (1,i):
                if i % j == 0 :
                    ChickTotal+=j
                    resultSingleNum.insert(0,j)
            if ChickTotal == i: result.insert(0,i)
    return result

