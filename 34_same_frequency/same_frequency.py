def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_dict = {}
    for char in str(num1):
        num1_dict[char] = num1_dict.get(char, 0) + 1

    num2 = str(num2)
    num2_dict = {}
    for char in str(num2):
        num2_dict[char] = num2_dict.get(char, 0) + 1

    return True if num1_dict == num2_dict else False