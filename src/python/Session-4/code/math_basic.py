def isPrime(num: int) -> bool:
    '''
    this function takes an integer as input and returns True if the number is prime, otherwise returns False.
    Args:
        num (int): The number to check for primality.
    Returns:
        bool: True if the number is prime, False otherwise.
    Example:
        >>> isPrime(7)
        True
        >>> isPrime(10)
        False
    '''
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def factorial(num: int) -> int:
    '''
    this function takes an integer as input and returns the factorial of that number.
    Args:
        num (int): The number to calculate the factorial of.
    Returns:
        int: The factorial of the input number.
    Example:
        >>> fact(5)
        120

    '''
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num * factorial(num - 1)