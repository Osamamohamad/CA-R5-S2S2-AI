def user_info(name: str, age: int) -> str:
    '''
    This function takes a name and age as input and returns them in a formatted string.
    Args:
        name (str): The name of the user.
        age (int): The age of the user.
    Returns:
        returns a formatted string containing the user's information.
    Example:
        user_info("osama", 21) will return "Name: osama, Age: 21"
    '''
    return(f"Name: {name}, Age: {age}")